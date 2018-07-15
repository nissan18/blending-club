"""
List of data columns with their metadata and helper functions
"""

def get_feature_types():
    return sorted(list(set([c["feature"]["type"] for c in columns])))


def get_column_names():
    return sorted(list(set([c["name"] for c in columns])))


def get_columns_by_feature_type(feature_type):
    assert (isinstance(feature_type, str)), "feature_type must be str"
    assert (feature_type in get_feature_types()), "Invalid feature type: {}".format(feature_type)

    return [c for c in columns if c["feature"]["type"] == feature_type]


def get_columns_by_feature_types(feature_types):
    assert (isinstance(feature_types, list)), "feature_types but be a list of strings"
    assert all([x in get_feature_types() for x in feature_types]), "Invalid feature type in: {}".format(feature_types)

    return [c for c in columns if c["feature"]["type"] == feature_types]


def get_columns_by_names(column_names):
    assert (isinstance(column_names, list)), "column_names has to be a list of column names"
    assert all([x in get_column_names() for x in column_names]), "Invalid column name in: {}".format(column_names)

    return [c for c in columns if c["name"] in column_names]


def get_dtypes_by_name():
    return {c["name"] : c["dtype"] for c in columns}



columns = [
    {
        "name": "acc_now_delinq",
        "dtype": "float64",
        "feature": {
            "type": "numeric"
        }
    },
    {
        "name": "acc_open_past_24mths",
        "dtype": "float64",
        "feature": {
            "type": "numeric"
        }
    },
    {
        "name": "addr_state",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "AK",
                "AL",
                "AR",
                "AZ",
                "CA",
                "CO",
                "CT",
                "DC",
                "DE",
                "FL",
                "GA",
                "HI",
                "ID",
                "IL",
                "IN",
                "KS",
                "KY",
                "LA",
                "MA",
                "MD",
                "ME",
                "MI",
                "MN",
                "MO",
                "MS",
                "MT",
                "NC",
                "ND",
                "NE",
                "NH",
                "NJ",
                "NM",
                "NV",
                "NY",
                "OH",
                "OK",
                "OR",
                "PA",
                "RI",
                "SC",
                "SD",
                "TN",
                "TX",
                "UT",
                "VA",
                "VT",
                "WA",
                "WI",
                "WV",
                "WY"
            ]
        }
    },
    {
        "name": "all_util",
        "dtype": "float64",
        "feature": {
            "type": "numeric"
        }
    },
    {
        "name": "annual_inc",
        "dtype": "float64",
        "feature": {
            "type": "numeric"
        }
    },
    {
        "name": "annual_inc_joint",
        "dtype": "float64",
        "feature": {
            "type": "numeric"
        }
    },
    {
        "name": "application_type",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "Individual",
                "Joint App"
            ]
        }
    },
    {
        "name": "avg_cur_bal",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "bc_open_to_buy",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "bc_util",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "chargeoff_within_12_mths",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "collection_recovery_fee",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "collections_12_mths_ex_med",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "debt_settlement_flag",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "N",
                "Y"
            ]
        }
    },
    {
        "name": "debt_settlement_flag_date",
        "dtype": str,
        "feature": { "type": "date" }
    },
    {
        "name": "deferral_term",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "delinq_2yrs",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "delinq_amnt",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "desc",
        "dtype": str,
        "feature": { "type": "NLP" }  # ignore for now
    },
    {
        "name": "disbursement_method",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "Cash",
                "DirectPay"
            ]
        }
    },
    {
        "name": "dti",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "dti_joint",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "earliest_cr_line",
        "dtype": str,
        "feature": { "type": "date" }
    },
    {
        "name": "emp_length",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "< 1 year",
                "1 year",
                "2 years",
                "3 years",
                "4 years",
                "5 years",
                "6 years",
                "7 years",
                "8 years",
                "9 years",
                "10+ years",
                "n/a"
            ]
        }
    },
    {
        "name": "emp_title",
        "dtype": str,
        "feature": { "type": "NLP" }  # ignore for now
    },
    {
        "name": "fico_range_high",
        "dtype": "int64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "fico_range_low",
        "dtype": "int64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "funded_amnt",
        "dtype": "int64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "funded_amnt_inv",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "grade",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "A",
                "B", 
                "C",
                "D",
                "E",
                "F",
                "G"
            ]
        }
    },
    {
        "name": "hardship_amount",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "hardship_dpd",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "hardship_end_date",
        "dtype": str,
        "feature": { "type": "date" }
    },
    {
        "name": "hardship_flag",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "N"
            ]
        }
    },
    {
        "name": "hardship_last_payment_amount",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "hardship_length",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "hardship_loan_status",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "Current",
                "In Grace Period",
                "Late (16-30 days)"
            ]
        }
    },
    {
        "name": "hardship_payoff_balance_amount",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "hardship_reason",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "DISABILITY",
                "EXCESSIVE_OBLIGATIONS",
                "NATURAL_DISASTER"
            ]
        }
    },
    {
        "name": "hardship_start_date",
        "dtype": str,
        "feature": { "type": "date" }
    },
    {
        "name": "hardship_status",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "COMPLETED"
            ]
        }
    },
    {
        "name": "hardship_type",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "INTEREST ONLY-3 MONTHS DEFERRAL"
            ]
        }
    },
    {
        "name": "home_ownership",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "NONE",
                "OWN",
                "RENT",
                "ANY",
                "OTHER",
                "MORTGAGE"
            ]
        }
    },
    {
        "name": "id",
        "dtype": "int64",
        "feature": { "type": "don't parse" }  # don't need this for real model, maybe add to test for noise
    },
    {
        "name": "il_util",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "initial_list_status",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "f",
                "w"
            ]
        }
    },
    {
        "name": "inq_fi",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "inq_last_12m",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "inq_last_6mths",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "installment",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "int_rate",
        "dtype": str,
        "feature": { "type": "percent" }  #     df["f_int_rate"] = df["int_rate"].apply(lambda val : np.float64(val.strip(" %")))

    },
    {
        "name": "issue_d",
        "dtype": str,
        "feature": { "type": "date" }
    },
    {
        "name": "last_credit_pull_d",
        "dtype": str,
        "feature": { "type": "date" }
    },
    {
        "name": "last_fico_range_high",
        "dtype": "int64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "last_fico_range_low",
        "dtype": "int64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "last_pymnt_amnt",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "last_pymnt_d",
        "dtype": str,
        "feature": { "type": "date" }
    },
    {
        "name": "loan_amnt",
        "dtype": "int64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "loan_status",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "Fully Paid",
                "Charged Off",
                "Does not meet the credit policy. Status:Fully Paid",
                "Does not meet the credit policy. Status:Charged Off",
                "Current",
                "Late (16-30 days)",
                "Late (31-120 days)",
                "In Grace Period",
                "Default"
            ]
        }
    },
    {
        "name": "max_bal_bc",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "member_id",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "mo_sin_old_il_acct",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "mo_sin_old_rev_tl_op",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "mo_sin_rcnt_rev_tl_op",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "mo_sin_rcnt_tl",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "mort_acc",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "mths_since_last_delinq",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "mths_since_last_major_derog",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "mths_since_last_record",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "mths_since_rcnt_il",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "mths_since_recent_bc",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "mths_since_recent_bc_dlq",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "mths_since_recent_inq",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "mths_since_recent_revol_delinq",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "next_pymnt_d",
        "dtype": str,
        "feature": { "type": "date" }
    },
    {
        "name": "num_accts_ever_120_pd",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "num_actv_bc_tl",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "num_actv_rev_tl",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "num_bc_sats",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "num_bc_tl",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "num_il_tl",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "num_op_rev_tl",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "num_rev_accts",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "num_rev_tl_bal_gt_0",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "num_sats",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "num_tl_120dpd_2m",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "num_tl_30dpd",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "num_tl_90g_dpd_24m",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "num_tl_op_past_12m",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "open_acc",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "open_acc_6m",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "open_act_il",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "open_il_12m",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "open_il_24m",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "open_rv_12m",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "open_rv_24m",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "orig_projected_additional_accrued_interest",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "out_prncp",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "out_prncp_inv",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "payment_plan_start_date",
        "dtype": str,
        "feature": { "type": "date" }
    },
    {
        "name": "pct_tl_nvr_dlq",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "percent_bc_gt_75",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "policy_code",
        "dtype": "int64",
        "feature": {
            "type": "one-hot encoding",
            "values": [
                1,  # publicly available policy_code
                2  # new products not publicly available policy_code
            ]
        }
    },
    {
        "name": "pub_rec",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "pub_rec_bankruptcies",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "purpose",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "car",
                "credit_card",
                "debt_consolidation",
                "home_improvement",
                "house",
                "major_purchase",
                "medical",
                "moving",
                "other",
                "renewable_energy",
                "small_business",
                "vacation",
                "wedding"
            ]
        }
    },
    {
        "name": "pymnt_plan",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "n"
            ]
        }
    },
    {
        "name": "recoveries",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "revol_bal",
        "dtype": "int64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "revol_bal_joint",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "revol_util",
        "dtype": str,
        "feature": {"type": "percent" } # buildPercentageFeature(df, "revol_util")
    },
    {
        "name": "sec_app_chargeoff_within_12_mths",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "sec_app_collections_12_mths_ex_med",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "sec_app_earliest_cr_line",
        "dtype": str,
        "feature": { "type": "date" }
    },
    {
        "name": "sec_app_fico_range_high",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "sec_app_fico_range_low",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "sec_app_inq_last_6mths",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "sec_app_mort_acc",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "sec_app_mths_since_last_major_derog",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "sec_app_num_rev_accts",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "sec_app_open_acc",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "sec_app_open_act_il",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "sec_app_revol_util",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "settlement_amount",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "settlement_date",
        "dtype": str,
        "feature": { "type": "date" }
    },
    {
        "name": "settlement_percentage",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "settlement_status",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "ACTIVE",
                "BROKEN",
                "COMPLETE"
            ]
        }
    },
    {
        "name": "settlement_term",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "sub_grade",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "A1",
                "A2",
                "A3",
                "A4",
                "A5",
                "B1",
                "B2",
                "B3",
                "B4",
                "B5",
                "C1",
                "C2",
                "C3",
                "C4",
                "C5",
                "D1",
                "D2",
                "D3",
                "D4",
                "D5",
                "E1",
                "E2",
                "E3",
                "E4",
                "E5",
                "F1",
                "F2",
                "F3",
                "F4",
                "F5",
                "G1",
                "G2",
                "G4",
                "G5"
            ] 
        }
    },
    {
        "name": "tax_liens",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "term",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                " 36 months",
                " 60 months"
            ]
        }
    },
    {
        "name": "title",
        "dtype": str,
        "feature": { "type": "NLP" }
    },
    {
        "name": "tot_coll_amt",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "tot_cur_bal",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "tot_hi_cred_lim",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "total_acc",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "total_bal_ex_mort",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "total_bal_il",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "total_bc_limit",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "total_cu_tl",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "total_il_high_credit_limit",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "total_pymnt",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "total_pymnt_inv",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "total_rec_int",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "total_rec_late_fee",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "total_rec_prncp",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "total_rev_hi_lim",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "url",
        "dtype": str,
        "feature": { "type": "don't parse" }  # check probably always https://lendingclub.com/browse/loanDetail.action?loan_id=<id>
    },
    {
        "name": "verification_status",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "Not Verified",
                "Source Verified",
                "Verified"
            ]
        }
    },
    {
        "name": "verification_status_joint",    # WARNING: verified_status_joint SHOULD BE verification_status_joint
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "Not Verified",
                "Source Verified",
                "Verified"
            ]
        }
    },
    {
        "name": "zip_code",
        "dtype": str,
        "feature": {
            "type": "one-hot encoding",
            "values": [
                "010xx",
                "011xx",
                "015xx",
                "016xx",
                "017xx",
                "018xx",
                "020xx",
                "021xx",
                "023xx",
                "024xx",
                "025xx",
                "026xx",
                "027xx",
                "028xx",
                "029xx",
                "030xx",
                "038xx",
                "044xx",
                "045xx",
                "053xx",
                "054xx",
                "060xx",
                "062xx",
                "063xx",
                "064xx",
                "066xx",
                "067xx",
                "070xx",
                "071xx",
                "073xx",
                "074xx",
                "076xx",
                "077xx",
                "080xx",
                "082xx",
                "083xx",
                "087xx",
                "088xx",
                "100xx",
                "101xx",
                "103xx",
                "104xx",
                "105xx",
                "108xx",
                "109xx",
                "111xx",
                "112xx",
                "113xx",
                "114xx",
                "115xx",
                "117xx",
                "120xx",
                "123xx",
                "125xx",
                "126xx",
                "129xx",
                "130xx",
                "131xx",
                "132xx",
                "134xx",
                "138xx",
                "139xx",
                "140xx",
                "142xx",
                "150xx",
                "151xx",
                "152xx",
                "154xx",
                "157xx",
                "162xx",
                "166xx",
                "168xx",
                "171xx",
                "172xx",
                "173xx",
                "175xx",
                "177xx",
                "180xx",
                "183xx",
                "187xx",
                "188xx",
                "189xx",
                "190xx",
                "191xx",
                "194xx",
                "197xx",
                "200xx",
                "201xx",
                "207xx",
                "208xx",
                "210xx",
                "211xx",
                "212xx",
                "217xx",
                "220xx",
                "221xx",
                "223xx",
                "224xx",
                "225xx",
                "226xx",
                "228xx",
                "229xx",
                "232xx",
                "233xx",
                "234xx",
                "235xx",
                "236xx",
                "240xx",
                "246xx",
                "253xx",
                "255xx",
                "260xx",
                "270xx",
                "272xx",
                "274xx",
                "277xx",
                "278xx",
                "280xx",
                "281xx",
                "282xx",
                "283xx",
                "284xx",
                "285xx",
                "288xx",
                "290xx",
                "292xx",
                "293xx",
                "294xx",
                "295xx",
                "298xx",
                "299xx",
                "300xx",
                "301xx",
                "302xx",
                "303xx",
                "304xx",
                "305xx",
                "306xx",
                "307xx",
                "310xx",
                "313xx",
                "317xx",
                "318xx",
                "319xx",
                "320xx",
                "321xx",
                "322xx",
                "325xx",
                "327xx",
                "328xx",
                "329xx",
                "330xx",
                "331xx",
                "333xx",
                "334xx",
                "335xx",
                "336xx",
                "337xx",
                "338xx",
                "339xx",
                "342xx",
                "344xx",
                "346xx",
                "347xx",
                "349xx",
                "351xx",
                "352xx",
                "354xx",
                "356xx",
                "357xx",
                "358xx",
                "360xx",
                "361xx",
                "365xx",
                "366xx",
                "370xx",
                "371xx",
                "372xx",
                "377xx",
                "378xx",
                "379xx",
                "380xx",
                "381xx",
                "384xx",
                "385xx",
                "388xx",
                "389xx",
                "390xx",
                "392xx",
                "395xx",
                "400xx",
                "402xx",
                "403xx",
                "409xx",
                "420xx",
                "423xx",
                "427xx",
                "430xx",
                "432xx",
                "433xx",
                "440xx",
                "441xx",
                "442xx",
                "445xx",
                "446xx",
                "448xx",
                "450xx",
                "452xx",
                "453xx",
                "454xx",
                "458xx",
                "460xx",
                "461xx",
                "462xx",
                "463xx",
                "464xx",
                "467xx",
                "468xx",
                "469xx",
                "471xx",
                "473xx",
                "480xx",
                "481xx",
                "482xx",
                "483xx",
                "484xx",
                "485xx",
                "486xx",
                "488xx",
                "489xx",
                "490xx",
                "494xx",
                "495xx",
                "496xx",
                "498xx",
                "531xx",
                "532xx",
                "535xx",
                "539xx",
                "545xx",
                "546xx",
                "547xx",
                "548xx",
                "549xx",
                "550xx",
                "551xx",
                "553xx",
                "554xx",
                "557xx",
                "560xx",
                "564xx",
                "565xx",
                "577xx",
                "585xx",
                "592xx",
                "598xx",
                "599xx",
                "601xx",
                "603xx",
                "604xx",
                "605xx",
                "606xx",
                "609xx",
                "610xx",
                "612xx",
                "617xx",
                "618xx",
                "622xx",
                "625xx",
                "629xx",
                "630xx",
                "631xx",
                "633xx",
                "640xx",
                "641xx",
                "647xx",
                "650xx",
                "651xx",
                "656xx",
                "657xx",
                "658xx",
                "660xx",
                "670xx",
                "671xx",
                "680xx",
                "681xx",
                "684xx",
                "700xx",
                "701xx",
                "703xx",
                "705xx",
                "707xx",
                "708xx",
                "713xx",
                "714xx",
                "718xx",
                "719xx",
                "720xx",
                "721xx",
                "723xx",
                "727xx",
                "729xx",
                "730xx",
                "731xx",
                "735xx",
                "740xx",
                "741xx",
                "744xx",
                "745xx",
                "750xx",
                "751xx",
                "752xx",
                "754xx",
                "757xx",
                "759xx",
                "760xx",
                "761xx",
                "762xx",
                "765xx",
                "766xx",
                "769xx",
                "770xx",
                "773xx",
                "774xx",
                "775xx",
                "776xx",
                "778xx",
                "782xx",
                "783xx",
                "785xx",
                "786xx",
                "787xx",
                "788xx",
                "790xx",
                "791xx",
                "794xx",
                "797xx",
                "799xx",
                "800xx",
                "801xx",
                "802xx",
                "805xx",
                "806xx",
                "809xx",
                "815xx",
                "826xx",
                "838xx",
                "840xx",
                "841xx",
                "850xx",
                "851xx",
                "852xx",
                "853xx",
                "856xx",
                "857xx",
                "859xx",
                "864xx",
                "871xx",
                "875xx",
                "878xx",
                "890xx",
                "891xx",
                "894xx",
                "895xx",
                "898xx",
                "900xx",
                "902xx",
                "904xx",
                "906xx",
                "907xx",
                "908xx",
                "910xx",
                "913xx",
                "915xx",
                "917xx",
                "919xx",
                "920xx",
                "921xx",
                "922xx",
                "923xx",
                "925xx",
                "926xx",
                "927xx",
                "928xx",
                "930xx",
                "931xx",
                "932xx",
                "933xx",
                "934xx",
                "935xx",
                "936xx",
                "939xx",
                "940xx",
                "941xx",
                "944xx",
                "945xx",
                "946xx",
                "948xx",
                "949xx",
                "950xx",
                "951xx",
                "954xx",
                "955xx",
                "956xx",
                "957xx",
                "958xx",
                "959xx",
                "960xx",
                "967xx",
                "970xx",
                "971xx",
                "972xx",
                "973xx",
                "974xx",
                "980xx",
                "981xx",
                "982xx",
                "983xx",
                "984xx",
                "985xx",
                "988xx",
                "990xx",
                "995xx"
            ]
        }
    }
]
