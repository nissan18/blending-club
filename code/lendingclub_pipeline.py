import pandas as pd
from sklearn.dummy import DummyClassifier

import pandas_helper
import scikit_helper

import lendingclub_columns
import lendingclub_features


class LendingClub_Pipeline:

    def __init__(self):
        # self.featurize_columns = ["sub_grade"]    
        self.featurize_columns = ["annual_inc", "sub_grade"]
        # self.featurize_columns = ["annual_inc", "annual_inc_joint", "application_type", "avg_cur_bal"]
        # all_numeric_and_one_hot_encoding_columns = lendingclub_columns.get_columns_by_feature_types(["numeric", "one-hot encoding"])
        # self.featurize_columns = [c["name"] for c in all_numeric_and_one_hot_encoding_columns]
        # self.featurize_columns = ["emp_length"]
        self.labelize_columns = ["loan_status"]

        # stage data


    def run(self, trainset_filename, testset_filename):
        # stage data
        self.feature_column_defs = lendingclub_columns.get_columns_by_names(self.featurize_columns)
        self.feature_columns = lendingclub_columns.get_feature_names_by_columns(self.featurize_columns)
        self.label_columns = ["l_" + col for col in self.labelize_columns]

        df_train = pandas_helper.read_data(trainset_filename, lendingclub_columns.get_dtypes_by_name())
        model = self.buildModel(df_train)
        print(model)

        print("Train accuracy: {}".format(self.getAccuracy(model, df_train)))
        df_test = pandas_helper.read_data(testset_filename, lendingclub_columns.get_dtypes_by_name())
        print("Test accuracy: {}".format(self.getAccuracy(model, df_test)))

        # self.smokeTest(model)

        clf_0 = scikit_helper.get_constant_classifier(0)
        clf_1 = scikit_helper.get_constant_classifier(1)

        print("Const 0 accurary on train set: {}".format(self.getAccuracy(clf_0, df_train)))
        print("Const 1 accurary on train set: {}".format(self.getAccuracy(clf_1, df_train)))

        print("Const 0 accurary on test set: {}".format(self.getAccuracy(clf_0, df_test)))
        print("Const 1 accurary on test set: {}".format(self.getAccuracy(clf_1, df_test)))

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
        lendingclub_features.build_features_by_columns(df_smoke, self.feature_column_defs)

        X = df_smoke[self.feature_columns].values

        for i in range(len(smoke_data)):
            print(smoke_data[i], "prediction: {}".format(model.predict(X[[i]])))


    def getAccuracy(self, model, df):
        self.buildFeaturesAndLabels(df)

        X = df[self.feature_columns].values
        y = df[self.label_columns[0]].values

        accuracy = scikit_helper.get_accuracy(model, X, y)
        return accuracy

    def buildModel(self, df):
        self.buildFeaturesAndLabels(df)

        X = df[self.feature_columns].values
        y = df[self.label_columns[0]].values

        Model = scikit_helper.models[0]
        clf = scikit_helper.train_model(X, y, Model)
        return clf

    def buildFeaturesAndLabels(self, df):
        lendingclub_features.build_features_by_columns(df, self.feature_column_defs)
        lendingclub_features.build_categorical_label(df, self.labelize_columns[0], lendingclub_features.parse_loan_status)


