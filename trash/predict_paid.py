import pandas_helper
import lendingclub_helper
import scikit_helper


def main():
    """
    1. DONE create finished_loans.csv from all_loans.csv
    2. DONE extract sample of finished loans
    3. DONE train basic SVC model
    4. validate on rest of finished loans (or a sample)
    5. try other models

    999. do the same in time series and/or with K-fold validation
    """
    print("begin")
    
    train_data_file = "finished_train_sample.csv"
    test_data_file = "finished_test_sample.csv"

    train_df = getTrainableDataFrame(train_data_file)
    print("shape", train_df.shape)

    feature_columns = lendingclub_helper.getFeatureColumns(train_df)
    train_features = train_df[feature_columns]

    label_columns = lendingclub_helper.getLabelColumns(train_df)
    train_labels = train_df[label_columns[0]]

    model = scikit_helper.trainModel(train_features.values, train_labels.values)
    print(model)

    train_accuracy = scikit_helper.getAccuracy(model, train_features.values, train_labels.values)
    print("Train accuracy:", train_accuracy)


    test_df = getTrainableDataFrame(test_data_file)
    print("shape", test_df.shape)

    test_features = test_df[feature_columns]
    test_labels = test_df[label_columns[0]]

    test_accuracy = scikit_helper.getAccuracy(model, train_features.values, train_labels.values)
    print("Test accuracy:", test_accuracy)

    # df = lendingclub_helper.getFinishedLoans(df)
    # print("shape", df.shape)

    # model = scikit_helper.trainModel(X, y)


    print("end")


def getTrainableDataFrame(filename):
    train_data_file = filename

    df = pandas_helper.readData(train_data_file, lendingclub_helper.dtypes)

    lendingclub_helper.buildFeatures(df)
    lendingclub_helper.buildCategorialLabel(df, "loan_status", lendingclub_helper.parse_loan_status)

    return df


if __name__ == "__main__":
    main()
