# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 15:54:55 2020

@author: vatsal
"""

import pandas as pd
import os

df_train = pd.read_csv('lang_id_train.csv')
file= "train.txt"
path= r"C:\Users\vatsa\OneDrive\Desktop\hw4-handout\handout\bert_input_data"
for i in df_train["text"]:
    with open(os.path.join(path, file), 'a',encoding='utf-8') as fp:
        fp.write("%s\n" %i)
        
df_test = pd.read_csv('lang_id_test.csv')
file= "test.txt"
path= r"C:\Users\vatsa\OneDrive\Desktop\hw4-handout\handout\bert_input_data"
for i in df_test["text"]:
    with open(os.path.join(path, file), 'a',encoding='utf-8') as fp:
        fp.write("%s\n" %i)
        
df_eval = pd.read_csv('lang_id_eval.csv')
file= "eval.txt"
path= r"C:\Users\vatsa\OneDrive\Desktop\hw4-handout\handout\bert_input_data"
for i in df_eval["text"]:
    with open(os.path.join(path, file), 'a',encoding='utf-8') as fp:
        fp.write("%s\n" %i)