"""Model factories for HW2 (one place to change hyperparameters)."""
from sklearn.linear_model import Perceptron
from sklearn.svm import LinearSVC, SVC

from hw2.data import SEED


def make_perceptron(seed=SEED):
    return Perceptron(max_iter=1000, tol=1e-3, random_state=seed)


def make_linear_svm(C=1.0, seed=SEED):
    # hinge loss = the textbook SVM objective
    return LinearSVC(C=C, loss="hinge", dual=True, max_iter=20000,
                     random_state=seed)


def make_kernel_svm(kernel="rbf", C=1.0, gamma="scale", degree=2):
    """Kernel SVM. degree is only used by the polynomial kernel."""
    return SVC(kernel=kernel, C=C, gamma=gamma, degree=degree)
