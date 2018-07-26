from sklearn.base import ClassifierMixin
from sklearn.dummy import DummyClassifier
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


def get_accuracy(clf, X, y):
    assert(isinstance(clf, ClassifierMixin))
    assert (isinstance(X, np.ndarray)), "X must be np.ndarray"
    assert (isinstance(y, np.ndarray)), "y must be np.ndarray"
    assert (len(y.shape) == 1), "y.shape: {}".format(y.shape)
    assert (X.shape[0] == y.shape[0]), "X.shape: {}, y.shape: {}".format(X.shape, y.shape)

    return clf.score(X, y)


def saveModel(clf, filename):
    assert(isinstance(clf, ClassifierMixin))
    assert(isinstance(filename, str))

    joblib.dump(clf, filename)


def loadModel(filename):
    assert(isinstance(filename, str))

    return joblib.load(filename)


def get_constant_classifier(constant):
    assert (isinstance(constant, int) or isinstance(constant, float)), "constant must be a number: {}".format(constant)

    clf = DummyClassifier(strategy='constant', constant=constant)
    clf.fit([[0]], [constant])
    return clf
