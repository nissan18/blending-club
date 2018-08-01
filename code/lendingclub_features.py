import numpy as np
import pandas as pd

from dateutil import parser as dateparser
from datetime import datetime

import definitions
import pandas_helper


# https://docs.scipy.org/doc/numpy-1.13.0/user/basics.types.html
# dtypes = {  # TODO: possibly consider trimming memory footprint later
#     'acc_now_delinq': 'float64',
#     'acc_open_past_24mths': 'float64',
#     'addr_state': str,
#     'all_util': 'float64',
#     'annual_inc': 'float64',
#     'annual_inc_joint': 'float64',
#     'application_type': str,
#     'avg_cur_bal': 'float64',
#     'bc_open_to_buy': 'float64',
#     'bc_util': 'float64',
#     'chargeoff_within_12_mths': 'float64',
#     'collection_recovery_fee': 'float64',
#     'collections_12_mths_ex_med': 'float64',
#     'debt_settlement_flag': str,
#     'debt_settlement_flag_date': str,
#     'deferral_term': 'float64',
#     'delinq_2yrs': 'float64',
#     'delinq_amnt': 'float64',
#     'desc': str,
#     'disbursement_method': str,
#     'dti': 'float64',
#     'dti_joint': 'float64',
#     'earliest_cr_line': str,
#     'emp_length': str,
#     'emp_title': str,
#     'fico_range_high': 'int64',
#     'fico_range_low': 'int64',
#     'funded_amnt': 'int64',
#     'funded_amnt_inv': 'float64',
#     'grade': str,
#     'hardship_amount': 'float64',
#     'hardship_dpd': 'float64',
#     'hardship_end_date': str,
#     'hardship_flag': str,
#     'hardship_last_payment_amount': 'float64',
#     'hardship_length': 'float64',
#     'hardship_loan_status': str,
#     'hardship_payoff_balance_amount': 'float64',
#     'hardship_reason': str,
#     'hardship_start_date': str,
#     'hardship_status': str,
#     'hardship_type': str,
#     'home_ownership': str,
#     'id': 'int64',
#     'il_util': 'float64',
#     'initial_list_status': str,
#     'inq_fi': 'float64',
#     'inq_last_12m': 'float64',
#     'inq_last_6mths': 'float64',
#     'installment': 'float64',
#     'int_rate': str,
#     'issue_d': str,
#     'last_credit_pull_d': str,
#     'last_fico_range_high': 'int64',
#     'last_fico_range_low': 'int64',
#     'last_pymnt_amnt': 'float64',
#     'last_pymnt_d': str,
#     'loan_amnt': 'int64',
#     'loan_status': str,
#     'max_bal_bc': 'float64',
#     'member_id': 'float64',
#     'mo_sin_old_il_acct': 'float64',
#     'mo_sin_old_rev_tl_op': 'float64',
#     'mo_sin_rcnt_rev_tl_op': 'float64',
#     'mo_sin_rcnt_tl': 'float64',
#     'mort_acc': 'float64',
#     'mths_since_last_delinq': 'float64',
#     'mths_since_last_major_derog': 'float64',
#     'mths_since_last_record': 'float64',
#     'mths_since_rcnt_il': 'float64',
#     'mths_since_recent_bc': 'float64',
#     'mths_since_recent_bc_dlq': 'float64',
#     'mths_since_recent_inq': 'float64',
#     'mths_since_recent_revol_delinq': 'float64',
#     'next_pymnt_d': str,
#     'num_accts_ever_120_pd': 'float64',
#     'num_actv_bc_tl': 'float64',
#     'num_actv_rev_tl': 'float64',
#     'num_bc_sats': 'float64',
#     'num_bc_tl': 'float64',
#     'num_il_tl': 'float64',
#     'num_op_rev_tl': 'float64',
#     'num_rev_accts': 'float64',
#     'num_rev_tl_bal_gt_0': 'float64',
#     'num_sats': 'float64',
#     'num_tl_120dpd_2m': 'float64',
#     'num_tl_30dpd': 'float64',
#     'num_tl_90g_dpd_24m': 'float64',
#     'num_tl_op_past_12m': 'float64',
#     'open_acc': 'float64',
#     'open_acc_6m': 'float64',
#     'open_act_il': 'float64',
#     'open_il_12m': 'float64',
#     'open_il_24m': 'float64',
#     'open_rv_12m': 'float64',
#     'open_rv_24m': 'float64',
#     'orig_projected_additional_accrued_interest': 'float64',
#     'out_prncp': 'float64',
#     'out_prncp_inv': 'float64',
#     'payment_plan_start_date': str,
#     'pct_tl_nvr_dlq': 'float64',
#     'percent_bc_gt_75': 'float64',
#     'policy_code': 'int64',
#     'pub_rec': 'float64',
#     'pub_rec_bankruptcies': 'float64',
#     'purpose': str,
#     'pymnt_plan': str,
#     'recoveries': 'float64',
#     'revol_bal': 'int64',
#     'revol_bal_joint': 'float64',
#     'revol_util': str,
#     'sec_app_chargeoff_within_12_mths': 'float64',
#     'sec_app_collections_12_mths_ex_med': 'float64',
#     'sec_app_earliest_cr_line': str,
#     'sec_app_fico_range_high': 'float64',
#     'sec_app_fico_range_low': 'float64',
#     'sec_app_inq_last_6mths': 'float64',
#     'sec_app_mort_acc': 'float64',
#     'sec_app_mths_since_last_major_derog': 'float64',
#     'sec_app_num_rev_accts': 'float64',
#     'sec_app_open_acc': 'float64',
#     'sec_app_open_act_il': 'float64',
#     'sec_app_revol_util': 'float64',
#     'settlement_amount': 'float64',
#     'settlement_date': str,
#     'settlement_percentage': 'float64',
#     'settlement_status': str,
#     'settlement_term': 'float64',
#     'sub_grade': str,
#     'tax_liens': 'float64',
#     'term': str,
#     'title': str,
#     'tot_coll_amt': 'float64',
#     'tot_cur_bal': 'float64',
#     'tot_hi_cred_lim': 'float64',
#     'total_acc': 'float64',
#     'total_bal_ex_mort': 'float64',
#     'total_bal_il': 'float64',
#     'total_bc_limit': 'float64',
#     'total_cu_tl': 'float64',
#     'total_il_high_credit_limit': 'float64',
#     'total_pymnt': 'float64',
#     'total_pymnt_inv': 'float64',
#     'total_rec_int': 'float64',
#     'total_rec_late_fee': 'float64',
#     'total_rec_prncp': 'float64',
#     'total_rev_hi_lim': 'float64',
#     'url': str,
#     'verification_status': str,
#     'verification_status_joint': str,
#     'zip_code': str
# }

