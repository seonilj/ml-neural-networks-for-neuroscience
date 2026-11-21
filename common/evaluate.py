"""Shared evaluation helpers."""
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score


def evaluate(model, X, y):
    """Main metrics of a fitted binary classifier, returned as a dict."""
    pred = model.predict(X)
    return {
        "accuracy": accuracy_score(y, pred),
        "f1": f1_score(y, pred),
        # AUC needs a continuous score, not the 0/1 prediction
        "auc": roc_auc_score(y, model.decision_function(X)),
    }


def compare_models(models, X, y):
    """models = {name: fitted model}  ->  one row of metrics per model."""
    table = {name: evaluate(m, X, y) for name, m in models.items()}
    return pd.DataFrame(table).T.round(3)


def margin_width(model, X):
    """Width of the empty band around a linear boundary (2 x closest distance)."""
    dist = np.abs(model.decision_function(X)) / np.linalg.norm(model.coef_[0])
    return 2 * dist.min()
