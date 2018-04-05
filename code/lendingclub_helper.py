import numpy as np
import pandas as pd
from sklearn.svm import SVC

import columns
import pandas_helper


def getFinishedLoans(df):
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
    buildOneHotEncodingFeature(df, "application_type")  # ['Individual' 'Joint App']
    buildNumericFeature(df, "avg_cur_bal")
    buildNumericFeature(df, "bc_open_to_buy")
    buildNumericFeature(df, "bc_util")
    buildNumericFeature(df, "chargeoff_within_12_mths")
    buildNumericFeature(df, "collection_recovery_fee")
    buildNumericFeature(df, "collections_12_mths_ex_med")
    buildNumericFeature(df, "delinq_2yrs")
    buildNumericFeature(df, "delinq_amnt")
    # TODO: desc -- use NLP?
    buildNumericFeature(df, "dti")
    buildNumericFeature(df, "dti_joint")
    # TODO: earliest_cr_line -- parse date, format Dec-1994, or better calculate diff(this, today)??
    # TODO: emp_length -- one hot encoding of ['10+ years', '< 1 year', '1 year', '3 years', '8 years', '9 years', '4 years', '5 years', '6 years', '2 years', '7 years', 'n/a']
    # TODO: emp_title -- NLP -- data is pretty random
    buildNumericFeature(df, "fico_range_high")
    buildNumericFeature(df, "fico_range_low")
    buildNumericFeature(df, "funded_amnt")
    buildNumericFeature(df, "funded_amnt_inv")
    buildOneHotEncodingFeature(df, "grade")
    buildOneHotEncodingFeature(df, "home_ownership")  # ['NONE', 'OWN', 'RENT', 'ANY', 'OTHER', 'MORTGAGE']
    # TODO: id -- don't need this for real model, maybe add to test for noise
    buildNumericFeature(df, "il_util")
    buildOneHotEncodingFeature(df, "initial_list_status")
    buildNumericFeature(df, "inq_fi")
    buildNumericFeature(df, "inq_last_12m")
    buildNumericFeature(df, "inq_last_6mths")
    buildNumericFeature(df, "installment")
    df["f_int_rate"] = df["int_rate"].apply(lambda val : np.float64(val.strip(" %")))
    # TODO: issue_d -- date in this format: Sep-2010
    # TODO: last_credit_pull_d , date in this format: Sep-2010 or diff(this, today)
    buildNumericFeature(df, "last_fico_range_high")
    buildNumericFeature(df, "last_fico_range_low")
    buildNumericFeature(df, "last_pymnt_amnt")
    # TODO: last_pymnt_d -- parse date format 'Jan-2015' or calculate diff(this, today)??
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
    # TODO: member_id -- looks like always empty, check in all dataSets
    # df["f_mo_sin_old_il_acct"] = df["mo_sin_old_il_acct"].fillna(0)
    # df["f_mo_sin_old_rev_tl_op"] = df["mo_sin_old_rev_tl_op"]
    # df["f_mo_sin_rcnt_rev_tl_op"] = df["mo_sin_rcnt_rev_tl_op"]
    # df["f_mo_sin_rcnt_tl"] = df["mo_sin_rcnt_tl"]
    buildNumericFeature(df, "mort_acc")
    # df["f_mths_since_last_delinq"] = df["mths_since_last_delinq"]
    # df["f_mths_since_last_major_derog"] = df["mths_since_last_major_derog"]
    # df["f_mths_since_last_record"] = df["mths_since_last_record"]
    # df["f_mths_since_rcnt_il"] = df["mths_since_rcnt_il"]
    # df["f_mths_since_recent_bc"] = df["mths_since_recent_bc"]
    # df["f_mths_since_recent_bc_dlq"] = df["mths_since_recent_bc_dlq"]
    # df["f_mths_since_recent_inq"] = df["mths_since_recent_inq"]
    # df["f_mths_since_recent_revol_delinq"] = df["mths_since_recent_revol_delinq"]
    # TODO: next_pymnt_d -- parse date format 'Jan-2016' or diff(this, today)?
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
    # TODO: pymnt_plan -- always ['n'] for df3a
    df["f_recoveries"] = df["recoveries"].fillna(0)
    df["f_revol_bal"] = df["revol_bal"].fillna(0)
    # TODO: revol_util -- parse correctly
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
    # df["f_sec_app_earliest_cr_line"] = df["sec_app_earliest_cr_line"]  # TODO: -- parse date
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
    buildOneHotEncodingFeature(df, "hardship_type")  # one-hot encode nan
    buildOneHotEncodingFeature(df, "hardship_reason")  # one-hot encode nan
    buildOneHotEncodingFeature(df, "hardship_status")  # one-hot encode nan
    buildNumericFeature(df, "deferral_term")
    buildNumericFeature(df, "hardship_amount")
    # TODO: hardship_start_date  # TODO: -- parse date
    # TODO: hardship_end_date  # TODO: -- parse date
    # TODO: payment_plan_start_date  # TODO: -- parse date
    buildNumericFeature(df, "hardship_length")
    buildNumericFeature(df, "hardship_dpd")
    buildOneHotEncodingFeature(df, "hardship_loan_status")
    buildNumericFeature(df, "orig_projected_additional_accrued_interest")
    buildNumericFeature(df, "hardship_payoff_balance_amount")
    buildNumericFeature(df, "hardship_last_payment_amount")
    buildOneHotEncodingFeature(df, "disbursement_method")
    buildOneHotEncodingFeature(df, "debt_settlement_flag")
    # TODO: debt_settlement_flag_date -- parse date format 'Mar-2013' or diff(this, today)??
    buildOneHotEncodingFeature(df, "settlement_status")
    # TODO: settlement_date -- parse date format 'Mar-2013' or diff(this, today)??
    buildNumericFeature(df, "settlement_amount")
    buildNumericFeature(df, "settlement_percentage")
    buildNumericFeature(df, "settlement_term")


def getFeatureColumns(df):
    assert(isinstance(df, pd.DataFrame))

    return pandas_helper.getColumnsByPrefix(df, "f_")


def buildLabels(df):
    df["l_loan_status"] = df["loan_status"].apply(columns.parse_loan_status)


def getLabelColumns(df):
    assert(isinstance(df, pd.DataFrame))

    return pandas_helper.getColumnsByPrefix(df, "l_")





def buildNumericFeature(df, col):
    # TODO: normalize
    # TODO: consider filling na with mean instead of 0
    df["f_" + col] = df[col].fillna(0)
    


def buildOneHotEncodingFeature(df, col):
    temp = pandas_helper.getOneHotEncoding(df, col)
    for c in temp.columns:
        df["f_" + c] = temp[c]

