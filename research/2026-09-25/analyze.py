#!/usr/bin/env python3
"""Reproduce one administrative notice, not an industry-wide access measure.

Python standard library only. See README.md for source and interpretation limits.
"""
import argparse
import csv
import hashlib
import io
import json
import re
import urllib.request
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

BASE = Path(__file__).resolve().parent
URL = "https://www.mee.gov.cn/gkml/zj/bgt/200910/t20091022_173901.htm"
DATE = "2005-01-26"
STANDARD = "《汽车加速行驶车外噪声限值及测量方法》（GB1495-2002）第二阶段限值"
HEADERS = ["source_row", "institution_raw", "test_scope_raw", "venues_raw", "document_date", "source_id"]
VENUES = {
    "交通部公路交通实验场": "V01",
    "东风汽车实验场（襄樊）": "V02",
    "海南汽车试验研究所": "V03",
    "长春农安汽车试验场": "V04",
}


class TableParser(HTMLParser):
    """Read actual cells; exclude rowspan continuation rows and contact fields."""
    def __init__(self):
        super().__init__()
        self.rows, self.row, self.cell = [], None, None

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.row = []
        if tag in ("td", "th") and self.row is not None:
            self.cell = []

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self.cell is not None:
            # Formatting whitespace only; preserve names and punctuation.
            self.row.append(re.sub(r"\s+", "", "".join(self.cell)))
            self.cell = None
        if tag == "tr" and self.row is not None:
            self.rows.append(self.row)
            self.row = None


def extract(raw):
    html = raw.decode("utf-8")
    if DATE not in html or "环办〔2005〕13号" not in html:
        raise ValueError("Source identity/date not confirmed; inspect before using.")
    parser = TableParser()
    parser.feed(html)
    rows = []
    for row in parser.rows:
        if len(row) >= 4 and row[0].isdigit() and 1 <= int(row[0]) <= 12:
            rows.append(dict(zip(HEADERS, row[:4] + [DATE, "S03"])))
    validate(rows)
    return rows


def validate(rows):
    if [r["source_row"] for r in rows] != [str(i) for i in range(1, 13)]:
        raise ValueError("Expected the 12 ordered rows of this notice, exactly once.")
    if len({r["institution_raw"] for r in rows}) != 12:
        raise ValueError("Duplicate or missing institution names.")
    for row in rows:
        if row["test_scope_raw"] != STANDARD or row["document_date"] != DATE or row["source_id"] != "S03":
            raise ValueError("Mixed dates, sources, or scopes: do not pool silently.")
        names = row["venues_raw"].split("、")
        if len(names) != len(set(names)) or any(n not in VENUES for n in names):
            raise ValueError("Unknown or duplicate venue; resolve names explicitly.")


def csv_text(rows, fields):
    buf = io.StringIO(newline="")
    writer = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue()


def calculate(rows):
    validate(rows)
    links = []
    for row in rows:
        for name in row["venues_raw"].split("、"):
            links.append({"source_row": row["source_row"], "venue_id": VENUES[name], "venue_raw": name})
    counts = Counter(x["venue_raw"] for x in links)
    multiplicity = Counter(len(r["venues_raw"].split("、")) for r in rows)
    summary = {
        "document_date": DATE,
        "document_id": "环办〔2005〕13号",
        "population": "Only the institutions named in this additional-qualification notice",
        "unit": "Institution listed for GB1495-2002 stage-II testing",
        "institutions": len(rows),
        "distinct_listed_venue_names": len(counts),
        "institution_venue_links": len(links),
        "institutions_by_number_of_listed_venues": dict(sorted(multiplicity.items())),
        "venue_counts": [{"venue_id": VENUES[n], "venue_raw": n, "institutions_listing_venue": counts[n],
                          "denominator_institutions_in_notice": len(rows)} for n in VENUES],
        "not_measured": ["actual testing transactions", "manufacturer clients or ownership", "fees and waiting times",
                         "new entrant access", "physical capacity", "policy effects"],
    }
    return {
        "authorizations.csv": csv_text(rows, HEADERS),
        "institution_venue_links.csv": csv_text(links, ["source_row", "venue_id", "venue_raw"]),
        "summary.json": json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--html", type=Path, help="Re-extract a saved official HTML page")
    source.add_argument("--download", action="store_true", help="Re-extract the current official page (requires internet)")
    parser.add_argument("--check", action="store_true", help="Compare with committed outputs; do not overwrite")
    args = parser.parse_args()
    if args.html or args.download:
        raw = args.html.read_bytes() if args.html else urllib.request.urlopen(URL, timeout=45).read()
        rows = extract(raw)
        print("Downloaded/supplied HTML SHA256:", hashlib.sha256(raw).hexdigest())
    else:
        with (BASE / "authorizations.csv").open(encoding="utf-8", newline="") as stream:
            rows = list(csv.DictReader(stream))
    outputs = calculate(rows)
    for name, content in outputs.items():
        path = BASE / name
        if args.check:
            if not path.exists() or path.read_bytes() != content.encode("utf-8"):
                raise ValueError("Reproduction mismatch: " + name)
        else:
            path.write_text(content, encoding="utf-8")
    print("Verified" if args.check else "Wrote", ", ".join(outputs))


if __name__ == "__main__":
    main()
