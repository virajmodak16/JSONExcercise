# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:19:56 2019

@author: vpmodak
"""

"""
Viraj P Modak

JSON exercise 10/31/2019

For this purpose, I have decided to bundle 2&3 together 
since that results in a much more concise code and a more informative output

"""


import pandas as pd
import numpy as np
import json
from pandas.io.json import json_normalize

df = pd.read_json('data/world_bank_projects.json')
data = json.load((open('data/world_bank_projects.json')))
data_norm = json_normalize(data, 'mjtheme_namecode')

# Find 10 countries with the most projects:
print(df['countryname'].value_counts()[0:10])

# Create data frame with missing names filled in
data_norm['name'].replace('', np.nan,inplace=True)
data_norm = data_norm.groupby('code').apply(lambda x : x.ffill().bfill())

# Find 10 major project themes:
print(data_norm['name'].value_counts()[0:10])