import numpy as np
import pandas as pd

from dateutil import parser as dateparser
from datetime import datetime

import definitions
import pandas_helper


# https://docs.scipy.org/doc/numpy-1.13.0/user/basics.types.html
dtypes = {  # TODO: possibly consider trimming memory footprint later
    'acc_now_delinq': 'float64',
    'acc_open_past_24mths': 'float64',
    'addr_state': str,
    'all_util': 'float64',
    'annual_inc': 'float64',
    'annual_inc_joint': 'float64',
    'application_type': str,
    'avg_cur_bal': 'float64',
    'bc_open_to_buy': 'float64',
    'bc_util': 'float64',
    'chargeoff_within_12_mths': 'float64',
    'collection_recovery_fee': 'float64',
    'collections_12_mths_ex_med': 'float64',
    'debt_settlement_flag': str,
    'debt_settlement_flag_date': str,
    'deferral_term': 'float64',
    'delinq_2yrs': 'float64',
    'delinq_amnt': 'float64',
    'desc': str,
    'disbursement_method': str,
    'dti': 'float64',
    'dti_joint': 'float64',
    'earliest_cr_line': str,
    'emp_length': str,
    'emp_title': str,
    'fico_range_high': 'int64',
    'fico_range_low': 'int64',
    'funded_amnt': 'int64',
    'funded_amnt_inv': 'float64',
    'grade': str,
    'hardship_amount': 'float64',
    'hardship_dpd': 'float64',
    'hardship_end_date': str,
    'hardship_flag': str,
    'hardship_last_payment_amount': 'float64',
    'hardship_length': 'float64',
    'hardship_loan_status': str,
    'hardship_payoff_balance_amount': 'float64',
    'hardship_reason': str,
    'hardship_start_date': str,
    'hardship_status': str,
    'hardship_type': str,
    'home_ownership': str,
    'id': 'int64',
    'il_util': 'float64',
    'initial_list_status': str,
    'inq_fi': 'float64',
    'inq_last_12m': 'float64',
    'inq_last_6mths': 'float64',
    'installment': 'float64',
    'int_rate': str,
    'issue_d': str,
    'last_credit_pull_d': str,
    'last_fico_range_high': 'int64',
    'last_fico_range_low': 'int64',
    'last_pymnt_amnt': 'float64',
    'last_pymnt_d': str,
    'loan_amnt': 'int64',
    'loan_status': str,
    'max_bal_bc': 'float64',
    'member_id': 'float64',
    'mo_sin_old_il_acct': 'float64',
    'mo_sin_old_rev_tl_op': 'float64',
    'mo_sin_rcnt_rev_tl_op': 'float64',
    'mo_sin_rcnt_tl': 'float64',
    'mort_acc': 'float64',
    'mths_since_last_delinq': 'float64',
    'mths_since_last_major_derog': 'float64',
    'mths_since_last_record': 'float64',
    'mths_since_rcnt_il': 'float64',
    'mths_since_recent_bc': 'float64',
    'mths_since_recent_bc_dlq': 'float64',
    'mths_since_recent_inq': 'float64',
    'mths_since_recent_revol_delinq': 'float64',
    'next_pymnt_d': str,
    'num_accts_ever_120_pd': 'float64',
    'num_actv_bc_tl': 'float64',
    'num_actv_rev_tl': 'float64',
    'num_bc_sats': 'float64',
    'num_bc_tl': 'float64',
    'num_il_tl': 'float64',
    'num_op_rev_tl': 'float64',
    'num_rev_accts': 'float64',
    'num_rev_tl_bal_gt_0': 'float64',
    'num_sats': 'float64',
    'num_tl_120dpd_2m': 'float64',
    'num_tl_30dpd': 'float64',
    'num_tl_90g_dpd_24m': 'float64',
    'num_tl_op_past_12m': 'float64',
    'open_acc': 'float64',
    'open_acc_6m': 'float64',
    'open_act_il': 'float64',
    'open_il_12m': 'float64',
    'open_il_24m': 'float64',
    'open_rv_12m': 'float64',
    'open_rv_24m': 'float64',
    'orig_projected_additional_accrued_interest': 'float64',
    'out_prncp': 'float64',
    'out_prncp_inv': 'float64',
    'payment_plan_start_date': str,
    'pct_tl_nvr_dlq': 'float64',
    'percent_bc_gt_75': 'float64',
    'policy_code': 'int64',
    'pub_rec': 'float64',
    'pub_rec_bankruptcies': 'float64',
    'purpose': str,
    'pymnt_plan': str,
    'recoveries': 'float64',
    'revol_bal': 'int64',
    'revol_bal_joint': 'float64',
    'revol_util': str,
    'sec_app_chargeoff_within_12_mths': 'float64',
    'sec_app_collections_12_mths_ex_med': 'float64',
    'sec_app_earliest_cr_line': str,
    'sec_app_fico_range_high': 'float64',
    'sec_app_fico_range_low': 'float64',
    'sec_app_inq_last_6mths': 'float64',
    'sec_app_mort_acc': 'float64',
    'sec_app_mths_since_last_major_derog': 'float64',
    'sec_app_num_rev_accts': 'float64',
    'sec_app_open_acc': 'float64',
    'sec_app_open_act_il': 'float64',
    'sec_app_revol_util': 'float64',
    'settlement_amount': 'float64',
    'settlement_date': str,
    'settlement_percentage': 'float64',
    'settlement_status': str,
    'settlement_term': 'float64',
    'sub_grade': str,
    'tax_liens': 'float64',
    'term': str,
    'title': str,
    'tot_coll_amt': 'float64',
    'tot_cur_bal': 'float64',
    'tot_hi_cred_lim': 'float64',
    'total_acc': 'float64',
    'total_bal_ex_mort': 'float64',
    'total_bal_il': 'float64',
    'total_bc_limit': 'float64',
    'total_cu_tl': 'float64',
    'total_il_high_credit_limit': 'float64',
    'total_pymnt': 'float64',
    'total_pymnt_inv': 'float64',
    'total_rec_int': 'float64',
    'total_rec_late_fee': 'float64',
    'total_rec_prncp': 'float64',
    'total_rev_hi_lim': 'float64',
    'url': str,
    'verification_status': str,
    'verification_status_joint': str,
    'zip_code': str
}

