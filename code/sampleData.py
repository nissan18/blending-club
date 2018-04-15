import time
import logging
import sys

import definitions
import pandas_helper
import scikit_helper
import lendingclub_helper

import pandas as pd


def main():
    print("Begin: " + __file__)

    filename = "../data/everything.csv"
    df = pandas_helper.readData(filename)
    df.sample(1000).to_csv("sample.csv", index=False)

    print("End: " + __file__)


if __name__ == "__main__":
    main()
