import pandas_helper
import scikit_helper

import lendingclub_columns
import lendingclub_helper


class LendingClub_Pipeline:

    def __init__(self):
        pass


    def run(self, trainset_filename, testset_filename):
        # read trainset_file
        # extractd features, labels
        # build model
        # check accuracy on trainset
        # check accuracy on testset

        df_train = pandas_helper.readData(trainset_filename, lendingclub_columns.get_dtypes_by_name())

        self.buildFeaturesAndLabels(df_train)

        feature_columns = lendingclub_helper.getFeatureColumns(df_train)
        label_columns = lendingclub_helper.getLabelColumns(df_train)

        print("features: {}".format(feature_columns))
        print("labels: {}".format(label_columns))


        X = df_train[feature_columns].values
        y = df_train[label_columns[0]].values
        # print(df_train[['f_annual_inc', 'f_sub_grade_A1', 'f_sub_grade_A2', 'f_sub_grade_A3', 'f_sub_grade_A4', 'f_sub_grade_A5', 'f_sub_grade_B1', 'f_sub_grade_B2', 'f_sub_grade_B3', 'f_sub_grade_B4', 'f_sub_grade_B5', 'f_sub_grade_C1', 'f_sub_grade_C2', 'f_sub_grade_C3', 'f_sub_grade_C4', 'f_sub_grade_C5', 'f_sub_grade_D1', 'f_sub_grade_D2', 'f_sub_grade_D3', 'f_sub_grade_D4', 'f_sub_grade_D5', 'f_sub_grade_E1', 'f_sub_grade_E2', 'f_sub_grade_E3', 'f_sub_grade_E4', 'f_sub_grade_E5', 'f_sub_grade_F1', 'f_sub_grade_F2', 'f_sub_grade_F4', 'f_sub_grade_F5', 'f_sub_grade_G1', 'f_sub_grade_G2', 'f_sub_grade_F3', 'f_sub_grade_G4', 'f_sub_grade_G5', 'f_sub_grade_NULL']])
        # print(df_train[feature_columns])
        # print(df_train[[label_columns]])
        # print(df_train[feature_columns + label_columns])

        model = scikit_helper.trainModel(X, y)
        print(model)



    def buildFeaturesAndLabels(self, df):
        feature_columns = lendingclub_columns.get_columns_by_names(["annual_inc", "sub_grade"])
        # feature_columns = lendingclub_columns.get_columns_by_names(["annual_inc"])
        lendingclub_helper.build_features_by_columns(df, feature_columns)
        lendingclub_helper.buildCategorialLabel(df, "loan_status", lendingclub_helper.parse_loan_status)


