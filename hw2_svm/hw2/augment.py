"""Gaussian-noise augmentation and its evaluation (Q4)."""
import numpy as np
import pandas as pd

from common.evaluate import evaluate
from common.plots import plot_decision_boundary
from hw2.data import SEED


def add_gaussian_noise(X, sigma, rng):
    """Move every point in a random direction: X + N(0, sigma^2) per coordinate."""
    return X + rng.normal(0.0, sigma, size=X.shape)


def augment_rounds(X, y, sigma, k, n_sample=1000, cumulative=False, seed=SEED):
    """Yield k augmented datasets (round, X_aug, y_aug) of n_sample points each.

    cumulative=False: every round starts from a fresh sample of the original data.
    cumulative=True : round t continues from round t-1, so the points keep
                      drifting like a random walk.
    """
    rng = np.random.default_rng(seed)
    idx = rng.choice(len(X), n_sample, replace=False)
    X_cur, y_cur = X[idx], y[idx]
    for t in range(1, k + 1):
        if not cumulative and t > 1:
            idx = rng.choice(len(X), n_sample, replace=False)
            X_cur, y_cur = X[idx], y[idx]
        X_cur = add_gaussian_noise(X_cur, sigma, rng)
        yield t, X_cur, y_cur # To avoid filing up 2000 sets at once, but per a round


def run_augmentation(model, X, y, sigma, k, cumulative=False, n_sample=1000, seed=SEED):
    """Evaluate a fitted model on k augmented datasets (one row of metrics per round)."""
    rows = [{"round": t, **evaluate(model, Xa, ya)}
            for t, Xa, ya in augment_rounds(X, y, sigma, k, n_sample, cumulative, seed)]
    return pd.DataFrame(rows)


def first_round_below(results, threshold=0.70, metric="accuracy"):
    """First round where the metric drops below the threshold (None if it never does)."""
    below = results.loc[results[metric] < threshold, "round"]
    return int(below.iloc[0]) if len(below) else None


def plot_augmented(ax, model, X_aug, y_aug, title=""):
    """Scatter of an augmented dataset; misclassified points get a black cross."""
    plot_decision_boundary(ax, model, X_aug, y_aug, title)
    wrong = model.predict(X_aug) != y_aug # x mark for incorrect dots through boolean masking
    ax.scatter(X_aug[wrong, 0], X_aug[wrong, 1], marker="x", s=25,
               color="k", linewidths=0.8, label="Misclassified")
    ax.legend(markerscale=2, loc="upper right")
