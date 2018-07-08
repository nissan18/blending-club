import time
import logging
import sys

import definitions
import pandas_helper
import scikit_helper
import lendingclub_helper as l


def main():
    print("Begin: " + __file__)

    b = [c for c in l.columns if c["feature"] == "one-hot encoding"]
    print("len = ", len(b))
    print(b)

    print("End: " + __file__)


if __name__ == "__main__":
    main()
