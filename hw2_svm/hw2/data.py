"""Dataset generators for HW2."""
import numpy as np
from sklearn.datasets import make_blobs, make_circles
from sklearn.model_selection import train_test_split

SEED = 42


def make_linear_data(n=10_000, n_features=2, spread=3.0, std=0.9, seed=SEED):
    """Two well-separated Gaussian clusters (linearly separable)."""
    centers = np.array([[-spread] * n_features, [spread] * n_features])
    X, y = make_blobs(n_samples=n, centers=centers, cluster_std=std,
                      random_state=seed)
    return X, y


def make_circular_data(n=10_000, factor=0.5, noise=0.08, seed=SEED):
    """Inner circle (class 1) surrounded by an outer ring (class 0)."""
    X, y = make_circles(n_samples=n, factor=factor, noise=noise,
                        random_state=seed)
    return X, y


def split_data(X, y, test_size=0.3, seed=SEED):
    """Train/test split that keeps the class balance."""
    return train_test_split(X, y, test_size=test_size,
                            stratify=y, random_state=seed) # sequence: X_train, X_test, y_train, y_test
