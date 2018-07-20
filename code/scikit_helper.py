from sklearn.base import ClassifierMixin
from sklearn.svm import SVC
from sklearn.externals import joblib

import numpy as np


def trainModel(X, y):
    assert(isinstance(X, np.ndarray))
    assert(isinstance(y, np.ndarray))
    assert(len(y.shape) == 1), y.shape
    assert(X.shape[0] == y.shape[0])

    clf = SVC()
    clf.fit(X, y)
    return clf


def getAccuracy(clf, X, y):
    # assert(isinstance(clf, ClassifierMixin))  # TODO: uncomment test when implement TODO's in lendingclub_models.py
    assert(isinstance(X, np.ndarray))
    assert(isinstance(y, np.ndarray))
    assert(len(y.shape) == 1)
    assert(X.shape[0] == y.shape[0])

    y_p = clf.predict(X)  # predicted
    assert(y.shape == y_p.shape)
    return sum(y == y_p)/len(y)


def saveModel(clf, filename):
    assert(isinstance(clf, ClassifierMixin))
    assert(isinstance(filename, str))

    joblib.dump(clf, filename)


def loadModel(filename):
    assert(isinstance(filename, str))

    return joblib.load(filename)
