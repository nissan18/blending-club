import pandas as pd


def getNumericColumns(df):
    assert(df is pd.DataFrame)
    return df.columns[df.dtypes != "O"]  # really non-object columns


def getObjectColumns(df):
    assert(df is pd.DataFrame)
    return df.columns[df.dtypes == "O"]


def getNullableColumns(df):
    assert(df is pd.DataFrame)
    return df.columns[df.isna().all()]


def getNonNullableColumns(df):
    assert(df is pd.DataFrame)
    return df.columns[df.notna().all()]


def getFeatures(df):
    assert(df is pd.DataFrame)
    numeric_columns = getNumericColumns(df)
    nonnullable_columns = getNonNullableColumns(df)
    numeric_nonnullable_columns = list(set(numeric_columns) & set(nonnullable_columns))
    return numeric_nonnullable_columns
