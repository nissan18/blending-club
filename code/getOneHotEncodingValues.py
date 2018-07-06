import pandas_helper
import lendingclub_helper


def main():
    print("begin getOneHotEncodingValues")

    filename = ""
    columns = ""


    df = pandas_helper.readData(filename, lendingclub_helper.dtypes)
    
    """
    load filename into pandas dataframe
    for each col in columns
        extract unique values
        write them to file

    """

    print("end getOneHotEncodingValues")


if __name__ == "__main__":
    main()
