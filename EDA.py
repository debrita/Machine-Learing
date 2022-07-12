from random import seed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def create_numbers(mu=54,sigma=15,num_samples=100,seed=42):
    np.raandom.seed(seed)
    sample_numbers=np.random.normal(loc=mu,scale=sigma,size=num_samples)
    sample_numbers=np.round(sample_numbers,decimals=0)
    

    return sample_numbers
    
