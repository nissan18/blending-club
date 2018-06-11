import pandas
import numpy as np

import definitions
import pandas_helper
import scikit_helper
import lendingclub_helper



def main():

    #  Pick one
    key = "2007-2011"
    # key = "2012-2013"
    # key = "2014"
    # key = "2015"
    # key = "2016Q1"
    # key = "2016Q2"
    # key = "2016Q3"
    # key = "2016Q4"
    # key = "2017Q1"
    # key = "2017Q2"
    # key = "2017Q3"
    # key = "2017Q4"

    print("Generate model for " + key)
    print("Reading data...")
    dataFile = definitions.dataFiles[key]
    dataFrame = pandas_helper.readData(dataFile, lendingclub_helper.dtypes)

    print("Building features...")
    lendingclub_helper.buildFeatures(dataFrame)
    lendingclub_helper.buildLabels(dataFrame)

    featureColumns = lendingclub_helper.getFeatureColumns(dataFrame)
    labelColumns = lendingclub_helper.getLabelColumns(dataFrame)

    print("Training model...")
    X = dataFrame[featureColumns].values
    y = dataFrame[labelColumns[0]].values

    model = scikit_helper.trainModel(X, y)

    print("Saving model...")
    modelFile = "model_{0}.pkl".format(key)
    scikit_helper.saveModel(model, modelFile)

    print("Done")


if __name__ == "__main__":
    main()
