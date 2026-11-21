"""Label-noise helpers (Q5)."""
import numpy as np
import pandas as pd
from sklearn.base import clone

from common.evaluate import evaluate
from hw2.data import SEED


def corrupt_labels(y, fraction, mode="shuffle", seed=SEED):
    """Return a copy of y in which `fraction` of the labels are corrupted.

    mode="shuffle": the chosen labels are permuted among themselves
                    (with balanced classes about half of them stay unchanged).

    mode="flip"   : the chosen labels are inverted (exactly `fraction` are wrong).
    """
    rng = np.random.default_rng(seed)
    y_new = y.copy() # not to touch original labels
    idx = rng.choice(len(y), int(round(fraction * len(y))), replace=False)
    if mode == "shuffle":
        y_new[idx] = rng.permutation(y[idx]) # shuffle for selected labels (change locations)
    elif mode == "flip":
        y_new[idx] = 1 - y[idx] # 0-1 flip
    else:
        raise ValueError(f"unknown mode: {mode}")
    return y_new


def run_label_noise(model, Xtr, ytr, Xte, yte, fractions, mode="shuffle", n_repeats=5):
    """Train on corrupted labels, test on clean labels (one row per fraction and repeat)."""
    rows = []
    for frac in fractions:
        for rep in range(n_repeats):
            y_noisy = corrupt_labels(ytr, frac, mode, seed=SEED + rep)
            m = clone(model).fit(Xtr, y_noisy)
            rows.append({
                "fraction": frac,
                "repeat": rep,
                "wrong_labels": np.mean(y_noisy != ytr), # share that really changed (actual % of incorrect labels)
                "train_acc_noisy": m.score(Xtr, y_noisy), # fit to the noisy labels
                **evaluate(m, Xte, yte), # clean test set
            })
    return pd.DataFrame(rows)
