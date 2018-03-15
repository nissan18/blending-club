def parse_acc_now_delinq(value):
    pass
def parse_acc_open_past_24mths(value):
    pass
def parse_addr_state(value):
    """
    one hot encoding of
    ['AZ', 'GA', 'IL', 'CA', 'OR', 'NC', 'TX', 'VA', 'MO', 'CT', 'UT',
       'FL', 'NY', 'PA', 'MN', 'NJ', 'KY', 'OH', 'SC', 'RI', 'LA', 'MA',
       'WA', 'WI', 'AL', 'CO', 'KS', 'NV', 'AK', 'MD', 'WV', 'VT', 'MI',
       'DC', 'SD', 'NH', 'AR', 'NM', 'MT', 'HI', 'WY', 'OK', 'DE', 'MS',
       'TN', 'IA', 'NE', 'ID', 'IN', 'ME']
    """
    pass
def parse_all_util(value):
    pass
def parse_annual_inc(value):
    pass
def parse_annual_inc_joint(value):
    pass
def parse_application_type(value):
    # TODO: always ['Individual']
    pass
def parse_avg_cur_bal(value):
    pass
def parse_bc_open_to_buy(value):
    pass
def parse_bc_util(value):
    pass
def parse_chargeoff_within_12_mths(value):
    pass
def parse_collection_recovery_fee(value):
    pass
def parse_collections_12_mths_ex_med(value):
    pass
def parse_delinq_2yrs(value):
    pass
def parse_delinq_amnt(value):
    pass
def parse_desc(value):
    # TODO: nlp?
    pass
def parse_dti(value):
    pass
def parse_dti_joint(value):
    pass
def parse_earliest_cr_line(value):
    # TODO: parse data, format Dec-1994
    # or better calculate diff(this, today)??
    pass
def parse_emp_length(value):
    """
    one hot encoding of
    (['10+ years', '< 1 year', '1 year', '3 years', '8 years', '9 years',
       '4 years', '5 years', '6 years', '2 years', '7 years', 'n/a']
    """
    pass
def parse_emp_title(value):
    # probably not necessary now: also can do one hot encoding
    pass
def parse_fico_range_high(value):
    pass
def parse_fico_range_low(value):
    pass
def parse_funded_amnt(value):
    pass
def parse_funded_amnt_inv(value):
    pass
def parse_grade(value):
    # TODO: one hot encoding of ['B', 'C', 'A', 'E', 'F', 'D', 'G']
    pass
def parse_home_ownership(value):
    # TODO: one hot encoding of ['RENT', 'OWN', 'MORTGAGE', 'OTHER', 'NONE']
    pass
def parse_id(value):
    pass
def parse_il_util(value):
    pass
def parse_initial_list_status(value):
    # TODO: always ['f']
    pass
def parse_inq_fi(value):
    pass
def parse_inq_last_12m(value):
    pass
def parse_inq_last_6mths(value):
    pass
def parse_installment(value):
    pass
def parse_int_rate(value):
    return float(value.strip(" %"))
def parse_issue_d(value):
    # TODO: data in this format: Sep-2010
    pass
def parse_last_credit_pull_d(value):
    # TODO: data in this format: Sep-2010 or diff(this, today)
    pass
def parse_last_fico_range_high(value):
    pass
def parse_last_fico_range_low(value):
    pass
def parse_last_pymnt_amnt(value):
    pass
def parse_last_pymnt_d(value):
    # TODO: parse date format 'Jan-2015' or calculate diff(this, today)??
    pass
def parse_loan_amnt(value):
    pass
def parse_loan_status(value):
    """
    one hot encoding of
    ['Fully Paid', 'Charged Off',
       'Does not meet the credit policy. Status:Fully Paid',
       'Does not meet the credit policy. Status:Charged Off']
    """
    pass
def parse_max_bal_bc(value):
    pass
def parse_member_id(value):
    pass
def parse_mo_sin_old_il_acct(value):
    pass
def parse_mo_sin_old_rev_tl_op(value):
    pass
def parse_mo_sin_rcnt_rev_tl_op(value):
    pass
def parse_mo_sin_rcnt_tl(value):
    pass
def parse_mort_acc(value):
    pass
def parse_mths_since_last_delinq(value):
    pass
def parse_mths_since_last_major_derog(value):
    pass
def parse_mths_since_last_record(value):
    pass
def parse_mths_since_rcnt_il(value):
    pass
def parse_mths_since_recent_bc(value):
    pass
def parse_mths_since_recent_bc_dlq(value):
    pass
def parse_mths_since_recent_inq(value):
    pass
def parse_mths_since_recent_revol_delinq(value):
    pass
