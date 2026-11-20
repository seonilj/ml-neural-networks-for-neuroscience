# Machine Learning & Neural Networks for Neuroscience

Coursework for the *Machine Learning & Neural Networks for Neuroscience* course
at Bar-Ilan University (Erasmus Mundus NeuroData MSc).
Each homework lives in its own folder; shared helpers are in `common/`.

## Assignments

| HW | Topic | Methods | Status |
|----|-------|---------|--------|
| [HW2](hw2_svm/) | SVM and perceptron on simulated data | linear/kernel SVM, augmentation, label noise, high dimensions | In progress |
| [HW3](hw3_cifar10/) | CIFAR-10: CNN vs MLP | overfitting, augmentation | Not started |

## Repository structure

```
common/      shared helpers (evaluation metrics, plotting)
hw2_svm/     notebook, hw2 modules, figures, report
hw3_cifar10/ ...
```

## How to run

```bash
git clone https://github.com/seonilj/ml-nn-neuroscience.git
cd ml-nn-neuroscience
pip install -r requirements.txt
```

Then open the notebook inside a homework folder
(e.g. `hw1_neural_tuning/analysis.ipynb`). All notebooks were developed in Google Colab.

## Notes

- Random seeds are fixed in each homework for reproducibility.
- Reports are in each folder under `report/`.