"""Generate synthetic data for the state-coordination reproducibility demo.

The generated files are for workflow demonstration only and should not be
interpreted substantively.
"""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)

rng = np.random.default_rng(42)
sectors = ["Electronics", "Automobiles", "Shipbuilding", "Textiles", "Chemicals", "Machinery"]
dimensions = ["persistence", "specificity", "network_breadth", "allocation"]
years_pre = np.arange(1978, 1987)
years_panel = np.arange(1980, 1996)

# Passage-level coding data
rows = []
for sector in sectors:
    sector_strength = rng.normal(0, 1)
    for year in years_pre:
        for dim in dimensions:
            latent = sector_strength + 0.12 * (year - 1978) + rng.normal(0, 0.9)
            score = int(np.clip(np.round(latent + 1), 0, 2))
            rows.append({
                "source_id": f"SRC_{sector[:3].upper()}_{year}_{dim[:3].upper()}",
                "sector": sector,
                "year": year,
                "dimension": dim,
                "score": score,
                "passage_excerpt": "Synthetic passage for workflow demonstration only.",
                "coder_id": "demo",
                "confidence": rng.choice(["medium", "high", "low"], p=[0.45, 0.4, 0.15]),
                "review_status": rng.choice(["accepted", "needs_review"], p=[0.8, 0.2]),
                "notes": "Synthetic data; no substantive interpretation."
            })
passages = pd.DataFrame(rows)
passages.to_csv(DATA / "demo_coded_passages.csv", index=False)

# Sector-year panel with outcome generated from a simple synthetic DGP
support_raw = passages.groupby("sector")["score"].mean()
support_std = (support_raw - support_raw.mean()) / support_raw.std(ddof=0)
rows = []
for sector in sectors:
    unit_fe = rng.normal(0, 1)
    support = support_std.loc[sector]
    for year in years_panel:
        event_time = year - 1987
        post = year >= 1987
        common_trend = 0.04 * (year - 1980)
        treatment_path = 0.0 if not post else 0.12 * support * min(event_time + 1, 6)
        outcome = 2.0 + unit_fe + common_trend + treatment_path + rng.normal(0, 0.35)
        rows.append({
            "sector": sector,
            "year": year,
            "event_time": event_time,
            "entry_rate": outcome,
            "capital_intensity_pre": rng.normal(0, 1),
            "export_exposure_pre": rng.normal(0, 1),
        })
panel = pd.DataFrame(rows)
panel.to_csv(DATA / "demo_sector_year.csv", index=False)
print(f"Wrote {DATA / 'demo_coded_passages.csv'}")
print(f"Wrote {DATA / 'demo_sector_year.csv'}")
