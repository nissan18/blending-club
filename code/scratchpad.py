import time
import logging
import sys

import definitions
import pandas_helper
import scikit_helper
import lendingclub_helper
import lendingclub_columns
import lendingclub_validation
import pprint as pp

from lendingclub_pipeline import LendingClub_Pipeline


def main():
    print("Begin: " + __file__)

    """
    1. take only numeric columns
    2. build model to predict if loan will default
    3. train/test/validate
    4. in the future, add other types of columns
    """

    trainfile = "finished_train_sample.csv"
    testfile = "finished_test_sample.csv"
    "sample.csv"


    pipeline = LendingClub_Pipeline()
    pipeline.run(trainfile, testfile)
    return


    real = ['628xx', '593xx', '437xx', '072xx', '706xx', '243xx', '619xx', '648xx', '147xx', '184xx', '275xx', '847xx', '978xx', '918xx', '315xx', '664xx', '711xx', '905xx', '046xx', '019xx', '953xx', '635xx', '686xx', '176xx', '363xx', '279xx', '465xx', '291xx', '897xx', '136xx', '128xx', '436xx', '611xx', '685xx', '992xx', '296xx', '159xx', '457xx', '989xx', '952xx', '368xx', '793xx', '193xx', '393xx', '566xx', '107xx', '241xx', '078xx', '710xx', '218xx', '968xx', '722xx', '767xx', '199xx', '704xx', '032xx', '570xx', '600xx', '542xx', '405xx', '662xx', '991xx', '196xx', '215xx', '833xx', '148xx', '814xx', '986xx', '276xx', '789xx', '061xx', '835xx', '031xx', '478xx', '674xx', '911xx', '396xx', '119xx', '435xx', '451xx', '170xx', '068xx', '350xx', '683xx', '665xx', '943xx', '258xx', '975xx', '434xx', '326xx', '829xx', '362xx', '846xx', '297xx', '712xx', '242xx', '537xx', '155xx', '667xx', '209xx', '376xx', '181xx', '563xx', '474xx', '144xx', '661xx', '863xx', '383xx', '316xx', '613xx', '937xx', '860xx', '404xx', '431xx', '784xx', '530xx', '286xx', '411xx', '271xx', '086xx', '156xx', '124xx', '373xx', '976xx', '237xx', '231xx', '195xx', '924xx', '827xx', '265xx', '916xx', '075xx', '443xx', '386xx', '085xx', '961xx', '880xx', '106xx', '645xx', '689xx', '675xx', '855xx', '541xx', '608xx', '324xx', '206xx']
    for col in lendingclub_columns.columns:
        if col["name"] == "zip_code":
            zip_code = col
    
    temp = real + zip_code["feature"]["values"]
    zip_code["feature"]["values"] = sorted(list(set(temp)))

    with open("zip_code.py", "w") as fout:
        pp.pprint(zip_code, fout)



    return


    filename = "sample.csv"
    filename = "finished_test_sample.csv"
    filename = "finished_train_sample.csv"
    df = pandas_helper.readData(filename, lendingclub_columns.get_dtypes_by_name())

    lendingclub_validation.validate_one_hot_encoding_columns(df)







    print("End: " + __file__)


if __name__ == "__main__":
    main()