def get_finished_loans(df):
    assert (isinstance(df, pd.DataFrame)), "df must be pd.DataFrame"

    finishedStatuses = ['Fully Paid',
                        'Charged Off',
                        'Does not meet the credit policy. Status:Fully Paid',
                        'Does not meet the credit policy. Status:Charged Off']
    return df[df.loan_status.isin(finishedStatuses)]


# def convertLoanStatus(status):
#     convert = {
#         'Fully Paid': 1,
#         'Charged Off': 0,
#         'Does not meet the credit policy. Status:Fully Paid': 1,
#         'Does not meet the credit policy. Status:Charged Off': 0,
#     }
#     assert(status in convert)
#     return convert[status]


# def extractData(df, features):
#     return df[features].values, df["loan_status"].apply(convertLoanStatus).values


# def buildFeatures(df):
#     build_numeric_feature(df, "acc_now_delinq")
#     build_numeric_feature(df, "acc_open_past_24mths")
#     build_one_hot_encoding_feature(df, "addr_state")
#     build_numeric_feature(df, "all_util")
#     build_numeric_feature(df, "annual_inc")
#     build_numeric_feature(df, "annual_inc_joint")
#     build_one_hot_encoding_feature(df, "application_type")
#     build_numeric_feature(df, "avg_cur_bal")
#     build_numeric_feature(df, "bc_open_to_buy")
#     build_numeric_feature(df, "bc_util")
#     build_numeric_feature(df, "chargeoff_within_12_mths")
#     build_numeric_feature(df, "collection_recovery_fee")
#     build_numeric_feature(df, "collections_12_mths_ex_med")
#     build_numeric_feature(df, "delinq_2yrs")
#     build_numeric_feature(df, "delinq_amnt")
#     # TODO: desc -- NLP?
#     build_numeric_feature(df, "dti")
#     build_numeric_feature(df, "dti_joint")
#     build_date_feature(df, "earliest_cr_line")
#     build_one_hot_encoding_feature(df, "emp_length")
#     # TODO: emp_title -- NLP -- data is pretty random
#     build_numeric_feature(df, "fico_range_high")
#     build_numeric_feature(df, "fico_range_low")
#     build_numeric_feature(df, "funded_amnt")
#     build_numeric_feature(df, "funded_amnt_inv")
#     build_one_hot_encoding_feature(df, "grade")
#     build_one_hot_encoding_feature(df, "home_ownership")
#     # TODO: id -- don't need this for real model, maybe add to test for noise
#     build_numeric_feature(df, "il_util")
#     build_one_hot_encoding_feature(df, "initial_list_status")
#     build_numeric_feature(df, "inq_fi")
#     build_numeric_feature(df, "inq_last_12m")
#     build_numeric_feature(df, "inq_last_6mths")
#     build_numeric_feature(df, "installment")
#     df["f_int_rate"] = df["int_rate"].apply(lambda val : np.float64(val.strip(" %")))
#     build_date_feature(df, "issue_d")
#     build_date_feature(df, "last_credit_pull_d")
#     build_numeric_feature(df, "last_fico_range_high")
#     build_numeric_feature(df, "last_fico_range_low")
#     build_numeric_feature(df, "last_pymnt_amnt")
#     build_date_feature(df, "last_pymnt_d")
#     build_numeric_feature(df, "loan_amnt")
#     # TODO: loan_status -- one hot encoding of
#     """
#     convert = {
#         'Fully Paid',
#         'Charged Off',
#         'Does not meet the credit policy. Status:Fully Paid',
#         'Does not meet the credit policy. Status:Charged Off',
#         'Current',
#         'Late (16-30 days)',
#         'Late (31-120 days)',
#         'In Grace Period',
#         'Default'
#     }
#     """
#     build_numeric_feature(df, "max_bal_bc")
#     build_numeric_feature(df, "mo_sin_old_il_acct")
#     build_numeric_feature(df, "mo_sin_old_rev_tl_op")
#     build_numeric_feature(df, "mo_sin_rcnt_rev_tl_op")
#     build_numeric_feature(df, "mo_sin_rcnt_tl")
#     build_numeric_feature(df, "mort_acc")
#     build_numeric_feature(df, "mths_since_last_delinq")
#     build_numeric_feature(df, "mths_since_last_major_derog")
#     build_numeric_feature(df, "mths_since_last_record")
#     build_numeric_feature(df, "mths_since_rcnt_il")
#     build_numeric_feature(df, "mths_since_recent_bc")
#     build_numeric_feature(df, "mths_since_recent_bc_dlq")
#     build_numeric_feature(df, "mths_since_recent_inq")
#     build_numeric_feature(df, "mths_since_recent_revol_delinq")
#     build_date_feature(df, "next_pymnt_d")
#     build_numeric_feature(df, "num_accts_ever_120_pd")
#     build_numeric_feature(df, "num_actv_bc_tl")
#     build_numeric_feature(df, "num_actv_rev_tl")
#     build_numeric_feature(df, "num_bc_sats")
#     build_numeric_feature(df, "num_bc_tl")
#     build_numeric_feature(df, "num_il_tl")
#     build_numeric_feature(df, "num_op_rev_tl")
#     build_numeric_feature(df, "num_rev_accts")
#     build_numeric_feature(df, "num_rev_tl_bal_gt_0")
#     build_numeric_feature(df, "num_sats")
#     build_numeric_feature(df, "num_tl_120dpd_2m")
#     build_numeric_feature(df, "num_tl_30dpd")
#     build_numeric_feature(df, "num_tl_90g_dpd_24m")
#     build_numeric_feature(df, "num_tl_op_past_12m")
#     build_numeric_feature(df, "open_acc")
#     build_numeric_feature(df, "open_acc_6m")
#     build_numeric_feature(df, "open_il_12m")
#     build_numeric_feature(df, "open_il_24m")
#     build_numeric_feature(df, "open_act_il")
#     build_numeric_feature(df, "open_rv_12m")
#     build_numeric_feature(df, "open_rv_24m")
#     build_numeric_feature(df, "out_prncp")
#     build_numeric_feature(df, "out_prncp_inv")
#     build_numeric_feature(df, "pct_tl_nvr_dlq")
#     build_numeric_feature(df, "percent_bc_gt_75")
#     build_one_hot_encoding_feature(df, "policy_code")
#     build_numeric_feature(df, "pub_rec")
#     build_numeric_feature(df, "pub_rec_bankruptcies")
#     build_one_hot_encoding_feature(df, "purpose")
#     build_one_hot_encoding_feature(df, "pymnt_plan")
#     build_numeric_feature(df, "recoveries")
#     build_numeric_feature(df, "revol_bal")
#     build_percentage_feature(df, "revol_util")
#     build_one_hot_encoding_feature(df, "sub_grade")
#     build_numeric_feature(df, "tax_liens")
#     build_one_hot_encoding_feature(df, "term")
#     # TODO: title -- nlp?
#     build_numeric_feature(df, "tot_coll_amt")
#     build_numeric_feature(df, "tot_cur_bal")
#     build_numeric_feature(df, "tot_hi_cred_lim")
#     build_numeric_feature(df, "total_acc")
#     build_numeric_feature(df, "total_bal_ex_mort")
#     build_numeric_feature(df, "total_bal_il")
#     build_numeric_feature(df, "total_bc_limit")
#     build_numeric_feature(df, "total_cu_tl")
#     build_numeric_feature(df, "total_il_high_credit_limit")
#     build_numeric_feature(df, "total_pymnt")
#     build_numeric_feature(df, "total_pymnt_inv")
#     build_numeric_feature(df, "total_rec_int")
#     build_numeric_feature(df, "total_rec_late_fee")
#     build_numeric_feature(df, "total_rec_prncp")
#     build_numeric_feature(df, "total_rev_hi_lim")
#     # TODO: url -- check probably always https://lendingclub.com/browse/loanDetail.action?loan_id=<id>
#     build_one_hot_encoding_feature(df, "verification_status")
#     # TODO: verified_status_joint -- column not found in any dataSets
#     build_one_hot_encoding_feature(df, "zip_code")
#     build_numeric_feature(df, "revol_bal_joint")
#     build_numeric_feature(df, "sec_app_fico_range_low")
#     build_numeric_feature(df, "sec_app_fico_range_high")
#     build_date_feature(df, "sec_app_earliest_cr_line")
#     build_numeric_feature(df, "sec_app_inq_last_6mths")
#     build_numeric_feature(df, "sec_app_mort_acc")
#     build_numeric_feature(df, "sec_app_open_acc")
#     build_numeric_feature(df, "sec_app_revol_util")
#     build_numeric_feature(df, "sec_app_open_act_il")
#     build_numeric_feature(df, "sec_app_num_rev_accts")
#     build_numeric_feature(df, "sec_app_chargeoff_within_12_mths")
#     build_numeric_feature(df, "sec_app_collections_12_mths_ex_med")
#     build_numeric_feature(df, "sec_app_mths_since_last_major_derog")
#     build_one_hot_encoding_feature(df, "hardship_flag")
#     build_one_hot_encoding_feature(df, "hardship_type")
#     build_one_hot_encoding_feature(df, "hardship_reason")
#     build_one_hot_encoding_feature(df, "hardship_status")
#     build_numeric_feature(df, "deferral_term")
#     build_numeric_feature(df, "hardship_amount")
#     build_date_feature(df, "hardship_start_date")
#     build_date_feature(df, "hardship_end_date")
#     build_date_feature(df, "payment_plan_start_date")
#     build_numeric_feature(df, "hardship_length")
#     build_numeric_feature(df, "hardship_dpd")
#     build_one_hot_encoding_feature(df, "hardship_loan_status")
#     build_numeric_feature(df, "orig_projected_additional_accrued_interest")
#     build_numeric_feature(df, "hardship_payoff_balance_amount")
#     build_numeric_feature(df, "hardship_last_payment_amount")
#     build_one_hot_encoding_feature(df, "disbursement_method")
#     build_one_hot_encoding_feature(df, "debt_settlement_flag")
#     build_date_feature(df, "debt_settlement_flag_date")
#     build_one_hot_encoding_feature(df, "settlement_status")
#     build_date_feature(df, "settlement_date")
#     build_numeric_feature(df, "settlement_amount")
#     build_numeric_feature(df, "settlement_percentage")
#     build_numeric_feature(df, "settlement_term")


