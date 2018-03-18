# Pandas helper functions

def getNumericColumns(df):
    return df.columns[df.dtypes != "O"]  # really non-object columns


def getObjectColumns(df):
    return df.columns[df.dtypes == "O"]


def getNullableColumns(df):
    return df.columns[df.isna().all()]


def getNonNullableColumns(df):
    return df.columns[df.notna().all()]


# TODO: refactor into different file
def getFinishedLoans(df):
    finishedStatuses = ['Fully Paid',
                        'Charged Off',
                        'Does not meet the credit policy. Status:Fully Paid',
                        'Does not meet the credit policy. Status:Charged Off']
    return df[df.loan_status.isin(finishedStatuses)]
