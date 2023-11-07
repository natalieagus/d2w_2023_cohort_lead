import numpy as np 
import pandas as pd 

def calc_linreg(X, beta):
    ## TODO 
    pass 

def compute_cost_linreg(X, y, beta):
    ## TODO 
    pass 

def prepare_feature(df_feature):
    ## TODO 
    pass 

# the target is basically y --> dependent variable 
# this is a column vector, with rows as many as #samples
def prepare_target(df_target):
    cols = df_target.shape[1] # df_target.shape returns a tuple #row,#col, i'm expecting 1 here at Week 9

    # check if df_target is a dataframe? 
    if type(df_target) == pd.DataFrame:
        # if yes, convert to numpy using the to_numpy() func from Pandas
        np_target = df_target.to_numpy()
    else:
        # by definition, if arg is not a DF, it will be a numpy array
        np_target = df_target 
    # ensure that we return a vector for each target
    return np_target.reshape(-1, cols) 
    