"""Obtain pinned public inputs. Fail if a publisher has changed a source file."""
from pathlib import Path
import argparse,csv,gzip,hashlib,json,urllib.request,zipfile
BASE=Path(__file__).resolve().parent
RAW=BASE/'raw'
parser=argparse.ArgumentParser()
parser.add_argument('--cache',type=Path,help='Optional directory containing the original named downloads')
args=parser.parse_args()
RAW.mkdir(exist_ok=True)
manifest=json.loads((BASE/'source_manifest.json').read_text())
for entry in manifest:
    dest=RAW/entry['file']
    if dest.exists():data=dest.read_bytes()
    elif 'snapshot' in entry:data=gzip.decompress((BASE/entry['snapshot']).read_bytes())
    elif args.cache and (args.cache/entry['file']).is_file():data=(args.cache/entry['file']).read_bytes()
    else:
        request=urllib.request.Request(entry['url'],headers={'User-Agent':'StateCoordinationResearch/2026-09-20'})
        with urllib.request.urlopen(request,timeout=90) as response:data=response.read()
    actual=hashlib.sha256(data).hexdigest()
    if actual!=entry['sha256']:
        raise SystemExit(f"Source checksum differs: {entry['file']}. Expected {entry['sha256']}, got {actual}. Stop and document a version change; do not silently substitute new data.")
    if not dest.exists():dest.write_bytes(data)
    print('Verified',entry['file'])

for archive,filename,target in [
    ('state_capacity_v1.zip','StateCapacityDataset_v1.dta','state_capacity_v1/StateCapacityDataset_v1.dta'),
    ('ddcg_replication.zip','DDCGdata_final.dta','ddcg_replication/replication_files_ddcg/DDCGdata_final.dta')]:
    with zipfile.ZipFile(RAW/archive) as z:
        names=[n for n in z.namelist() if Path(n).name==filename]
        if len(names)!=1:raise SystemExit(f'Expected one {filename} in {archive}')
        dest=RAW/target;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(z.read(names[0]))

import openpyxl
book=openpyxl.load_workbook(RAW/'mpd2023_sources.xlsx',read_only=True,data_only=True)
with open(RAW/'mpd_GDPpc.csv','w',newline='') as f:
    csv.writer(f).writerows(book['GDPpc'].iter_rows(values_only=True))
book.close()
(RAW/'manifest.json').write_text(json.dumps(manifest,indent=2))
print('All pinned inputs ready. Run analyze.py, audit_gdp_sources.py, then validate_and_plot.py.')