def getFinishedLoans(df):
    assert(isinstance(df, pd.DataFrame))

    finishedStatuses = ['Fully Paid',
                        'Charged Off',
                        'Does not meet the credit policy. Status:Fully Paid',
                        'Does not meet the credit policy. Status:Charged Off']
    return df[df.loan_status.isin(finishedStatuses)]


def convertLoanStatus(status):
    convert = {
        'Fully Paid': 1,
        'Charged Off': 0,
        'Does not meet the credit policy. Status:Fully Paid': 1,
        'Does not meet the credit policy. Status:Charged Off': 0,
    }
    assert(status in convert)
    return convert[status]


def extractData(df, features):
    return df[features].values, df["loan_status"].apply(convertLoanStatus).values


def buildFeatures(df):
    buildNumericFeature(df, "acc_now_delinq")
    buildNumericFeature(df, "acc_open_past_24mths")
    buildOneHotEncodingFeature(df, "addr_state")
    buildNumericFeature(df, "all_util")
    buildNumericFeature(df, "annual_inc")
    buildNumericFeature(df, "annual_inc_joint")
    buildOneHotEncodingFeature(df, "application_type")
    buildNumericFeature(df, "avg_cur_bal")
    buildNumericFeature(df, "bc_open_to_buy")
    buildNumericFeature(df, "bc_util")
    buildNumericFeature(df, "chargeoff_within_12_mths")
    buildNumericFeature(df, "collection_recovery_fee")
    buildNumericFeature(df, "collections_12_mths_ex_med")
    buildNumericFeature(df, "delinq_2yrs")
    buildNumericFeature(df, "delinq_amnt")
    # TODO: desc -- NLP?
    buildNumericFeature(df, "dti")
    buildNumericFeature(df, "dti_joint")
    buildDateFeature(df, "earliest_cr_line")
    buildOneHotEncodingFeature(df, "emp_length")
    # TODO: emp_title -- NLP -- data is pretty random
    buildNumericFeature(df, "fico_range_high")
    buildNumericFeature(df, "fico_range_low")
    buildNumericFeature(df, "funded_amnt")
    buildNumericFeature(df, "funded_amnt_inv")
    buildOneHotEncodingFeature(df, "grade")
    buildOneHotEncodingFeature(df, "home_ownership")
    # TODO: id -- don't need this for real model, maybe add to test for noise
    buildNumericFeature(df, "il_util")
    buildOneHotEncodingFeature(df, "initial_list_status")
    buildNumericFeature(df, "inq_fi")
    buildNumericFeature(df, "inq_last_12m")
    buildNumericFeature(df, "inq_last_6mths")
    buildNumericFeature(df, "installment")
    df["f_int_rate"] = df["int_rate"].apply(lambda val : np.float64(val.strip(" %")))
    buildDateFeature(df, "issue_d")
    buildDateFeature(df, "last_credit_pull_d")
    buildNumericFeature(df, "last_fico_range_high")
    buildNumericFeature(df, "last_fico_range_low")
    buildNumericFeature(df, "last_pymnt_amnt")
    buildDateFeature(df, "last_pymnt_d")
    buildNumericFeature(df, "loan_amnt")
    # TODO: loan_status -- one hot encoding of
    """
    convert = {
        'Fully Paid',
        'Charged Off',
        'Does not meet the credit policy. Status:Fully Paid',
        'Does not meet the credit policy. Status:Charged Off',
        'Current',
        'Late (16-30 days)',
        'Late (31-120 days)',
        'In Grace Period',
        'Default'
    }
    """
    buildNumericFeature(df, "max_bal_bc")
    buildNumericFeature(df, "mo_sin_old_il_acct")
    buildNumericFeature(df, "mo_sin_old_rev_tl_op")
    buildNumericFeature(df, "mo_sin_rcnt_rev_tl_op")
    buildNumericFeature(df, "mo_sin_rcnt_tl")
    buildNumericFeature(df, "mort_acc")
    buildNumericFeature(df, "mths_since_last_delinq")
    buildNumericFeature(df, "mths_since_last_major_derog")
    buildNumericFeature(df, "mths_since_last_record")
    buildNumericFeature(df, "mths_since_rcnt_il")
    buildNumericFeature(df, "mths_since_recent_bc")
    buildNumericFeature(df, "mths_since_recent_bc_dlq")
    buildNumericFeature(df, "mths_since_recent_inq")
    buildNumericFeature(df, "mths_since_recent_revol_delinq")
    buildDateFeature(df, "next_pymnt_d")
    buildNumericFeature(df, "num_accts_ever_120_pd")
    buildNumericFeature(df, "num_actv_bc_tl")
    buildNumericFeature(df, "num_actv_rev_tl")
    buildNumericFeature(df, "num_bc_sats")
    buildNumericFeature(df, "num_bc_tl")
    buildNumericFeature(df, "num_il_tl")
    buildNumericFeature(df, "num_op_rev_tl")
    buildNumericFeature(df, "num_rev_accts")
    buildNumericFeature(df, "num_rev_tl_bal_gt_0")
    buildNumericFeature(df, "num_sats")
    buildNumericFeature(df, "num_tl_120dpd_2m")
    buildNumericFeature(df, "num_tl_30dpd")
    buildNumericFeature(df, "num_tl_90g_dpd_24m")
    buildNumericFeature(df, "num_tl_op_past_12m")
    buildNumericFeature(df, "open_acc")
    buildNumericFeature(df, "open_acc_6m")
    buildNumericFeature(df, "open_il_12m")
    buildNumericFeature(df, "open_il_24m")
    buildNumericFeature(df, "open_act_il")
    buildNumericFeature(df, "open_rv_12m")
    buildNumericFeature(df, "open_rv_24m")
    buildNumericFeature(df, "out_prncp")
    buildNumericFeature(df, "out_prncp_inv")
    buildNumericFeature(df, "pct_tl_nvr_dlq")
    buildNumericFeature(df, "percent_bc_gt_75")
    buildOneHotEncodingFeature(df, "policy_code")
    buildNumericFeature(df, "pub_rec")
    buildNumericFeature(df, "pub_rec_bankruptcies")
    buildOneHotEncodingFeature(df, "purpose")
    buildOneHotEncodingFeature(df, "pymnt_plan")
    buildNumericFeature(df, "recoveries")
    buildNumericFeature(df, "revol_bal")
    buildPercentageFeature(df, "revol_util")
    buildOneHotEncodingFeature(df, "sub_grade")
    buildNumericFeature(df, "tax_liens")
    buildOneHotEncodingFeature(df, "term")
    # TODO: title -- nlp?
    buildNumericFeature(df, "tot_coll_amt")
    buildNumericFeature(df, "tot_cur_bal")
    buildNumericFeature(df, "tot_hi_cred_lim")
    buildNumericFeature(df, "total_acc")
    buildNumericFeature(df, "total_bal_ex_mort")
    buildNumericFeature(df, "total_bal_il")
    buildNumericFeature(df, "total_bc_limit")
    buildNumericFeature(df, "total_cu_tl")
    buildNumericFeature(df, "total_il_high_credit_limit")
    buildNumericFeature(df, "total_pymnt")
    buildNumericFeature(df, "total_pymnt_inv")
    buildNumericFeature(df, "total_rec_int")
    buildNumericFeature(df, "total_rec_late_fee")
    buildNumericFeature(df, "total_rec_prncp")
    buildNumericFeature(df, "total_rev_hi_lim")
    # TODO: url -- check probably always https://lendingclub.com/browse/loanDetail.action?loan_id=<id>
    buildOneHotEncodingFeature(df, "verification_status")
    # TODO: verified_status_joint -- column not found in any dataSets
    buildOneHotEncodingFeature(df, "zip_code")
    buildNumericFeature(df, "revol_bal_joint")
    buildNumericFeature(df, "sec_app_fico_range_low")
    buildNumericFeature(df, "sec_app_fico_range_high")
    buildDateFeature(df, "sec_app_earliest_cr_line")
    buildNumericFeature(df, "sec_app_inq_last_6mths")
    buildNumericFeature(df, "sec_app_mort_acc")
    buildNumericFeature(df, "sec_app_open_acc")
    buildNumericFeature(df, "sec_app_revol_util")
    buildNumericFeature(df, "sec_app_open_act_il")
    buildNumericFeature(df, "sec_app_num_rev_accts")
    buildNumericFeature(df, "sec_app_chargeoff_within_12_mths")
    buildNumericFeature(df, "sec_app_collections_12_mths_ex_med")
    buildNumericFeature(df, "sec_app_mths_since_last_major_derog")
    buildOneHotEncodingFeature(df, "hardship_flag")
    buildOneHotEncodingFeature(df, "hardship_type")
    buildOneHotEncodingFeature(df, "hardship_reason")
    buildOneHotEncodingFeature(df, "hardship_status")
    buildNumericFeature(df, "deferral_term")
    buildNumericFeature(df, "hardship_amount")
    buildDateFeature(df, "hardship_start_date")
    buildDateFeature(df, "hardship_end_date")
    buildDateFeature(df, "payment_plan_start_date")
    buildNumericFeature(df, "hardship_length")
    buildNumericFeature(df, "hardship_dpd")
    buildOneHotEncodingFeature(df, "hardship_loan_status")
    buildNumericFeature(df, "orig_projected_additional_accrued_interest")
    buildNumericFeature(df, "hardship_payoff_balance_amount")
    buildNumericFeature(df, "hardship_last_payment_amount")
    buildOneHotEncodingFeature(df, "disbursement_method")
    buildOneHotEncodingFeature(df, "debt_settlement_flag")
    buildDateFeature(df, "debt_settlement_flag_date")
    buildOneHotEncodingFeature(df, "settlement_status")
    buildDateFeature(df, "settlement_date")
    buildNumericFeature(df, "settlement_amount")
    buildNumericFeature(df, "settlement_percentage")
    buildNumericFeature(df, "settlement_term")


