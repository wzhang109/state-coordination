"""Weight sensitivity for the State Support Index.

Runs leave-one-out and Dirichlet perturbation. Requires >= 3 sectors to be
informative; prints a warning and exits early below that.
"""
import numpy as np, pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
dim = pd.read_csv(ROOT / "data" / "dimension_means.csv")   # sector, dimension, index_input
DIMS = sorted(dim["dimension"].unique())
wide = dim.pivot(index="sector", columns="dimension", values="index_input")

if len(wide) < 3:
    print(f"Only {len(wide)} sectors. Sensitivity analysis is not informative yet. "
          f"Script retained for use once coverage increases.")
    raise SystemExit(0)

def index_from(weights):
    w = np.array([weights[d] for d in DIMS])
    return wide[DIMS].values @ w

# 1) leave-one-out
print("\n=== Leave-one-dimension-out ===")
for drop in DIMS:
    keep = [d for d in DIMS if d != drop]
    w = {d: 1/len(keep) for d in keep} | {drop: 0.0}
    s = pd.Series(index_from(w), index=wide.index).sort_values(ascending=False)
    print(f"drop {drop:16s} -> ranking: {list(s.index)}")

# 2) Dirichlet perturbation
print("\n=== Dirichlet(1,1,1,1) perturbation, 1000 draws ===")
rng = np.random.default_rng(20260802)
base = pd.Series(index_from({d: 0.25 for d in DIMS}), index=wide.index)
base_top = base.idxmax()
hits = 0
for _ in range(1000):
    w = dict(zip(DIMS, rng.dirichlet(np.ones(len(DIMS)))))
    if pd.Series(index_from(w), index=wide.index).idxmax() == base_top:
        hits += 1
print(f"top-ranked sector under equal weights: {base_top}")
print(f"share of draws preserving that ranking: {hits/1000:.1%}")
