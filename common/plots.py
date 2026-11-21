"""Shared plot helpers."""
import numpy as np
import matplotlib.pyplot as plt

COLORS = {0: "tab:blue", 1: "tab:red"}


def plot_scatter(ax, X, y, title=""):
    """Scatter plot of a 2D dataset, colored by class."""
    for label, color in COLORS.items():
        pts = X[y == label]
        ax.scatter(pts[:, 0], pts[:, 1], s=4, alpha=0.5,
                   color=color, label=f"Class {label}")
    ax.set_title(title)
    ax.set_xlabel("X1")
    ax.set_ylabel("X2")
    ax.set_aspect("equal")
    ax.legend(markerscale=3)


def plot_datasets(datasets, save_path=None):
    """Plot several datasets side by side. datasets = {title: (X, y)}"""
    fig, axes = plt.subplots(1, len(datasets), figsize=(6 * len(datasets), 5))
    for ax, (title, (X, y)) in zip(axes, datasets.items()):
        plot_scatter(ax, X, y, title)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.show()


def plot_decision_boundary(ax, model, X, y, title="", show_margin=False):
    """Shade the predicted regions, draw the boundary (and margin), then the data."""
    pad = 0.5
    xx, yy = np.meshgrid(
        np.linspace(X[:, 0].min() - pad, X[:, 0].max() + pad, 300),
        np.linspace(X[:, 1].min() - pad, X[:, 1].max() + pad, 300),
    )
    scores = model.decision_function(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    # background: blue where the model predicts class 0, red where class 1
    ax.contourf(xx, yy, scores, levels=[-1e9, 0, 1e9],
                colors=[COLORS[0], COLORS[1]], alpha=0.12)
    ax.contour(xx, yy, scores, levels=[0], colors="k", linewidths=2)
    if show_margin:  # only meaningful for SVM: score = -1 and +1
        ax.contour(xx, yy, scores, levels=[-1, 1], colors="k",
                   linestyles="--", linewidths=1)
    plot_scatter(ax, X, y, title)


def draw_line(ax, model, x_range, **kwargs):
    """Draw a linear model's boundary w1*x1 + w2*x2 + b = 0 as a line."""
    (w1, w2), b = model.coef_[0], model.intercept_[0]
    xs = np.array(x_range)
    ax.plot(xs, -(w1 * xs + b) / w2, **kwargs)
