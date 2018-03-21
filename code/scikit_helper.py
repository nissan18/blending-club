from sklearn.base import ClassifierMixin
from sklearn.svm import SVC
from sklearn.externals import joblib


def getAccuracy(clf, X, y):
    assert(clf is ClassifierMixin)
    assert(X is np.array)
    assert(y is np.array)


    y_p = clf.predict(X)  # predicted
    assert(y.shape == y_p.shape)
    return sum(y == y_p)/len(y)


def trainModel(X, y):
    assert(X is np.array)
    assert(y is np.array)

    clf = SVC()
    clf.fit(X, y)
    return clf


def saveModel(clf, filename):
    assert(clf is ClassifierMixin)
    assert(filename is str)

    joblib.dump(clf, filename)


def loadModel(filename):
    assert(filename is str)

    return joblib.load(filename)

