import pandas_helper
import lendingclub_helper


def main():
    """
    1. DONE create finished_loans.csv from all_loans.csv
    2. extract sample of finished loans
    3. train basic SVC model
    4. validate on rest of finished loans (or a sample)
    5. try other models

    999. do the same in time series
    """
    print("begin")
    filename = "../data/finished_loans.csv"
    # filename = "sample.csv"
    df = pandas_helper.readData(filename, lendingclub_helper.dtypes)
    print("shape", df.shape)

    df = lendingclub_helper.getFinishedLoans(df)
    print("shape", df.shape)


    print("end")


if __name__ == "__main__":
    main()
