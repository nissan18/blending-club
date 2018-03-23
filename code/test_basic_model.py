import pandas
import numpy as np

import columns
import definitions
import pandas_helper
import scikit_helper
import lendingclub_helper

def main():
    key = "2007-2011"
    modelFile = "../models/svc{0}.pkl".format(key)
    clf = scikit_helper.loadModel(modelFile)

    files = [
        '../data/LoanStats3a_securev1.csv',
        # '../data/LoanStats3b_securev1.csv',
        # '../data/LoanStats3c_securev1.csv',
        # '../data/LoanStats3d_securev1.csv'
        # '../data/LoanStats_securev1_2016Q1.csv',
        # '../data/LoanStats_securev1_2016Q2.csv',
        # '../data/LoanStats_securev1_2016Q3.csv',
        # '../data/LoanStats_securev1_2016Q4.csv',
        '../data/LoanStats_securev1_2017Q1.csv',
        '../data/LoanStats_securev1_2017Q2.csv',
        '../data/LoanStats_securev1_2017Q3.csv',
        '../data/LoanStats_securev1_2017Q4.csv'
    ]

    features = None
    for filename in files:
        print(filename)

        df = pandas.read_csv(filename, dtype=columns.dtypes)
        print("raw shape: {0}".format(df.shape))

        df = lendingclub_helper.getFinishedLoans(df)
        print("finished shape: {0}".format( df.shape))

        if not features:
            features = pandas_helper.getFeatures(df)
        X, y = lendingclub_helper.extractData(df, features)
        print("Accuracy = {0}".format(scikit_helper.getAccuracy(clf, X, y)))


if __name__ == "__main__":
    main()
