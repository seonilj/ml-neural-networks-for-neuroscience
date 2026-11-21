"""Evaluation figures: confusion matrix and ROC curve."""
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay


def plot_confusion(ax, model, X, y, title=""):
    """Confusion matrix (counts) of a fitted classifier on (X, y)."""
    ConfusionMatrixDisplay.from_estimator(model, X, y, ax=ax,
                                          cmap="Blues", colorbar=False)
    ax.set_title(title)


def plot_roc(ax, models, X, y):
    """ROC curves of several fitted models on one axis. models = {name: model}"""
    for name, model in models.items():
        RocCurveDisplay.from_estimator(model, X, y, ax=ax, name=name)
    ax.plot([0, 1], [0, 1], "k--", lw=1, label="Chance")
    ax.set_title("ROC curves")
    ax.legend(loc="lower right")
