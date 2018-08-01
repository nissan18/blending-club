import time
import logging
import sys

import pandas_helper
import scikit_helper
import lendingclub_features
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


    df = pandas_helper.read_data(filename, lendingclub_columns.get_dtypes_by_name())

    feature_column_defs = lendingclub_columns.get_columns_by_names(featurize_columns)
    lendingclub_features.build_features_by_columns(df, feature_column_defs)
    lendingclub_features.build_categorical_label(df, labelize_columns[0], lendingclub_features.parse_loan_status)

    feature_columns = lendingclub_features.getFeatureColumns(df)
    label_columns = lendingclub_features.get_label_columns(df)

    X = df[feature_columns].values
    y = df[label_columns[0]].values

    model = scikit_helper.train_model(X, y)
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