def parse_next_pymnt_d(value):
    # TODO: parse data format 'Jan-2016' or diff(this, today)?
    pass
def parse_num_accts_ever_120_pd(value):
    pass
def parse_num_actv_bc_tl(value):
    pass
def parse_num_actv_rev_tl(value):
    pass
def parse_num_bc_sats(value):
    pass
def parse_num_bc_tl(value):
    pass
def parse_num_il_tl(value):
    pass
def parse_num_op_rev_tl(value):
    pass
def parse_num_rev_accts(value):
    pass
def parse_num_rev_tl_bal_gt_0(value):
    pass
def parse_num_sats(value):
    pass
def parse_num_tl_120dpd_2m(value):
    pass
def parse_num_tl_30dpd(value):
    pass
def parse_num_tl_90g_dpd_24m(value):
    pass
def parse_num_tl_op_past_12m(value):
    pass
def parse_open_acc(value):
    pass
def parse_open_acc_6m(value):
    pass
def parse_open_il_12m(value):
    pass
def parse_open_il_24m(value):
    pass
def parse_open_act_il(value):
    pass
def parse_open_rv_12m(value):
    pass
def parse_open_rv_24m(value):
    pass
def parse_out_prncp(value):
    pass
def parse_out_prncp_inv(value):
    pass
def parse_pct_tl_nvr_dlq(value):
    pass
def parse_percent_bc_gt_75(value):
    pass
def parse_policy_code(value):
    pass
def parse_pub_rec(value):
    pass
def parse_pub_rec_bankruptcies(value):
    pass
def parse_purpose(value):
    """
    one hot encoding of
    ['credit_card', 'car', 'small_business', 'other', 'wedding',
       'debt_consolidation', 'home_improvement', 'major_purchase',
       'medical', 'moving', 'vacation', 'house', 'renewable_energy',
       'educational']
    """
    pass
def parse_pymnt_plan(value):
    # TODO: always ['n'] for df3a
    pass
def parse_recoveries(value):
    pass
def parse_revol_bal(value):
    pass
def parse_revol_util(value):
    return float(value.strip(" %"))
def parse_sub_grade(value):
    """
    one hot encoding of ['B2', 'C4', 'C5', 'C1', 'B5', 'A4', 'E1', 'F2', 'C3', 'B1', 'D1',
       'A1', 'B3', 'B4', 'C2', 'D2', 'A3', 'A5', 'D5', 'A2', 'E4', 'D3',
       'D4', 'F3', 'E3', 'F4', 'F1', 'E5', 'G4', 'E2', 'G3', 'G2', 'G1',
       'F5', 'G5']
    """
    pass
def parse_tax_liens(value):
    pass
def parse_term(value):
    conversion = {
        ' 36 months': 36,
        ' 60 months': 60
    }
    return conversion[value]

def parse_title(value):
    # TODO: nlp?
    pass
def parse_tot_coll_amt(value):
    pass
def parse_tot_cur_bal(value):
    pass
def parse_tot_hi_cred_lim(value):
    pass
def parse_total_acc(value):
    pass
def parse_total_bal_ex_mort(value):
    pass
def parse_total_bal_il(value):
    pass
def parse_total_bc_limit(value):
    pass
def parse_total_cu_tl(value):
    pass
def parse_total_il_high_credit_limit(value):
    pass
def parse_total_pymnt(value):
    pass
def parse_total_pymnt_inv(value):
    pass
def parse_total_rec_int(value):
    pass
def parse_total_rec_late_fee(value):
    pass
def parse_total_rec_prncp(value):
    pass
def parse_total_rev_hi_lim(value):
    pass
def parse_url(value):
    # TODO: probably always https://lendingclub.com/browse/loanDetail.action?loan_id=<id>
    pass
def parse_verification_status(value):
    # TODO: one hot encoding of ['Verified', 'Source Verified', 'Not Verified']
    pass
def parse_verified_status_joint(value):
    pass
def parse_zip_code(value):
    # TODO: format 309xx; one hot encoding?
    pass
def parse_revol_bal_joint(value):
    pass
def parse_sec_app_fico_range_low(value):
    pass
def parse_sec_app_fico_range_high(value):
    pass
def parse_sec_app_earliest_cr_line(value):
    pass
def parse_sec_app_inq_last_6mths(value):
    pass
def parse_sec_app_mort_acc(value):
    pass
def parse_sec_app_open_acc(value):
    pass
def parse_sec_app_revol_util(value):
    pass
def parse_sec_app_open_act_il(value):
    pass
def parse_sec_app_num_rev_accts(value):
    pass
def parse_sec_app_chargeoff_within_12_mths(value):
    pass
