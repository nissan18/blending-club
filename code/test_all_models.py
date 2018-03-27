import time
import logging
import sys

import definitions
import pandas_helper
import scikit_helper
import lendingclub_helper


def main():
    print("Begin: " + __file__)

    setupLogging()
    logger = logging.getLogger()

    for key1 in definitions.dataFiles:
        begin = time.time()

        filename = "../models/svc_{0}.pkl".format(key1)
        clf = scikit_helper.loadModel(filename)

        for key2 in definitions.dataFiles:
            begin = time.time()

            df = pandas_helper.readData(definitions.dataFiles[key2])

            lendingclub_helper.buildFeatures(df)
            featureColumns = lendingclub_helper.getFeatureColumns(df)
            assert(not pandas_helper.columnsHaveNull(df, featureColumns.tolist()))

            lendingclub_helper.buildLabels(df)
            labelColumns = lendingclub_helper.getLabelColumns(df)

            df = lendingclub_helper.getFinishedLoans(df)
            assert(not pandas_helper.columnsHaveNull(df, labelColumns.tolist()))

            X = df[featureColumns].values
            y = df[labelColumns[0]].values
            
            accuracy = scikit_helper.getAccuracy(clf, X, y)

            logger.info("model: {0}, data: {1}, accurary: {2}".format(key1, key2, accuracy))

            end = time.time()
            logger.info("Elapsed {0} seconds".format(end-begin))

    print("End: " + __file__)


def setupLogging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("output.txt")
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    
    sh = logging.StreamHandler(sys.stderr)
    sh.setLevel(logging.DEBUG)
    logger.addHandler(sh)


if __name__ == "__main__":
    main()
