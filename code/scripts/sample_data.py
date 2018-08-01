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

    # filename = "../data/all_loans.csv"
    filename = "../data/finished_loans.csv"
    df = pandas_helper.read_data(filename, lendingclub_helper.dtypes)
    df.sample(1000).to_csv("sample.csv", index=False)

    print("End: " + __file__)


if __name__ == "__main__":
    main()