def parse_sec_app_collections_12_mths_ex_med(value):
    pass
def parse_sec_app_mths_since_last_major_derog(value):
    pass
def parse_hardship_flag(value):
    # TODO: always ['N']
    pass
def parse_hardship_type(value):
    pass
def parse_hardship_reason(value):
    pass
def parse_hardship_status(value):
    pass
def parse_deferral_term(value):
    pass
def parse_hardship_amount(value):
    pass
def parse_hardship_start_date(value):
    pass
def parse_hardship_end_date(value):
    pass
def parse_payment_plan_start_date(value):
    pass
def parse_hardship_length(value):
    pass
def parse_hardship_dpd(value):
    pass
def parse_hardship_loan_status(value):
    pass
def parse_orig_projected_additional_accrued_interest(value):
    pass
def parse_hardship_payoff_balance_amount(value):
    pass
def parse_hardship_last_payment_amount(value):
    pass
def parse_disbursement_method(value):
    # TODO: always ['Cash']
    pass
def parse_debt_settlement_flag(value):
    # TODO: one hot encoding of ['N', 'Y']
    pass
def parse_debt_settlement_flag_date(value):
    # TODO: parse data format 'Mar-2013' or diff(this, today)??
    pass
def parse_settlement_status(value):
    # TODO: one hot encoding of [nan, 'COMPLETE', 'BROKEN', 'ACTIVE']
    pass
def parse_settlement_date(value):
    # TODO: parse data format 'Mar-2013' or diff(this, today)??
    pass
def parse_settlement_amount(value):
    pass
def parse_settlement_percentage(value):
    pass
def parse_settlement_term(value):
    pass

