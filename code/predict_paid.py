import pandas_helper
import lendingclub_helper
import scikit_helper


def main():
    """
    1. DONE create finished_loans.csv from all_loans.csv
    2. DONE extract sample of finished loans
    3. train basic SVC model
    4. validate on rest of finished loans (or a sample)
    5. try other models

    999. do the same in time series and/or with K-fold validation
    """
    print("begin")
    
    train_data_file = "finished_train_sample.csv"
    # test_data_file = "finished_test_sample.csv"

    df = pandas_helper.readData(train_data_file, lendingclub_helper.dtypes)
    print("shape", df.shape)

    lendingclub_helper.buildFeatures(df)
    lendingclub_helper.buildCategorialLabel(df, "loan_status", lendingclub_helper.parse_loan_status)
    print("shape", df.shape)

    feature_columns = lendingclub_helper.getFeatureColumns(df)
    features = df[feature_columns]

    label_columns = lendingclub_helper.getLabelColumns(df)
    labels = df[label_columns[0]]

    model = scikit_helper.trainModel(features.values, labels.values)
    print(model)

    # df = lendingclub_helper.getFinishedLoans(df)
    # print("shape", df.shape)

    # model = scikit_helper.trainModel(X, y)


    print("end")


if __name__ == "__main__":
    main()
