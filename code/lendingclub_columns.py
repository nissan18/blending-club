

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
            "values": []
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
        "feature": { "type": "one-hot encoding", "values": [] }
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
        "feature": { "type": "one-hot encoding", "values": [] }
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
                "10+ years",
                "< 1 year",
                "1 year",
                "3 years",
                "8 years",
                "9 years",
                "4 years",
                "5 years",
                "6 years",
                "2 years",
                "7 years",
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
        "feature": { "type": "one-hot encoding", "values": [] }
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
        "feature": { "type": "one-hot encoding", "values": [] }
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
        "feature": { "type": "one-hot encoding", "values": [] }
    },
    {
        "name": "hardship_payoff_balance_amount",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "hardship_reason",
        "dtype": str,
        "feature": { "type": "one-hot encoding", "values": [] }
    },
    {
        "name": "hardship_start_date",
        "dtype": str,
        "feature": { "type": "date" }
    },
    {
        "name": "hardship_status",
        "dtype": str,
        "feature": { "type": "one-hot encoding", "values": [] }
    },
    {
        "name": "hardship_type",
        "dtype": str,
        "feature": { "type": "one-hot encoding", "values": [] }
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
        "feature": { "type": "one-hot encoding", "values": [] }
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
        "feature": { "type": "one-hot encoding", "values": [] }  # TODO: "publicly available policy_code=1, new products not publicly available policy_code=2"
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
        "feature": { "type": "one-hot encoding", "values": [] }
    },
    {
        "name": "pymnt_plan",
        "dtype": str,
        "feature": { "type": "one-hot encoding", "values": [] }
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
        "feature": { "type": "one-hot encoding", "values": [] }
    },
    {
        "name": "settlement_term",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "sub_grade",
        "dtype": str,
        "feature": { "type": "one-hot encoding", "values": [] }
    },
    {
        "name": "tax_liens",
        "dtype": "float64",
        "feature": { "type": "numeric" }
    },
    {
        "name": "term",
        "dtype": str,
        "feature": { "type": "one-hot encoding", "values": [] }
    },
    {
        "name": "title",
        "dtype": str,
        "feature": { "type": "NLP" }  # TODO: title -- nlp?
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
        "feature": { "type": "don't parse" }  # TODO: url -- check probably always https://lendingclub.com/browse/loanDetail.action?loan_id=<id>
    },
    {
        "name": "verification_status",
        "dtype": str,
        "feature": { "type": "one-hot encoding", "values": [] }
    },
    {
        "name": "verification_status_joint",
        "dtype": str,
        "feature": { "type": "one-hot encoding", "values": [] }  # WARNING: verified_status_joint SHOULD BE verification_status_joint
    },
    {
        "name": "zip_code",
        "dtype": str,
        "feature": { "type": "one-hot encoding", "values": [] }
    }
]
