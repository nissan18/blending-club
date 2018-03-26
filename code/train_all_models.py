import time

import definitions
import pandas_helper
import scikit_helper
import lendingclub_helper


def main():
    print("Begin:" + __file__)

    for key in definitions.dataFiles:
        begin = time.time()
        print("Processing: " + key)

        df = pandas_helper.readData(definitions.dataFiles[key])

        lendingclub_helper.buildFeatures(df)
        featureColumns = lendingclub_helper.getFeatureColumns(df)
        assert(not pandas_helper.columnsHaveNull(df, featureColumns.tolist()))

        lendingclub_helper.buildLabels(df)
        labelColumns = lendingclub_helper.getLabelColumns(df)
        df = lendingclub_helper.getFinishedLoans(df)
        assert(not pandas_helper.columnsHaveNull(df, labelColumns.tolist()))

        X = df[featureColumns].values
        y = df[labelColumns[0]].values
        clf = scikit_helper.trainModel(X, y)

        filename = "svc_{0}.pkl".format(key)
        scikit_helper.saveModel(clf, filename)

        end = time.time()
        print("Elapsed {0} seconds".format(end-begin))


if __name__ == "__main__":
    main()
