import pandas as pd
import numpy as np
import time
import seaborn as sns
import matplotlib.pyplot as plt

class Print:
    def __lt__(self, thing):
        print(thing)

p = Print()
p < "Successfully imported."

data = pd.read_csv('./1- mental-illnesses-prevalence.csv')

p < data

p < '---------------------------------'

time.sleep(2)

countries = data['Entity'].unique()

p < countries

#data.columns = ['Country' , 'Year' , 'Schizophrenia disorders' , 'Depressive disorders' , 'Anxiety disorders' , 'Bipolar disorders' , 'Eating disorders']
#data.head(1)

data.info()
p < sns.heatmap(data.isna())
data.columns = ['Code', 'Country', 'Year', 'Schizophrenia disorders', 'Depressive disorders', 'Anxiety disorders', 'Bipolar disorders', 'Eating disorders']
p < data.columns

Schizo_mean = data['Schizophrenia disorders'].mean()
Depression_mean = data['Depressive disorders'].mean()
Anxiety_mean = data['Anxiety disorders'].mean()
Bipolar_mean = data['Bipolar disorders'].mean()
Eating_mean = data['Eating disorders'].mean()

mean_list = [Schizo_mean, Depression_mean, Anxiety_mean, Bipolar_mean, Eating_mean]
p < mean_list
