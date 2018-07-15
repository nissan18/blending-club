# Plan

1. get random sample
2. train model to predict expected return rate for each loan
    - figure out how to compute actual return rate (to train model)
3. validate, retrain, test

Link to Lending Club API - https://www.lendingclub.com/developers/listed-loans


### QUESTION: How do deal with one-hot encoding columns?
Should I hard-code all possible values, build a model and then validate any input into model or build them on a fly? Since I need to think about it, let's ignore one-hot encoding columns for now.

