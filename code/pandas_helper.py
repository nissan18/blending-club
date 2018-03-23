import pandas as pd

import columns


def readData(filename):
    assert(isinstance(filename, str))

    return pd.read_csv(filename, dtype=columns.dtypes)


def columnHasNull(df, col):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(col, str))

    return df[col].isnull().any()


def columnsHaveNull(df, cols):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(cols, list))
    assert(all([isinstance(c, str) for c in cols]))

    return all([c for c in cols if columnHasNull(df, c)])


def getNumericColumns(df):
    assert(isinstance(df, pd.DataFrame))

    return df.columns[df.dtypes != "O"]  # really non-object columns


def getObjectColumns(df):
    assert(isinstance(df, pd.DataFrame))

    return df.columns[df.dtypes == "O"]


def getNullableColumns(df):
    assert(isinstance(df, pd.DataFrame))

    return df.columns[df.isna().all()]


def getNonNullableColumns(df):
    assert(isinstance(df, pd.DataFrame))

    return df.columns[df.notna().all()]


def getFeatures(df):
    assert(isinstance(df, pd.DataFrame))

    numeric_columns = getNumericColumns(df)
    nonnullable_columns = getNonNullableColumns(df)
    numeric_nonnullable_columns = list(set(numeric_columns) & set(nonnullable_columns))
    return numeric_nonnullable_columns
