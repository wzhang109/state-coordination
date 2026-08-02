"""Agreement between two independent score sets on the same passages."""
import pandas as pd
from sklearn.metrics import cohen_kappa_score

df = pd.read_csv("data/reliability_pairs.csv")   # row_id, score_a, score_b
a, b = df["score_a"], df["score_b"]

exact = (a == b).mean()
within1 = (abs(a - b) <= 1).mean()
kappa_lin = cohen_kappa_score(a, b, weights="linear")
kappa_quad = cohen_kappa_score(a, b, weights="quadratic")

print(f"n pairs:               {len(df)}")
print(f"exact agreement:       {exact:.1%}")
print(f"within-1 agreement:    {within1:.1%}")
print(f"Cohen's kappa (linear):    {kappa_lin:.3f}")
print(f"Cohen's kappa (quadratic): {kappa_quad:.3f}")
print("\nDisagreements:")
print(df[a != b].to_string(index=False))
