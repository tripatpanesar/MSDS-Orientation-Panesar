#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 10:16:44 2023

@author: tripatpanesar
"""

import pandas as pd
import seaborn as sns


df = pd.read_csv('df.csv')

plot = sns.distplot(df['Hard Drive Size (in GB)'], kde=False)

plot_11 = sns.displot(data = df, 
                  x = 'Hard Drive Size (in GB)'
                  )

plot_11.set(title = 'Distribution of Hard Drive Size (GB) for 2021')


