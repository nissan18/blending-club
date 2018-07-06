import time
import logging
import sys

import definitions
import pandas_helper
import scikit_helper
import lendingclub_helper as l


def main():
    print("Begin: " + __file__)

    a = l.dtypes
    b = l.columns

    for i in range(len(l.columns)):
        item = l.columns[i]
        if item["dtype"] != a[item["name"]]:
            print("item: ", item)
            print("dtype: ", a[item["name"]])
            break
    # b = { { x["name"]: x["dtype"] } for x in l.columns }

    # print(len(a.keys()))
    # print(len(b.keys()))



    print("End: " + __file__)


if __name__ == "__main__":
    main()