def get_feature_columns(df):
    assert(isinstance(df, pd.DataFrame))

    return pandas_helper.get_columns_by_prefix(df, "f_")

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


def build_categorical_label(df, col, parse_function):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(col, str))
    # TODO: assert parse_function????

    label_col = "l_" + col
    df[label_col] = df[col].apply(parse_function)


def get_label_columns(df):
    assert(isinstance(df, pd.DataFrame))

    return pandas_helper.get_columns_by_prefix(df, "l_")


def build_numeric_feature(df, col):
    # TODO: consider normalize
    # TODO: consider filling na with mean instead of 0
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(col, str))

    df["f_" + col] = df[col].fillna(0)


def build_one_hot_encoding_feature(df, col, values=None):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(col, str))
    assert (values is None or isinstance(values, list)), "This should be a list: {0}".format(values)

    if "NULL" not in values:
        values = values + ["NULL"]

    tempCol = "f_" + col
    df[tempCol] = df[col].fillna("NULL")  # create temporary column to fill na values
    real_values = df[tempCol].values
    assert (values is None or set(real_values).issubset(set(values))), "First set should be a subset of the second:\n{0}\n{1}".format(set(real_values), set(values))

    temp = pandas_helper.get_one_hot_encoding(df, tempCol)
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


def build_percentage_feature(df, col):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(col, str))

    f_col = "f_" + col
    df[f_col] = df[col].str.strip("%").astype(float)/100
    df[f_col] = df[f_col].fillna(df[f_col].mean())


def build_date_feature(df, col):
    assert(isinstance(df, pd.DataFrame))
    assert(isinstance(col, str))


    month_col = col + "_month"  # create temporary column to parse month name
    df[month_col] = pd.to_datetime(df[col]).dt.strftime('%b').replace("NaT", "NULL")  # handle nan dates in df[col]
    build_one_hot_encoding_feature(df, month_col, values=definitions.months)
    df.drop(month_col, axis=1, inplace=True)  # drop temporary column

    f_diff = "f_{0}_diff".format(col)
    today = datetime.today()
    df[f_diff] = (today - pd.to_datetime(df[col]))/np.timedelta64(1, "D")
    df[f_diff] = df[f_diff].fillna(0)  # if want to fill with mean, check if mean is not nan


def build_features_by_columns(df, feature_columns):
    for col in feature_columns:
        if col["feature"]["type"] == "numeric":
            build_numeric_feature(df, col["name"])
        elif col["feature"]["type"] == "one-hot encoding":
            build_one_hot_encoding_feature(df, col["name"], col["feature"]["values"])
        else:
            raise Exception("Unsuported feature_type: {}".format(col["feature"]["type"]))

