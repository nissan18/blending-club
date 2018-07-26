import pandas as pd
from sklearn.dummy import DummyClassifier

import pandas_helper
import scikit_helper

import lendingclub_columns
import lendingclub_helper
from lendingclub_models import ConstantClassifier


class LendingClub_Pipeline:

    def __init__(self):
        self.featurize_columns = ["annual_inc", "sub_grade"]
        self.labelize_columns = ["loan_status"]


    def run(self, trainset_filename, testset_filename):
        df_train = pandas_helper.readData(trainset_filename, lendingclub_columns.get_dtypes_by_name())
        model = self.buildModel(df_train)
        print(model)

        print("Train accuracy: {}".format(self.getAccuracy(model, df_train)))

        df_test = pandas_helper.readData(testset_filename, lendingclub_columns.get_dtypes_by_name())
        print("Test accuracy: {}".format(self.getAccuracy(model, df_test)))

        # self.smokeTest(model)

        clf_0 = scikit_helper.get_constant_classifier(0)
        clf_1 = scikit_helper.get_constant_classifier(1)

        print("Const 0 accurary on train set: {}".format(self.getAccuracy(clf_0, df_train)))
        print("Const 1 accurary on train set: {}".format(self.getAccuracy(clf_1, df_train)))

        print("Const 0 accurary on test set: {}".format(self.getAccuracy(clf_0, df_test)))
        print("Const 1 accurary on test set: {}".format(self.getAccuracy(clf_1, df_test)))

        # clf = clf = DummyClassifier(strategy='most_frequent',random_state=0)


    def smokeTest(self, model):
        smoke_data = [
            { "annual_inc": 100000000, "sub_grade": "A1"},
            { "annual_inc": 100000, "sub_grade": "B1"},
            { "annual_inc": 100000, "sub_grade": "C1"},
            { "annual_inc": 100000, "sub_grade": "D1"},
            { "annual_inc": 100000, "sub_grade": "E1"},
            { "annual_inc": 100000, "sub_grade": "F1"},
            { "annual_inc": 100000, "sub_grade": "G1"},
            { "annual_inc": 50000, "sub_grade": "A1"},
            { "annual_inc": 50000, "sub_grade": "B1"},
            { "annual_inc": 50000, "sub_grade": "C1"},
            { "annual_inc": 50000, "sub_grade": "D1"},
            { "annual_inc": 50000, "sub_grade": "E1"},
            { "annual_inc": 50000, "sub_grade": "F1"},
            { "annual_inc": 50000, "sub_grade": "G1"},
            { "annual_inc": 10000, "sub_grade": "A1"},
            { "annual_inc": 10000, "sub_grade": "B1"},
            { "annual_inc": 10000, "sub_grade": "C1"},
            { "annual_inc": 10000, "sub_grade": "D1"},
            { "annual_inc": 10000, "sub_grade": "E1"},
            { "annual_inc": 10000, "sub_grade": "F1"},
            { "annual_inc": 46000, "sub_grade": "C4"},
        ]
        df_smoke = pd.DataFrame(smoke_data)
        feature_column_defs = lendingclub_columns.get_columns_by_names(self.featurize_columns)
        lendingclub_helper.build_features_by_columns(df_smoke, feature_column_defs)

        feature_columns = lendingclub_helper.getFeatureColumns(df_smoke)

        X = df_smoke[feature_columns].values

        for i in range(len(smoke_data)):
            print(smoke_data[i], "prediction: {}".format(model.predict(X[[i]])))


    def getAccuracy(self, model, df):
        self.buildFeaturesAndLabels(df)
        feature_columns = lendingclub_helper.getFeatureColumns(df)
        label_columns = lendingclub_helper.getLabelColumns(df)

        X = df[feature_columns].values
        y = df[label_columns[0]].values

        accuracy = scikit_helper.get_accuracy(model, X, y)
        return accuracy

    def buildModel(self, df):
        self.buildFeaturesAndLabels(df)
        feature_columns = lendingclub_helper.getFeatureColumns(df)
        label_columns = lendingclub_helper.getLabelColumns(df)

        X = df[feature_columns].values
        y = df[label_columns[0]].values

        model = scikit_helper.trainModel(X, y)
        return model

    def buildFeaturesAndLabels(self, df):
        feature_column_defs = lendingclub_columns.get_columns_by_names(self.featurize_columns)
        lendingclub_helper.build_features_by_columns(df, feature_column_defs)
        lendingclub_helper.buildCategorialLabel(df, self.labelize_columns[0], lendingclub_helper.parse_loan_status)


