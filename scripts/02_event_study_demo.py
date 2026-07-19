"""Run a simple event-study demo on synthetic data.

This script estimates interactions between event-time indicators and the
pre-transition State Support Index, with sector and year fixed effects. It uses
synthetic data for workflow demonstration only.
"""
from pathlib import Path
import re
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

panel = pd.read_csv(DATA / "demo_sector_year.csv")
index = pd.read_csv(DATA / "demo_support_index.csv")
df = panel.merge(index[["sector", "state_support_index"]], on="sector", how="left")

# Restrict event window and omit k = -1 as reference period.
event_window = list(range(-6, 9))
reference = -1
for k in event_window:
    if k == reference:
        continue
    name = f"event_{'m' + str(abs(k)) if k < 0 else 'p' + str(k)}"
    df[name] = (df["event_time"] == k).astype(int)
    df[f"{name}_x_support"] = df[name] * df["state_support_index"]

interaction_terms = [c for c in df.columns if c.endswith("_x_support")]
formula = "entry_rate ~ " + " + ".join(interaction_terms) + " + C(sector) + C(year)"
model = smf.ols(formula, data=df).fit(cov_type="cluster", cov_kwds={"groups": df["sector"]})

rows = []
for term in interaction_terms:
    match = re.search(r"event_(m\d+|p\d+)_x_support", term)
    label = match.group(1)
    k = -int(label[1:]) if label.startswith("m") else int(label[1:])
    rows.append({
        "event_time": k,
        "estimate": model.params.get(term, np.nan),
        "std_error": model.bse.get(term, np.nan),
    })
coef = pd.DataFrame(rows).sort_values("event_time")
coef["ci_low"] = coef["estimate"] - 1.96 * coef["std_error"]
coef["ci_high"] = coef["estimate"] + 1.96 * coef["std_error"]
coef.to_csv(OUT / "event_study_coefficients.csv", index=False)

plt.figure(figsize=(7, 4.5))
plt.axhline(0, linewidth=1)
plt.axvline(0, linestyle="--", linewidth=1)
plt.errorbar(
    coef["event_time"],
    coef["estimate"],
    yerr=1.96 * coef["std_error"],
    fmt="o-",
    capsize=3,
)
plt.xlabel("Event time relative to 1987")
plt.ylabel("Interaction with State Support Index")
plt.title("Synthetic event-study demo")
plt.tight_layout()
plt.savefig(OUT / "event_study_plot.png", dpi=200)

print(model.summary().tables[1])
print(f"Wrote {OUT / 'event_study_coefficients.csv'}")
print(f"Wrote {OUT / 'event_study_plot.png'}")
