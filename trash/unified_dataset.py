import time
import pandas as pd

import definitions
import pandas_helper
import lendingclub_helper

def main():
    df = pd.DataFrame()

    dataFrames = []

    for key in definitions.dataFiles:
        filename = definitions.dataFiles[key]
        print("Reading " + filename)
        dataFrames.append(pandas_helper.readData(filename, lendingclub_helper.dtypes))

    print("Combining dataFrames")
    df = pd.concat(dataFrames)
    print("Shape: {0}".format(df.shape))


    # df.to_pickle("everything.pickle")  # can't do large dataFrames

    df.to_hdf("everything.hdf", "everything")



if __name__ == "__main__":
    main()