def getFeatureColumns(df):
    assert(isinstance(df, pd.DataFrame))

    return pandas_helper.getColumnsByPrefix(df, "f_")

def parse_loan_status(value):
    convert = {
        'Fully Paid': 1,
        'Charged Off': 0,
        'Does not meet the credit policy. Status:Fully Paid': 1,
        'Does not meet the credit policy. Status:Charged Off': 0,
        'Current': None,
        'Late (16-30 days)': None,
        'Late (31-120 days)': None,
        'In Grace Period': None,
        'Default': None
    }
    assert(value in convert)
    return convert[value]


def buildCategorialLabel(df, col, parse_function):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(col, str))
    # TODO: assert parse_function????

    label_col = "l_" + col
    df[label_col] = df[col].apply(parse_function)


def getLabelColumns(df):
    assert(isinstance(df, pd.DataFrame))

    return pandas_helper.getColumnsByPrefix(df, "l_")


def buildNumericFeature(df, col):
    # TODO: consider normalize
    # TODO: consider filling na with mean instead of 0
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(col, str))

    df["f_" + col] = df[col].fillna(0)


def buildOneHotEncodingFeature(df, col, values=None):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(col, str))
    assert (values is None or isinstance(values, list)), "This should be a list: {0}".format(values)

    if "NULL" not in values:
        values.append("NULL")

    tempCol = "f_" + col
    df[tempCol] = df[col].fillna(col + "_NULL")  # create temporary column to fill na values
    real_values = df[tempCol].values
    assert (values is None or set(real_values).issubset(set(values))), "First set should be a subset of the second:\n{0}\n{1}".format(set(real_values), set(values))

    temp = pandas_helper.getOneHotEncoding(df, tempCol)
    for c in temp.columns:
        df[c] = temp[c]
    df.drop(tempCol, axis=1, inplace=True)  # drop temporary column

    # fill remaining columns
    if values is not None:
        length = df.shape[0]
        for val in values:
            col_name = tempCol + "_" + val
            if col_name not in df.columns:
                df[col_name] = 0 * np.ones(length)


