import pandas_helper
import lendingclub_features
import lendingclub_columns
import pprint as pp


def main():
    print("begin getOneHotEncodingValues")

    filename = "sample.csv"
    columns = lendingclub_columns.get_columns_by_feature_type("one-hot encoding")

    for c in columns:
        l = len(c["feature"]["values"])
        if l == 0:
            print("{} has NO values".format(c["name"]))
        else:
            print("{} has {} values".format(c["name"], l))
    
    # df = pandas_helper.read_data(filename, lendingclub_columns.get_dtypes_by_name())


    # all_values = {}
    # for c in columns:
    #     try:
    #         values = df[c["name"]].dropna().values
    #         values = sorted(list(set(values)))
    #         all_values[c["name"]] = values
    #     except Exception as e:
    #         print("Error in column: ", c)
    #         print(e)
    #         print(values)
    #         return


    # pp.pprint(all_values, "all_values.txt")
    # with open("all_values.txt", "w") as fout:
    #     pp.pprint(all_values, fout)

    print("end getOneHotEncodingValues")





if __name__ == "__main__":
    main()
