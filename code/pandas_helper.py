import pandas as pd


def readData(filename, dtypes):
    assert(isinstance(filename, str))

    return pd.read_csv(filename, dtype=dtypes)


def writeData(df, filename):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(filename, str))

    df.to_csv(filename, index=False)


def getColumnsByPrefix(df, prefix):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(prefix, str))

    return df.columns[df.columns.str.startswith(prefix)]


def columnHasNull(df, col):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(col, str))

    return df[col].isnull().any()


def columnsHaveNull(df, cols):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(cols, list))
    assert(all([isinstance(c, str) for c in cols]))

    return all([columnHasNull(df, c) for c in cols])


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


def getOneHotEncoding(df, col):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(col, str))

    temp = pd.get_dummies(df[col])
    temp.columns = ["{0}_{1}".format(col, c) for c in temp.columns]
    return temp
