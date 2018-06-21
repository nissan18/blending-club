dataFiles = {
    "2007-2011": "../data/LoanStats3a_securev1.csv",
    "2012-2013": "../data/LoanStats3b_securev1.csv",
    "2014": "../data/LoanStats3c_securev1.csv",
    "2015": "../data/LoanStats3d_securev1.csv",
    "2016Q1": "../data/LoanStats_securev1_2016Q1.csv",
    "2016Q2": "../data/LoanStats_securev1_2016Q2.csv",
    "2016Q3": "../data/LoanStats_securev1_2016Q3.csv",
    "2016Q4": "../data/LoanStats_securev1_2016Q4.csv",
    "2017Q1": "../data/LoanStats_securev1_2017Q1.csv",
    "2017Q2": "../data/LoanStats_securev1_2017Q2.csv",
    "2017Q3": "../data/LoanStats_securev1_2017Q3.csv",
    "2017Q4": "../data/LoanStats_securev1_2017Q4.csv"
}

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

states = []  # TODO: fill array of all US states and use in one-hot encoding of addr_state

discrete_feature_values = {
    "application_type": ['Individual' 'Joint App'],
    "emp_length": ['10+ years', '< 1 year', '1 year', '3 years', '8 years', '9 years', '4 years', '5 years', '6 years', '2 years', '7 years', 'n/a'],
    "grade": [], # TODO: figure this out
    "home_ownership": ['NONE', 'OWN', 'RENT', 'ANY', 'OTHER', 'MORTGAGE'],
    "initial_list_status": [], # TODO: figure this out
    "policy_code": [], # TODO: figure this out
    "purpose": [], # TODO: figure this out
    "pymnt_plan": [], # TODO: figure this out
    "term": [], # TODO: figure this out
    "verification_status": [], # TODO: figure this out
    "zip_code": [], # TODO: figure this out
    "hardship_flag": [], # TODO: figure this out
    "hardship_type": [], # TODO: figure this out
    "hardship_reason": [], # TODO: figure this out
    "hardship_status": [], # TODO: figure this out
    "hardship_loan_status": [], # TODO: figure this out
    "disbursement_method": [], # TODO: figure this out
    "debt_settlement_flag": [], # TODO: figure this out
    "settlement_status": [] # TODO: figure this out
}
