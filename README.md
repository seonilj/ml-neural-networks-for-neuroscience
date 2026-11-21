# Machine Learning & Neural Networks for Neuroscience

Coursework for the *Machine Learning & Neural Networks for Neuroscience* course
at Bar-Ilan University (Erasmus Mundus NeuroData MSc).
Each homework lives in its own folder, shared helpers are in `common/`,
and a short Git/GitHub reference is kept in `docs/`.

## Assignments

| HW | Topic | Methods | Status |
|----|-------|---------|--------|
| [HW1](hw1_neural_tuning/) | Neural tuning analysis | data loading and inspection (`h5py`, `scipy.io.loadmat`), tuning curve fitting (`scipy.optimize.curve_fit`), model comparison, generalization analysis | Done |
| [HW2](hw2_svm/) | SVM and perceptron on simulated data | perceptron vs. linear SVM, RBF/polynomial kernels, noise augmentation, label noise, high dimensions | In progress |
| [HW3](hw3_cifar10/) | CIFAR-10: CNN vs MLP | overfitting, augmentation | Not started |

## Repository structure

```
ml-neural-networks-for-neuroscience/
├── README.md
├── requirements.txt
├── docs/                      Git & GitHub workflow notes
│   ├── README.md
│   └── git_workflow/
│       └── troubleshooting.md
├── common/                    shared helpers (evaluation metrics, plotting)
│   ├── evaluate.py
│   ├── plots.py
│   └── eval_plots.py
├── hw1_neural_tuning/
│   └── analysis.ipynb
├── hw2_svm/                   notebook, hw2 modules, figures, report
│   ├── hw2_main.ipynb
│   ├── hw2/
│   └── figs/
└── hw3_cifar10/               (coming soon)
```

## Docs

[`docs/`](docs/) is a practical reference for managing project repositories,
tracking changes, and keeping a clean development workflow.
It includes a [troubleshooting log](docs/git_workflow/troubleshooting.md)
of Git/GitHub issues, errors, and the solutions that fixed them.

## How to run

```bash
git clone https://github.com/seonilj/ml-neural-networks-for-neuroscience.git
cd ml-neural-networks-for-neuroscience
pip install -r requirements.txt
```

Then open the notebook inside a homework folder
(e.g. `hw1_neural_tuning/analysis.ipynb` or `hw2_svm/hw2_main.ipynb`).
All notebooks were developed in Google Colab.

## Notes

- Random seeds are fixed in each homework for reproducibility.
- `hw2_main.ipynb` was run in Colab with this repository folder stored in Google Drive;
  the project path is set by `ROOT` in the first cells and must be changed to run it elsewhere.
- Reports are in each homework folder under `report/` (where required).