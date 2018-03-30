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
    df["f_all_util"] = df["all_util"].fillna(0)
    df["f_annual_inc"] = df["annual_inc"].fillna(0)
    df["f_annual_inc_joint"] = df["annual_inc_joint"].fillna(0)
    # TODO: application_type -- one hot encoding of ['Individual' 'Joint App']
    df["f_avg_cur_bal"] = df["avg_cur_bal"].fillna(0)
    df["f_bc_open_to_buy"] = df["bc_open_to_buy"].fillna(0)
    df["f_bc_util"] = df["bc_util"].fillna(0)
    df["f_chargeoff_within_12_mths"] = df["chargeoff_within_12_mths"].fillna(0)
    df["f_collection_recovery_fee"] = df["collection_recovery_fee"]
    df["f_collections_12_mths_ex_med"] = df["collections_12_mths_ex_med"].fillna(0)
    df["f_delinq_2yrs"] = df["delinq_2yrs"].fillna(0)
    df["f_delinq_amnt"] = df["delinq_amnt"].fillna(0)
    # TODO: desc -- use NLP?
    df["f_dti"] = df["dti"].fillna(0)
    df["f_dti_joint"] = df["dti_joint"].fillna(0)
    # TODO: earliest_cr_line -- parse date, format Dec-1994, or better calculate diff(this, today)??
    # TODO: emp_length -- one hot encoding of ['10+ years', '< 1 year', '1 year', '3 years', '8 years', '9 years', '4 years', '5 years', '6 years', '2 years', '7 years', 'n/a']
    # TODO: emp_title -- one hot encoding or NLP??
    df["f_fico_range_high"] = df["fico_range_high"]
    df["f_fico_range_low"] = df["fico_range_low"]
    df["f_funded_amnt"] = df["funded_amnt"]
    df["f_funded_amnt_inv"] = df["funded_amnt_inv"]
    # TODO: grade -- one hot encoding of ['B', 'C', 'A', 'E', 'F', 'D', 'G']
    # TODO: home_ownership -- one hot encoding of ['RENT', 'OWN', 'MORTGAGE', 'OTHER', 'NONE']
    # TODO: id -- don't need this for real model, maybe add to test for noise
    df["f_il_util"] = df["il_util"].fillna(0)
    # TODO: initial_list_status -- one hot encoding of ['f' 'w']
    df["f_inq_fi"] = df["inq_fi"].fillna(0)
    df["f_inq_fi"] = df["inq_fi"].fillna(0)
    df["f_inq_last_12m"] = df["inq_last_12m"].fillna(0)
    df["f_inq_last_6mths"] = df["inq_last_6mths"].fillna(0)
    df["f_installment"] = df["installment"]
    df["f_int_rate"] = df["int_rate"].apply(lambda val : np.float64(val.strip(" %")))
    # TODO: issue_d -- date in this format: Sep-2010
    # TODO: last_credit_pull_d , date in this format: Sep-2010 or diff(this, today)
    df["f_last_fico_range_high"] = df["last_fico_range_high"]
    df["f_last_fico_range_low"] = df["last_fico_range_low"]
    df["f_last_pymnt_amnt"] = df["last_pymnt_amnt"]
    # TODO: last_pymnt_d -- parse date format 'Jan-2015' or calculate diff(this, today)??
    df["f_loan_amnt"] = df["loan_amnt"]
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



    df["f_max_bal_bc"] = df["max_bal_bc"].fillna(0)
    # TODO: member_id -- looks like always empty, check in all dataSets
    # df["f_mo_sin_old_il_acct"] = df["mo_sin_old_il_acct"].fillna(0)
    # df["f_mo_sin_old_rev_tl_op"] = df["mo_sin_old_rev_tl_op"]
    # df["f_mo_sin_rcnt_rev_tl_op"] = df["mo_sin_rcnt_rev_tl_op"]
    # df["f_mo_sin_rcnt_tl"] = df["mo_sin_rcnt_tl"]
    df["f_mort_acc"] = df["mort_acc"].fillna(0)
    # df["f_mths_since_last_delinq"] = df["mths_since_last_delinq"]
    # df["f_mths_since_last_major_derog"] = df["mths_since_last_major_derog"]
    # df["f_mths_since_last_record"] = df["mths_since_last_record"]
    # df["f_mths_since_rcnt_il"] = df["mths_since_rcnt_il"]
    # df["f_mths_since_recent_bc"] = df["mths_since_recent_bc"]
    # df["f_mths_since_recent_bc_dlq"] = df["mths_since_recent_bc_dlq"]
    # df["f_mths_since_recent_inq"] = df["mths_since_recent_inq"]
    # df["f_mths_since_recent_revol_delinq"] = df["mths_since_recent_revol_delinq"]
    # TODO: next_pymnt_d -- parse date format 'Jan-2016' or diff(this, today)?
    df["f_num_accts_ever_120_pd"] = df["num_accts_ever_120_pd"].fillna(0)
    df["f_num_actv_bc_tl"] = df["num_actv_bc_tl"].fillna(0)
    df["f_num_actv_rev_tl"] = df["num_actv_rev_tl"].fillna(0)
    df["f_num_bc_sats"] = df["num_bc_sats"].fillna(0)
    df["f_num_bc_tl"] = df["num_bc_tl"].fillna(0)
    df["f_num_il_tl"] = df["num_il_tl"].fillna(0)
    df["f_num_op_rev_tl"] = df["num_op_rev_tl"].fillna(0)
    df["f_num_rev_accts"] = df["num_rev_accts"].fillna(0)
    df["f_num_rev_tl_bal_gt_0"] = df["num_rev_tl_bal_gt_0"].fillna(0)
    df["f_num_sats"] = df["num_sats"].fillna(0)
    df["f_num_tl_120dpd_2m"] = df["num_tl_120dpd_2m"].fillna(0)
    df["f_num_tl_30dpd"] = df["num_tl_30dpd"].fillna(0)
    df["f_num_tl_90g_dpd_24m"] = df["num_tl_90g_dpd_24m"].fillna(0)
    df["f_num_tl_op_past_12m"] = df["num_tl_op_past_12m"].fillna(0)
    df["f_open_acc"] = df["open_acc"].fillna(0)
    df["f_open_acc_6m"] = df["open_acc_6m"].fillna(0)
    df["f_open_il_12m"] = df["open_il_12m"].fillna(0)
    df["f_open_il_24m"] = df["open_il_24m"].fillna(0)
    df["f_open_act_il"] = df["open_act_il"].fillna(0)
    df["f_open_rv_12m"] = df["open_rv_12m"].fillna(0)
    df["f_open_rv_24m"] = df["open_rv_24m"].fillna(0)
    df["f_out_prncp"] = df["out_prncp"].fillna(0)
    df["f_out_prncp_inv"] = df["out_prncp_inv"].fillna(0)
    df["f_pct_tl_nvr_dlq"] = df["pct_tl_nvr_dlq"].fillna(0)
    df["f_percent_bc_gt_75"] = df["percent_bc_gt_75"].fillna(0)
    # TODO: policy_code -- one hot encoding -- publicly available policy_code=1, new products not publicly available policy_code=2
    df["f_pub_rec"] = df["pub_rec"].fillna(0)
    df["f_pub_rec_bankruptcies"] = df["pub_rec_bankruptcies"].fillna(0)
    # TODO: purpose --     one hot encoding of
    """
    ['credit_card', 'car', 'small_business', 'other', 'wedding',
       'debt_consolidation', 'home_improvement', 'major_purchase',
       'medical', 'moving', 'vacation', 'house', 'renewable_energy',
       'educational']
    """
    # TODO: pymnt_plan -- always ['n'] for df3a
    df["f_recoveries"] = df["recoveries"].fillna(0)
    df["f_revol_bal"] = df["revol_bal"].fillna(0)
    # TODO: revol_util -- parse correctly
    # TODO: sub_grade -- one hot encoding of
    """
    one hot encoding of ['B2', 'C4', 'C5', 'C1', 'B5', 'A4', 'E1', 'F2', 'C3', 'B1', 'D1',
       'A1', 'B3', 'B4', 'C2', 'D2', 'A3', 'A5', 'D5', 'A2', 'E4', 'D3',
       'D4', 'F3', 'E3', 'F4', 'F1', 'E5', 'G4', 'E2', 'G3', 'G2', 'G1',
       'F5', 'G5']
    """
    df["f_tax_liens"] = df["tax_liens"].fillna(0)
    # TODO: term -- one hot encoding of  ' 36 months', ' 60 months'
    # TODO: title -- nlp?
    df["f_tot_coll_amt"] = df["tot_coll_amt"].fillna(0)
    df["f_tot_cur_bal"] = df["tot_cur_bal"].fillna(0)
    df["f_tot_hi_cred_lim"] = df["tot_hi_cred_lim"].fillna(0)
    df["f_total_acc"] = df["total_acc"].fillna(0)
    df["f_total_bal_ex_mort"] = df["total_bal_ex_mort"].fillna(0)
    df["f_total_bal_il"] = df["total_bal_il"].fillna(0)
    df["f_total_bc_limit"] = df["total_bc_limit"].fillna(0)
    df["f_total_cu_tl"] = df["total_cu_tl"].fillna(0)
    df["f_total_il_high_credit_limit"] = df["total_il_high_credit_limit"].fillna(0)
    df["f_total_pymnt"] = df["total_pymnt"].fillna(0)
    df["f_total_pymnt_inv"] = df["total_pymnt_inv"].fillna(0)
    df["f_total_rec_int"] = df["total_rec_int"].fillna(0)
    df["f_total_rec_late_fee"] = df["total_rec_late_fee"].fillna(0)
    df["f_total_rec_prncp"] = df["total_rec_prncp"].fillna(0)
    df["f_total_rev_hi_lim"] = df["total_rev_hi_lim"].fillna(0)
    # TODO: url -- check probably always https://lendingclub.com/browse/loanDetail.action?loan_id=<id>
    # TODO: verification_status -- one hot encoding of ['Verified', 'Source Verified', 'Not Verified']
    # TODO: verified_status_joint -- probably same as above
    # TODO: zip_code -- format 309xx; one hot encoding?
    df["f_revol_bal_joint"] = df["revol_bal_joint"].fillna(0)
    # df["f_sec_app_fico_range_low"] = df["sec_app_fico_range_low"].fillna(0)
    # df["f_sec_app_fico_range_high"] = df["sec_app_fico_range_high"].fillna(0)
    # df["f_sec_app_earliest_cr_line"] = df["sec_app_earliest_cr_line"]
    # df["f_sec_app_inq_last_6mths"] = df["sec_app_inq_last_6mths"]
    # df["f_sec_app_mort_acc"] = df["sec_app_mort_acc"]
    # df["f_sec_app_open_acc"] = df["sec_app_open_acc"]
    # df["f_sec_app_revol_util"] = df["sec_app_revol_util"]
    # df["f_sec_app_open_act_il"] = df["sec_app_open_act_il"]
    # df["f_sec_app_num_rev_accts"] = df["sec_app_num_rev_accts"]
    # df["f_sec_app_chargeoff_within_12_mths"] = df["sec_app_chargeoff_within_12_mths"]
    # df["f_sec_app_collections_12_mths_ex_med"] = df["sec_app_collections_12_mths_ex_med"]
    # df["f_sec_app_mths_since_last_major_derog"] = df["sec_app_mths_since_last_major_derog"]
    # TODO: hardship_flag -- check always ['N']
    # TODO: hardship_type -- check what is this?
    # TODO: hardship_reason -- check what is this?
    # TODO: hardship_status -- check what is this?
    # TODO: deferral_term -- check what is this?
    df["f_hardship_amount"] = df["hardship_amount"].fillna(0)
    # TODO: hardship_start_date -- check what is this?
    # TODO: hardship_end_date -- check what is this?
    # TODO: payment_plan_start_date -- check what is this?
    # TODO:hardship_length -- check what is this?
    # TODO: hardship_dpd -- check what is this?
    # TODO: hardship_loan_status -- check what is this?
    df["f_orig_projected_additional_accrued_interest"] = df["orig_projected_additional_accrued_interest"].fillna(0)
    df["f_hardship_payoff_balance_amount"] = df["hardship_payoff_balance_amount"].fillna(0)
    df["f_hardship_last_payment_amount"] = df["hardship_last_payment_amount"].fillna(0)
    # TODO: disbursement_method -- check always ['Cash']
    # TODO: debt_settlement_flag -- one hot encoding of ['N', 'Y']
    # TODO: debt_settlement_flag_date -- parse date format 'Mar-2013' or diff(this, today)??
    # TODO: settlement_status -- one hot encoding of [nan, 'COMPLETE', 'BROKEN', 'ACTIVE']
    # TODO: settlement_date -- parse date format 'Mar-2013' or diff(this, today)??
    df["f_settlement_amount"] = df["settlement_amount"].fillna(0)
    df["f_settlement_percentage"] = df["settlement_percentage"].fillna(0)
    df["f_settlement_term"] = df["settlement_term"].fillna(0)


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

