# Pandas helper functions

def getNumericColumns(df):
    return df.columns[df.dtypes != "O"]  # really non-object columns


def getObjectColumns(df):
    return df.columns[df.dtypes == "O"]


def nullableColumns(df):
    return df.columns[df.isna().all()]


def nonNullableColumns(df):
    return df.columns[df.notna().all()]
