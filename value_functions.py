import numpy as np
import pandas as pd
import csv

def greens_equally():

    # load the projects and relevant variables

    projects = pd.read_csv("variables.csv")
    projects = np.array(projects)

    greens = projects[:, 4]

    # return equal weights for the greens
    
    return np.array([1 if x in ["green", "Green", "green.", "Green."] else 0 for x in greens])
    

    
