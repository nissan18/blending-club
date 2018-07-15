import pandas as pd

import lendingclub_columns


def validate_one_hot_encoding_columns(df):
    assert(isinstance(df, pd.DataFrame))

    """
    make sure all non-nan values in df are in lendingclub_columns.columns
    here ignore nan values, when building the feature they will be replacted with <col_name>_NULL
    """
    columns = lendingclub_columns.get_columns_by_feature_type("one-hot encoding")

    for c in columns:
        real_values = df[c["name"]].dropna().values
        only_in_columns = set(c["feature"]["values"]) - set(real_values)
        only_in_real_values = set(real_values) - set(c["feature"]["values"])
        if len(only_in_real_values) > 0:
            print("Column: {}".format(c["name"]))
            # print("only_in_columns: ", only_in_columns)
            print("only_in_real_values: ", only_in_real_values)
