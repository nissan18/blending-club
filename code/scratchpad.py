import time
import logging
import sys

import definitions
import pandas_helper
import scikit_helper
import lendingclub_helper


def main():
    print("Begin: " + __file__)
    
    df = pandas_helper.readData("sample.csv")
    lendingclub_helper.buildFeatures(df)

    print("End: " + __file__)


if __name__ == "__main__":
    main()