columns = {
    "acc_now_delinq": { "name": "acc_now_delinq", "description": "The number of accounts on which the borrower is now delinquent.", "parseFunction": parse_acc_now_delinq,},
    "acc_open_past_24mths": { "name": "acc_open_past_24mths", "description": "Number of trades opened in past 24 months.", "parseFunction": parse_acc_open_past_24mths,},
    "addr_state": { "name": "addr_state", "description": "The state provided by the borrower in the loan application", "parseFunction": parse_addr_state,},
    "all_util": { "name": "all_util", "description": "Balance to credit limit on all trades", "parseFunction": parse_all_util,},
    "annual_inc": { "name": "annual_inc", "description": "The self-reported annual income provided by the borrower during registration.", "parseFunction": parse_annual_inc,},
    "annual_inc_joint": { "name": "annual_inc_joint", "description": "The combined self-reported annual income provided by the co-borrowers during registration", "parseFunction": parse_annual_inc_joint,},
    "application_type": { "name": "application_type", "description": "Indicates whether the loan is an individual application or a joint application with two co-borrowers", "parseFunction": parse_application_type,},
    "avg_cur_bal": { "name": "avg_cur_bal", "description": "Average current balance of all accounts", "parseFunction": parse_avg_cur_bal,},
    "bc_open_to_buy": { "name": "bc_open_to_buy", "description": "Total open to buy on revolving bankcards.", "parseFunction": parse_bc_open_to_buy,},
    "bc_util": { "name": "bc_util", "description": "Ratio of total current balance to high credit/credit limit for all bankcard accounts.", "parseFunction": parse_bc_util,},
    "chargeoff_within_12_mths": { "name": "chargeoff_within_12_mths", "description": "Number of charge-offs within 12 months", "parseFunction": parse_chargeoff_within_12_mths,},
    "collection_recovery_fee": { "name": "collection_recovery_fee", "description": "post charge off collection fee", "parseFunction": parse_collection_recovery_fee,},
    "collections_12_mths_ex_med": { "name": "collections_12_mths_ex_med", "description": "Number of collections in 12 months excluding medical collections", "parseFunction": parse_collections_12_mths_ex_med,},
    "delinq_2yrs": { "name": "delinq_2yrs", "description": "The number of 30+ days past-due incidences of delinquency in the borrower's credit file for the past 2 years", "parseFunction": parse_delinq_2yrs,},
    "delinq_amnt": { "name": "delinq_amnt", "description": "The past-due amount owed for the accounts on which the borrower is now delinquent.", "parseFunction": parse_delinq_amnt,},
    "desc": { "name": "desc", "description": "Loan description provided by the borrower", "parseFunction": parse_desc,},
    "dti": { "name": "dti", "description": "A ratio calculated using the borrower’s total monthly debt payments on the total debt obligations, excluding mortgage and the requested LC loan, divided by the borrower’s self-reported monthly income.", "parseFunction": parse_dti,},
    "dti_joint": { "name": "dti_joint", "description": "A ratio calculated using the co-borrowers' total monthly payments on the total debt obligations, excluding mortgages and the requested LC loan, divided by the co-borrowers' combined self-reported monthly income", "parseFunction": parse_dti_joint,},
    "earliest_cr_line": { "name": "earliest_cr_line", "description": "The month the borrower's earliest reported credit line was opened", "parseFunction": parse_earliest_cr_line,},
    "emp_length": { "name": "emp_length", "description": "Employment length in years. Possible values are between 0 and 10 where 0 means less than one year and 10 means ten or more years.", "parseFunction": parse_emp_length,},
    "emp_title": { "name": "emp_title", "description": "The job title supplied by the Borrower when applying for the loan.*", "parseFunction": parse_emp_title,},
    "fico_range_high": { "name": "fico_range_high", "description": "The upper boundary range the borrower’s FICO at loan origination belongs to.", "parseFunction": parse_fico_range_high,},
    "fico_range_low": { "name": "fico_range_low", "description": "The lower boundary range the borrower’s FICO at loan origination belongs to.", "parseFunction": parse_fico_range_low,},
    "funded_amnt": { "name": "funded_amnt", "description": "The total amount committed to that loan at that point in time.", "parseFunction": parse_funded_amnt,},
    "funded_amnt_inv": { "name": "funded_amnt_inv", "description": "The total amount committed by investors for that loan at that point in time.", "parseFunction": parse_funded_amnt_inv,},
    "grade": { "name": "grade", "description": "LC assigned loan grade", "parseFunction": parse_grade,},
    "home_ownership": { "name": "home_ownership", "description": "The home ownership status provided by the borrower during registration or obtained from the credit report. Our values are: RENT, OWN, MORTGAGE, OTHER", "parseFunction": parse_home_ownership,},
    "id": { "name": "id", "description": "A unique LC assigned ID for the loan listing.", "parseFunction": parse_id,},
    "il_util": { "name": "il_util", "description": "Ratio of total current balance to high credit/credit limit on all install acct", "parseFunction": parse_il_util,},
    "initial_list_status": { "name": "initial_list_status", "description": "The initial listing status of the loan. Possible values are – W, F", "parseFunction": parse_initial_list_status,},
    "inq_fi": { "name": "inq_fi", "description": "Number of personal finance inquiries", "parseFunction": parse_inq_fi,},
    "inq_last_12m": { "name": "inq_last_12m", "description": "Number of credit inquiries in past 12 months", "parseFunction": parse_inq_last_12m,},
    "inq_last_6mths": { "name": "inq_last_6mths", "description": "The number of inquiries in past 6 months (excluding auto and mortgage inquiries)", "parseFunction": parse_inq_last_6mths,},
    "installment": { "name": "installment", "description": "The monthly payment owed by the borrower if the loan originates.", "parseFunction": parse_installment,},
    "int_rate": { "name": "int_rate", "description": "Interest Rate on the loan", "parseFunction": parse_int_rate,},
    "issue_d": { "name": "issue_d", "description": "The month which the loan was funded", "parseFunction": parse_issue_d,},
    "last_credit_pull_d": { "name": "last_credit_pull_d", "description": "The most recent month LC pulled credit for this loan", "parseFunction": parse_last_credit_pull_d,},
    "last_fico_range_high": { "name": "last_fico_range_high", "description": "The upper boundary range the borrower’s last FICO pulled belongs to.", "parseFunction": parse_last_fico_range_high,},
    "last_fico_range_low": { "name": "last_fico_range_low", "description": "The lower boundary range the borrower’s last FICO pulled belongs to.", "parseFunction": parse_last_fico_range_low,},
    "last_pymnt_amnt": { "name": "last_pymnt_amnt", "description": "Last total payment amount received", "parseFunction": parse_last_pymnt_amnt,},
    "last_pymnt_d": { "name": "last_pymnt_d", "description": "Last month payment was received", "parseFunction": parse_last_pymnt_d,},
    "loan_amnt": { "name": "loan_amnt", "description": "The listed amount of the loan applied for by the borrower. If at some point in time, the credit department reduces the loan amount, then it will be reflected in this value.", "parseFunction": parse_loan_amnt,},
    "loan_status": { "name": "loan_status", "description": "Current status of the loan", "parseFunction": parse_loan_status,},
    "max_bal_bc": { "name": "max_bal_bc", "description": "Maximum current balance owed on all revolving accounts", "parseFunction": parse_max_bal_bc,},
    "member_id": { "name": "member_id", "description": "A unique LC assigned Id for the borrower member.", "parseFunction": parse_member_id,},
    "mo_sin_old_il_acct": { "name": "mo_sin_old_il_acct", "description": "Months since oldest bank installment account opened", "parseFunction": parse_mo_sin_old_il_acct,},
    "mo_sin_old_rev_tl_op": { "name": "mo_sin_old_rev_tl_op", "description": "Months since oldest revolving account opened", "parseFunction": parse_mo_sin_old_rev_tl_op,},
    "mo_sin_rcnt_rev_tl_op": { "name": "mo_sin_rcnt_rev_tl_op", "description": "Months since most recent revolving account opened", "parseFunction": parse_mo_sin_rcnt_rev_tl_op,},
    "mo_sin_rcnt_tl": { "name": "mo_sin_rcnt_tl", "description": "Months since most recent account opened", "parseFunction": parse_mo_sin_rcnt_tl,},
    "mort_acc": { "name": "mort_acc", "description": "Number of mortgage accounts.", "parseFunction": parse_mort_acc,},
    "mths_since_last_delinq": { "name": "mths_since_last_delinq", "description": "The number of months since the borrower's last delinquency.", "parseFunction": parse_mths_since_last_delinq,},
    "mths_since_last_major_derog": { "name": "mths_since_last_major_derog", "description": "Months since most recent 90-day or worse rating", "parseFunction": parse_mths_since_last_major_derog,},
    "mths_since_last_record": { "name": "mths_since_last_record", "description": "The number of months since the last public record.", "parseFunction": parse_mths_since_last_record,},
    "mths_since_rcnt_il": { "name": "mths_since_rcnt_il", "description": "Months since most recent installment accounts opened", "parseFunction": parse_mths_since_rcnt_il,},
    "mths_since_recent_bc": { "name": "mths_since_recent_bc", "description": "Months since most recent bankcard account opened.", "parseFunction": parse_mths_since_recent_bc,},
    "mths_since_recent_bc_dlq": { "name": "mths_since_recent_bc_dlq", "description": "Months since most recent bankcard delinquency", "parseFunction": parse_mths_since_recent_bc_dlq,},
    "mths_since_recent_inq": { "name": "mths_since_recent_inq", "description": "Months since most recent inquiry.", "parseFunction": parse_mths_since_recent_inq,},
    "mths_since_recent_revol_delinq": { "name": "mths_since_recent_revol_delinq", "description": "Months since most recent revolving delinquency.", "parseFunction": parse_mths_since_recent_revol_delinq,},
    "next_pymnt_d": { "name": "next_pymnt_d", "description": "Next scheduled payment date", "parseFunction": parse_next_pymnt_d,},
    "num_accts_ever_120_pd": { "name": "num_accts_ever_120_pd", "description": "Number of accounts ever 120 or more days past due", "parseFunction": parse_num_accts_ever_120_pd,},
    "num_actv_bc_tl": { "name": "num_actv_bc_tl", "description": "Number of currently active bankcard accounts", "parseFunction": parse_num_actv_bc_tl,},
    "num_actv_rev_tl": { "name": "num_actv_rev_tl", "description": "Number of currently active revolving trades", "parseFunction": parse_num_actv_rev_tl,},
    "num_bc_sats": { "name": "num_bc_sats", "description": "Number of satisfactory bankcard accounts", "parseFunction": parse_num_bc_sats,},
    "num_bc_tl": { "name": "num_bc_tl", "description": "Number of bankcard accounts", "parseFunction": parse_num_bc_tl,},
    "num_il_tl": { "name": "num_il_tl", "description": "Number of installment accounts", "parseFunction": parse_num_il_tl,},
    "num_op_rev_tl": { "name": "num_op_rev_tl", "description": "Number of open revolving accounts", "parseFunction": parse_num_op_rev_tl,},
    "num_rev_accts": { "name": "num_rev_accts", "description": "Number of revolving accounts", "parseFunction": parse_num_rev_accts,},
    "num_rev_tl_bal_gt_0": { "name": "num_rev_tl_bal_gt_0", "description": "Number of revolving trades with balance >0", "parseFunction": parse_num_rev_tl_bal_gt_0,},
    "num_sats": { "name": "num_sats", "description": "Number of satisfactory accounts", "parseFunction": parse_num_sats,},
    "num_tl_120dpd_2m": { "name": "num_tl_120dpd_2m", "description": "Number of accounts currently 120 days past due (updated in past 2 months)", "parseFunction": parse_num_tl_120dpd_2m,},
    "num_tl_30dpd": { "name": "num_tl_30dpd", "description": "Number of accounts currently 30 days past due (updated in past 2 months)", "parseFunction": parse_num_tl_30dpd,},
    "num_tl_90g_dpd_24m": { "name": "num_tl_90g_dpd_24m", "description": "Number of accounts 90 or more days past due in last 24 months", "parseFunction": parse_num_tl_90g_dpd_24m,},
    "num_tl_op_past_12m": { "name": "num_tl_op_past_12m", "description": "Number of accounts opened in past 12 months", "parseFunction": parse_num_tl_op_past_12m,},
    "open_acc": { "name": "open_acc", "description": "The number of open credit lines in the borrower's credit file.", "parseFunction": parse_open_acc,},
    "open_acc_6m": { "name": "open_acc_6m", "description": "Number of open trades in last 6 months", "parseFunction": parse_open_acc_6m,},
    "open_il_12m": { "name": "open_il_12m", "description": "Number of installment accounts opened in past 12 months", "parseFunction": parse_open_il_12m,},
    "open_il_24m": { "name": "open_il_24m", "description": "Number of installment accounts opened in past 24 months", "parseFunction": parse_open_il_24m,},
    "open_act_il": { "name": "open_act_il", "description": "Number of currently active installment trades", "parseFunction": parse_open_act_il,},
    "open_rv_12m": { "name": "open_rv_12m", "description": "Number of revolving trades opened in past 12 months", "parseFunction": parse_open_rv_12m,},
    "open_rv_24m": { "name": "open_rv_24m", "description": "Number of revolving trades opened in past 24 months", "parseFunction": parse_open_rv_24m,},
    "out_prncp": { "name": "out_prncp", "description": "Remaining outstanding principal for total amount funded", "parseFunction": parse_out_prncp,},
    "out_prncp_inv": { "name": "out_prncp_inv", "description": "Remaining outstanding principal for portion of total amount funded by investors", "parseFunction": parse_out_prncp_inv,},
    "pct_tl_nvr_dlq": { "name": "pct_tl_nvr_dlq", "description": "Percent of trades never delinquent", "parseFunction": parse_pct_tl_nvr_dlq,},
    "percent_bc_gt_75": { "name": "percent_bc_gt_75", "description": "Percentage of all bankcard accounts > 75% of limit.", "parseFunction": parse_percent_bc_gt_75,},
    "policy_code": { "name": "policy_code", "description": "\"publicly available policy_code=1; new products not publicly available policy_code=2\"", "parseFunction": parse_policy_code,},
    "pub_rec": { "name": "pub_rec", "description": "Number of derogatory public records", "parseFunction": parse_pub_rec,},
    "pub_rec_bankruptcies": { "name": "pub_rec_bankruptcies", "description": "Number of public record bankruptcies", "parseFunction": parse_pub_rec_bankruptcies,},
    "purpose": { "name": "purpose", "description": "A category provided by the borrower for the loan request.", "parseFunction": parse_purpose,},
    "pymnt_plan": { "name": "pymnt_plan", "description": "Indicates if a payment plan has been put in place for the loan", "parseFunction": parse_pymnt_plan,},
    "recoveries": { "name": "recoveries", "description": "post charge off gross recovery", "parseFunction": parse_recoveries,},
    "revol_bal": { "name": "revol_bal", "description": "Total credit revolving balance", "parseFunction": parse_revol_bal,},
    "revol_util": { "name": "revol_util", "description": "Revolving line utilization rate, or the amount of credit the borrower is using relative to all available revolving credit.", "parseFunction": parse_revol_util,},
    "sub_grade": { "name": "sub_grade", "description": "LC assigned loan subgrade", "parseFunction": parse_sub_grade,},
    "tax_liens": { "name": "tax_liens", "description": "Number of tax liens", "parseFunction": parse_tax_liens,},
    "term": { "name": "term", "description": "The number of payments on the loan. Values are in months and can be either 36 or 60.", "parseFunction": parse_term,},
    "title": { "name": "title", "description": "The loan title provided by the borrower", "parseFunction": parse_title,},
    "tot_coll_amt": { "name": "tot_coll_amt", "description": "Total collection amounts ever owed", "parseFunction": parse_tot_coll_amt,},
    "tot_cur_bal": { "name": "tot_cur_bal", "description": "Total current balance of all accounts", "parseFunction": parse_tot_cur_bal,},
    "tot_hi_cred_lim": { "name": "tot_hi_cred_lim", "description": "Total high credit/credit limit", "parseFunction": parse_tot_hi_cred_lim,},
    "total_acc": { "name": "total_acc", "description": "The total number of credit lines currently in the borrower's credit file", "parseFunction": parse_total_acc,},
    "total_bal_ex_mort": { "name": "total_bal_ex_mort", "description": "Total credit balance excluding mortgage", "parseFunction": parse_total_bal_ex_mort,},
    "total_bal_il": { "name": "total_bal_il", "description": "Total current balance of all installment accounts", "parseFunction": parse_total_bal_il,},
    "total_bc_limit": { "name": "total_bc_limit", "description": "Total bankcard high credit/credit limit", "parseFunction": parse_total_bc_limit,},
    "total_cu_tl": { "name": "total_cu_tl", "description": "Number of finance trades", "parseFunction": parse_total_cu_tl,},
    "total_il_high_credit_limit": { "name": "total_il_high_credit_limit", "description": "Total installment high credit/credit limit", "parseFunction": parse_total_il_high_credit_limit,},
    "total_pymnt": { "name": "total_pymnt", "description": "Payments received to date for total amount funded", "parseFunction": parse_total_pymnt,},
    "total_pymnt_inv": { "name": "total_pymnt_inv", "description": "Payments received to date for portion of total amount funded by investors", "parseFunction": parse_total_pymnt_inv,},
    "total_rec_int": { "name": "total_rec_int", "description": "Interest received to date", "parseFunction": parse_total_rec_int,},
    "total_rec_late_fee": { "name": "total_rec_late_fee", "description": "Late fees received to date", "parseFunction": parse_total_rec_late_fee,},
    "total_rec_prncp": { "name": "total_rec_prncp", "description": "Principal received to date", "parseFunction": parse_total_rec_prncp,},
    "total_rev_hi_lim": { "name": "total_rev_hi_lim", "description": "Total revolving high credit/credit limit", "parseFunction": parse_total_rev_hi_lim,},
    "url": { "name": "url", "description": "URL for the LC page with listing data.", "parseFunction": parse_url,},
    "verification_status": { "name": "verification_status", "description": "Indicates if income was verified by LC, not verified, or if the income source was verified", "parseFunction": parse_verification_status,},
    "verified_status_joint": { "name": "verified_status_joint", "description": "Indicates if the co-borrowers' joint income was verified by LC, not verified, or if the income source was verified", "parseFunction": parse_verified_status_joint,},
    "zip_code": { "name": "zip_code", "description": "The first 3 numbers of the zip code provided by the borrower in the loan application.", "parseFunction": parse_zip_code,},
    "revol_bal_joint": { "name": "revol_bal_joint", "description": " Sum of revolving credit balance of the co-borrowers, net of duplicate balances", "parseFunction": parse_revol_bal_joint,},
    "sec_app_fico_range_low": { "name": "sec_app_fico_range_low", "description": " FICO range (high) for the secondary applicant", "parseFunction": parse_sec_app_fico_range_low,},
    "sec_app_fico_range_high": { "name": "sec_app_fico_range_high", "description": " FICO range (low) for the secondary applicant", "parseFunction": parse_sec_app_fico_range_high,},
    "sec_app_earliest_cr_line": { "name": "sec_app_earliest_cr_line", "description": " Earliest credit line at time of application for the secondary applicant", "parseFunction": parse_sec_app_earliest_cr_line,},
    "sec_app_inq_last_6mths": { "name": "sec_app_inq_last_6mths", "description": " Credit inquiries in the last 6 months at time of application for the secondary applicant", "parseFunction": parse_sec_app_inq_last_6mths,},
    "sec_app_mort_acc": { "name": "sec_app_mort_acc", "description": " Number of mortgage accounts at time of application for the secondary applicant", "parseFunction": parse_sec_app_mort_acc,},
    "sec_app_open_acc": { "name": "sec_app_open_acc", "description": " Number of open trades at time of application for the secondary applicant", "parseFunction": parse_sec_app_open_acc,},
    "sec_app_revol_util": { "name": "sec_app_revol_util", "description": " Ratio of total current balance to high credit/credit limit for all revolving accounts", "parseFunction": parse_sec_app_revol_util,},
    "sec_app_open_act_il": { "name": "sec_app_open_act_il", "description": " Number of currently active installment trades at time of application for the secondary applicant", "parseFunction": parse_sec_app_open_act_il,},
    "sec_app_num_rev_accts": { "name": "sec_app_num_rev_accts", "description": " Number of revolving accounts at time of application for the secondary applicant", "parseFunction": parse_sec_app_num_rev_accts,},
    "sec_app_chargeoff_within_12_mths": { "name": "sec_app_chargeoff_within_12_mths", "description": " Number of charge-offs within last 12 months at time of application for the secondary applicant", "parseFunction": parse_sec_app_chargeoff_within_12_mths,},
    "sec_app_collections_12_mths_ex_med": { "name": "sec_app_collections_12_mths_ex_med", "description": " Number of collections within last 12 months excluding medical collections at time of application for the secondary applicant", "parseFunction": parse_sec_app_collections_12_mths_ex_med,},
    "sec_app_mths_since_last_major_derog": { "name": "sec_app_mths_since_last_major_derog", "description": " Months since most recent 90-day or worse rating at time of application for the secondary applicant", "parseFunction": parse_sec_app_mths_since_last_major_derog,},
    "hardship_flag": { "name": "hardship_flag", "description": "Flags whether or not the borrower is on a hardship plan", "parseFunction": parse_hardship_flag,},
    "hardship_type": { "name": "hardship_type", "description": "Describes the hardship plan offering", "parseFunction": parse_hardship_type,},
    "hardship_reason": { "name": "hardship_reason", "description": "Describes the reason the hardship plan was offered", "parseFunction": parse_hardship_reason,},
    "hardship_status": { "name": "hardship_status", "description": "Describes if the hardship plan is active, pending, canceled, completed, or broken", "parseFunction": parse_hardship_status,},
    "deferral_term": { "name": "deferral_term", "description": "Amount of months that the borrower is expected to pay less than the contractual monthly payment amount due to a hardship plan", "parseFunction": parse_deferral_term,},
    "hardship_amount": { "name": "hardship_amount", "description": "The interest payment that the borrower has committed to make each month while they are on a hardship plan", "parseFunction": parse_hardship_amount,},
    "hardship_start_date": { "name": "hardship_start_date", "description": "The start date of the hardship plan period", "parseFunction": parse_hardship_start_date,},
    "hardship_end_date": { "name": "hardship_end_date", "description": "The end date of the hardship plan period", "parseFunction": parse_hardship_end_date,},
    "payment_plan_start_date": { "name": "payment_plan_start_date", "description": "The day the first hardship plan payment is due. For example, if a borrower has a hardship plan period of 3 months, the start date is the start of the three-month period in which the borrower is allowed to make interest-only payments.", "parseFunction": parse_payment_plan_start_date,},
    "hardship_length": { "name": "hardship_length", "description": "The number of months the borrower will make smaller payments than normally obligated due to a hardship plan", "parseFunction": parse_hardship_length,},
    "hardship_dpd": { "name": "hardship_dpd", "description": "Account days past due as of the hardship plan start date", "parseFunction": parse_hardship_dpd,},
    "hardship_loan_status": { "name": "hardship_loan_status", "description": "Loan Status as of the hardship plan start date", "parseFunction": parse_hardship_loan_status,},
    "orig_projected_additional_accrued_interest": { "name": "orig_projected_additional_accrued_interest", "description": "The original projected additional interest amount that will accrue for the given hardship payment plan as of the Hardship Start Date. This field will be null if the borrower has broken their hardship payment plan.", "parseFunction": parse_orig_projected_additional_accrued_interest,},
    "hardship_payoff_balance_amount": { "name": "hardship_payoff_balance_amount", "description": "The payoff balance amount as of the hardship plan start date", "parseFunction": parse_hardship_payoff_balance_amount,},
    "hardship_last_payment_amount": { "name": "hardship_last_payment_amount", "description": "The last payment amount as of the hardship plan start date", "parseFunction": parse_hardship_last_payment_amount,},
    "disbursement_method": { "name": "disbursement_method", "description": "The method by which the borrower receives their loan. Possible values are: CASH, DIRECT_PAY", "parseFunction": parse_disbursement_method,},
    "debt_settlement_flag": { "name": "debt_settlement_flag", "description": "Flags whether or not the borrower, who has charged-off, is working with a debt-settlement company.", "parseFunction": parse_debt_settlement_flag,},
    "debt_settlement_flag_date": { "name": "debt_settlement_flag_date", "description": "The most recent date that the Debt_Settlement_Flag has been set  ", "parseFunction": parse_debt_settlement_flag_date,},
    "settlement_status": { "name": "settlement_status", "description": "The status of the borrower’s settlement plan. Possible values are: COMPLETE, ACTIVE, BROKEN, CANCELLED, DENIED, DRAFT", "parseFunction": parse_settlement_status,},
    "settlement_date": { "name": "settlement_date", "description": "The date that the borrower agrees to the settlement plan", "parseFunction": parse_settlement_date,},
    "settlement_amount": { "name": "settlement_amount", "description": "The loan amount that the borrower has agreed to settle for", "parseFunction": parse_settlement_amount,},
    "settlement_percentage": { "name": "settlement_percentage", "description": "The settlement amount as a percentage of the payoff balance amount on the loan", "parseFunction": parse_settlement_percentage,},
    "settlement_term": { "name": "settlement_term", "description": "The number of months that the borrower will be on the settlement plan", "parseFunction": parse_settlement_term,},
}

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
    'zip_code': object
}
