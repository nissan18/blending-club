import time
import logging
import sys

import pandas_helper
import scikit_helper
import lendingclub_helper
import lendingclub_columns
import lendingclub_validation
import pprint as pp

from lendingclub_pipeline import LendingClub_Pipeline


def main():
    print("Begin: " + __file__)

    """
    1. take only numeric columns
    2. build model to predict if loan will default
    3. train/test/validate
    4. in the future, add other types of columns
    """

    trainfile = "finished_train_sample.csv"
    testfile = "finished_test_sample.csv"
    "sample.csv"


    pipeline = LendingClub_Pipeline()
    pipeline.run(trainfile, testfile)

    print("End: " + __file__)


if __name__ == "__main__":
    main()
