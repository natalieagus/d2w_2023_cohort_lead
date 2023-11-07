import pandas as pd
import numpy as np

def normalize_z(dfin, columns_means=None, columns_stds=None):
    ## TODO 
    pass 

def get_features_targets(df, feature_names, target_names):
    ## TODO 
    pass  

def prepare_feature(df_feature):
    ## TODO 
    pass  

def prepare_target(df_target):
    ## TODO 
    pass  

def split_data(df_feature, df_target, random_state=None, test_size=0.5):
    ## TODO 
    pass  

import os
current_directory = os.getcwd()

# Check if the "week10" directory is one level above the current directory
if os.path.basename(current_directory) == "week10":
    # If the script is in the "week10 directory
    file_path = os.path.join(current_directory, "data",  "breast_cancer_data.csv")
else:
    # If the script is one level above the "Week 9" directory
    file_path = os.path.join(current_directory, "week10", "data", "breast_cancer_data.csv")
    
## TASK 2
df = None

## TASK 3
df_feature, df_target = None
df_feature,_,_ = None

## TASK 4
def replace_target(df_target, target_name, map_vals):
    ## TODO 
    pass  
df_target = None

## TASK 5
feature = None
target = None
