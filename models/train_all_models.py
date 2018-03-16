import pandas
import numpy as np
from sklearn.svm import SVC
from sklearn.externals import joblib

import columns
import helpers



def main():
    dataFiles = [
        '../data/LoanStats3a_securev1.csv',
        '../data/LoanStats3b_securev1.csv',
        '../data/LoanStats3c_securev1.csv',
        '../data/LoanStats3d_securev1.csv',
        '../data/LoanStats_securev1_2016Q1.csv',
        '../data/LoanStats_securev1_2016Q2.csv',
        '../data/LoanStats_securev1_2016Q3.csv',
        '../data/LoanStats_securev1_2016Q4.csv',
        '../data/LoanStats_securev1_2017Q1.csv',
        '../data/LoanStats_securev1_2017Q2.csv',
        '../data/LoanStats_securev1_2017Q3.csv',
        '../data/LoanStats_securev1_2017Q4.csv'
    ]

    modelFiles = [
        'svc3a.pkl',
        'svc3b.pkl',
        'svc3c.pkl',
        'svc3d.pkl',
        'svc2016Q1.pkl',
        'svc2016Q2.pkl',
        'svc2016Q3.pkl',
        'svc2016Q4.pkl',
        'svc2017Q1.pkl',
        'svc2017Q2.pkl',
        'svc2017Q3.pkl',
        'svc2017Q4.pkl'
    ]

    for i in range(8):
        df = pandas.read_csv(dataFiles[i], dtype=columns.dtypes)

        features = getFeatures(df)

        X, y = extractData(df, features)

        clf = trainModel(X, y)
        # print(clf)
        # print("Accuracy = {0}".format(getAccuracy(clf, X, y)))

        saveModel(clf, modelFiles[i])

        # clf2 = loadModel(filename)
        # print(clf2)
        # print("Accuracy = {0}".format(getAccuracy(clf2, X, y)))


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
