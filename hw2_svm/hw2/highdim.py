"""High-dimensional versions of the HW2 datasets (Q6)."""
import numpy as np

from hw2.data import SEED, make_linear_data


def make_linear_highdim(d, n=10_000, seed=SEED):
    """Two Gaussian clusters in d dimensions. The distance between the centers is
    kept at its 2D value (about 8.5), so only the dimension changes."""
    spread = 3.0 * np.sqrt(2 / d) # centers at +-spread on every axis
    return make_linear_data(n=n, n_features=d, spread=spread, seed=seed)


def make_circular_highdim(d, n=10_000, radii=(1.0, 0.5), noise=0.08, seed=SEED):
    """Two concentric hyperspheres in d dimensions (class 0 outside, class 1 inside)."""
    rng = np.random.default_rng(seed)
    y = rng.permutation(np.repeat([0, 1], n // 2))
    # a normalized Gaussian vector is a uniformly random direction
    directions = rng.normal(size=(n, d))
    directions /= np.linalg.norm(directions, axis=1, keepdims=True)
    radius = np.where(y == 0, radii[0], radii[1]) + rng.normal(0, noise, n)
    return directions * radius[:, None], y
