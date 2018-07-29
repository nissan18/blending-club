import time
import logging
import sys

import definitions
import pandas_helper
import scikit_helper
import lendingclub_helper
import lendingclub_columns
import lendingclub_validation
import pprint as pp

from lendingclub_pipeline import LendingClub_Pipeline


def main():
    print("Begin: " + __file__)


    print([c for c in lendingclub_columns.columns if c["name"] == "sub_grade"])

    # feature_columns = lendingclub_columns.get_feature_column_name("desc")
    # print(feature_columns)


    return
    # filename = "sample.csv"
    # filename = "finished_test_sample.csv"
    filename = "finished_train_sample.csv"

    featurize_columns = ["annual_inc", "sub_grade"]
    labelize_columns = ["loan_status"]


    df = pandas_helper.readData(filename, lendingclub_columns.get_dtypes_by_name())

    feature_column_defs = lendingclub_columns.get_columns_by_names(featurize_columns)
    lendingclub_helper.build_features_by_columns(df, feature_column_defs)
    lendingclub_helper.buildCategorialLabel(df, labelize_columns[0], lendingclub_helper.parse_loan_status)

    feature_columns = lendingclub_helper.getFeatureColumns(df)
    label_columns = lendingclub_helper.getLabelColumns(df)

    X = df[feature_columns].values
    y = df[label_columns[0]].values

    model = scikit_helper.trainModel(X, y)
    print(model)
    print("score: {}".format(model.score(X, y)))

    clf = scikit_helper.get_constant_classifier(0)
    print((clf))
    print("score: {}".format(clf.score(X, y)))

    clf = scikit_helper.get_constant_classifier(1)
    print((clf))
    print("score: {}".format(clf.score(X, y)))







    print("End: " + __file__)


if __name__ == "__main__":
    main()
