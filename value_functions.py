import numpy as np
import pandas as pd
import csv

def greens_equally():

    # load the projects and relevant variables.
    # assumes all non-green variables present

    projects = pd.read_csv("variables.csv")
    projects = np.array(projects)

    greens = projects[:, 4]

    # return equal weights for the greens
    
    return np.array([1 if x in ["green", "Green", "green.", "Green."] else 0 for x in greens])

def greens_amplification():

    projects = pd.read_csv("variables.csv")
    p = np.array(projects)
  
    amp_scores = [str(x) for x in p[:,10]]
    amplification_scores = [x.replace(",","") for x in amp_scores]
    amp_scores = [float(x) for x in amplification_scores]
    amp_scores = [np.log(x) for x in amp_scores]
    mean = np.nanmean(amp_scores)
    amp_scores = np.nan_to_num(amp_scores, nan=mean)
    return amp_scores
