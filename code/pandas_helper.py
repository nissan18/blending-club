import pandas as pd


def read_data(filename, dtypes):
    assert(isinstance(filename, str))

    return pd.read_csv(filename, dtype=dtypes)


def write_data(df, filename):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(filename, str))

    df.to_csv(filename, index=False)


def get_columns_by_prefix(df, prefix):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(prefix, str))

    return df.columns[df.columns.str.startswith(prefix)]


def column_has_null(df, col):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(col, str))

    return df[col].isnull().any()


def columns_have_null(df, cols):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(cols, list))
    assert(all([isinstance(c, str) for c in cols]))

    return all([columnHasNull(df, c) for c in cols])


def get_numeric_columns(df):
    assert(isinstance(df, pd.DataFrame))

    return df.columns[df.dtypes != "O"]  # really non-object columns


def get_object_columns(df):
    assert(isinstance(df, pd.DataFrame))

    return df.columns[df.dtypes == "O"]


def get_nullable_columns(df):
    assert(isinstance(df, pd.DataFrame))

    return df.columns[df.isna().all()]


def get_non_nullable_columns(df):
    assert(isinstance(df, pd.DataFrame))

    return df.columns[df.notna().all()]


def get_one_hot_encoding(df, col):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(col, str))

    temp = pd.get_dummies(df[col])
    temp.columns = ["{0}_{1}".format(col, c) for c in temp.columns]
    return temp
