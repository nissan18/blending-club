import pandas_helper
import lendingclub_columns
import lendingclub_helper


class LendingClub_Pipeline:

    def __init__(self):
        self.sooka = "pipeline"


    def run(self, trainset_filename, testset_filename):
        # read trainset_file
        # extractd features, labels
        # build model
        # check accuracy on trainset
        # check accuracy on testset

        df_train = pandas_helper.readData(trainset_filename, lendingclub_columns.get_dtypes_by_name())

        self.buildFeatures(df_train)


    def buildFeatures(self, df):

        feature_columns = lendingclub_columns.get_columns_by_names(["annual_inc", "sub_grade"])
        lendingclub_helper.build_features_by_columns(df, feature_columns)


        pass