def buildPercentageFeature(df, col):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(col, str))

    f_col = "f_" + col
    df[f_col] = df[col].str.strip("%").astype(float)/100
    df[f_col] = df[f_col].fillna(df[f_col].mean())


def buildDateFeature(df, col):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(col, str))


    month_col = col + "_month"  # create temporary column to parse month name
    df[month_col] = pd.to_datetime(df[col]).dt.strftime('%b').replace("NaT", "NULL")  # handle nan dates in df[col]
    buildOneHotEncodingFeature(df, month_col, values=definitions.months)
    df.drop(month_col, axis=1, inplace=True)  # drop temporary column

    f_diff = "f_{0}_diff".format(col)
    today = datetime.today()
    df[f_diff] = (today - pd.to_datetime(df[col]))/np.timedelta64(1, "D")
    df[f_diff] = df[f_diff].fillna(0)  # if want to fill with mean, check if mean is not nan


def build_features_by_columns(df, feature_columns):
    for col in feature_columns:
        if col["feature"]["type"] == "numeric":
            buildNumericFeature(df, col["name"])
        elif col["feature"]["type"] == "one-hot encoding":
            buildOneHotEncodingFeature(df, col["name"], col["feature"]["values"])
        else:
            raise Exception("Unsuported feature_type: {}".format(col["feature"]["type"]))

