import pandas
import numpy as np
from sklearn.svm import SVC
from sklearn.externals import joblib

from columns import columns
import helpers



def main():
    # load data
    df3a = pandas.read_csv("../data/LoanStats3a_securev1.csv")

    features = getFeatures(df3a)

    X, y = extractData(df3a, features)

    clf = trainModel(X, y)

    print(clf)

    print("Accuracy = {0}".format(getAccuracy(clf, X, y)))

    filename = "df3a_svc.pkl"
    saveModel(clf, filename)

    clf2 = loadModel(filename)
    print(clf2)

    print("Accuracy = {0}".format(getAccuracy(clf2, X, y)))

    # # check on next dataset
    # df3b = pandas.read_csv("../data/LoanStats3b_securev1.csv")


def getFeatures(df):
    numeric_columns = helpers.getNumericColumns(df)
    nonnullable_columns = helpers.getNonNullableColumns(df)
    numeric_nonnullable_columns = list(set(numeric_columns) & set(nonnullable_columns))
    return numeric_nonnullable_columns
    

def extractData(df, features):
    return df[features].values, df["loan_status"].apply(convertLoanStatus).values


def trainModel(X, y):
    clf = SVC()
    clf.fit(X, y)
    return clf


def saveModel(clf, filename):
    joblib.dump(clf, filename)


def loadModel(filename):
    return joblib.load(filename)


def getAccuracy(clf, X, y):
    y_p = clf.predict(X)  # predicted
    assert(y.shape == y_p.shape)
    return sum(y == y_p)/len(y)



def convertLoanStatus(status):
    convert = {
        'Fully Paid': 1,
        'Charged Off': 0,
        'Does not meet the credit policy. Status:Fully Paid': 1,
        'Does not meet the credit policy. Status:Charged Off': 0,
    }
    assert(status in convert)
    return convert[status]


if __name__ == "__main__":
    main()
