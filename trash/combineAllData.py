import time
import logging
import sys

import definitions
import pandas_helper
import scikit_helper
import lendingclub_helper
import lendingclub_columns

import pandas as pd


def main():
    print("Begin: " + __file__)

    dataFrames = []
    for key in definitions.dataFiles:
        print("Loading data for " + key)
        dataFrames.append(pandas_helper.readData(definitions.dataFiles[key], lendingclub_columns.get_dtypes_by_name))

    for df in dataFrames:
        print(df.shape)

    DF = pd.concat(dataFrames)
    print(DF.shape)

    DF.to_csv("combined.csv", index=False)

    print("End: " + __file__)


if __name__ == "__main__":
    main()
