# TODO: fix this
# see if there're built-in dummy models in scikit
# if not, implement this using ClassifierMixin from sklearn.base
# uncomment the test in scikit_helper

import numpy as np


class ConstantClassifier:
    def __init__(self, value):
        self.value = value

    def predict(self, X):
        assert (isinstance(X, np.ndarray)), "X must be np.ndarray"

        return np.ones(X.shape[0]) * self.value


