"""Construct a synthetic State Support Index from coded passage scores."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

DIMENSION_WEIGHTS = {
    "persistence": 0.25,
    "specificity": 0.25,
    "network_breadth": 0.25,
    "allocation": 0.25,
}

passages = pd.read_csv(DATA / "demo_coded_passages.csv")

# Average each sector's pre-transition scores by dimension.
dim_scores = (
    passages.groupby(["sector", "dimension"], as_index=False)["score"]
    .mean()
    .rename(columns={"score": "mean_score"})
)

# Standardize each dimension across sectors -- but only when there are enough
# sectors for standardization to mean anything. With n=2, the population SD
# is |a-b|/2, so z reduces to sign(a-b): the index degenerates into a vote
# over which sector scored higher, discarding all magnitude information,
# regardless of how close or far apart the two scores actually are.
N_SECTORS = dim_scores["sector"].nunique()
STANDARDIZE_MIN_SECTORS = 8

if N_SECTORS >= STANDARDIZE_MIN_SECTORS:
    dim_scores["std_score"] = dim_scores.groupby("dimension")["mean_score"].transform(
        lambda x: (x - x.mean()) / x.std(ddof=0)
    )
    scale_note = "z-standardized within dimension"
else:
    # Raw scores already share a common 0-2 scale, so no rescaling is needed.
    # With few sectors, z-scores collapse toward +/-1 and discard magnitude.
    dim_scores["std_score"] = dim_scores["mean_score"]
    scale_note = (
        f"raw 0-2 dimension means (standardization skipped: {N_SECTORS} sectors < "
        f"{STANDARDIZE_MIN_SECTORS})"
    )

print(f"[index scale] {scale_note}")

dim_scores["weight"] = dim_scores["dimension"].map(DIMENSION_WEIGHTS)
dim_scores["weighted_score"] = dim_scores["std_score"] * dim_scores["weight"]

index = (
    dim_scores.groupby("sector", as_index=False)["weighted_score"]
    .sum()
    .rename(columns={"weighted_score": "state_support_index"})
)

# Keep dimension-specific outputs for transparent inspection.
wide_dims = dim_scores.pivot(index="sector", columns="dimension", values="std_score").reset_index()
out = index.merge(wide_dims, on="sector", how="left")
out.to_csv(DATA / "demo_support_index.csv", index=False)
print(out)
print(f"Wrote {DATA / 'demo_support_index.csv'}")
