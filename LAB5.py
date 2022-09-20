import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

Raw = pd.read_csv('Iris.csv')
print(Raw)
IrisDataframe = pd.DataFrame(Raw)
print(IrisDataframe)

SepalWidth_Hist = sns.histplot(data =IrisDataframe, x='SepalWidthCm')

SepalLength_Hist = sns.histplot(data =IrisDataframe, x='SepalLengthCm')

PetalLengthCm_Hist = sns.histplot(data =IrisDataframe, x='PetalLengthCm')

PetalWidthCm_Hist = sns.histplot(data =IrisDataframe, x='PetalWidthCm')

ll=sns.jointplot(data=IrisDataframe, x='SepalLengthCm', y='PetalLengthCm', hue ='Species')

tt=sns.scatterplot(data=IrisDataframe, x='SepalLengthCm', y='PetalLengthCm', hue ='Species')

box_plot =sns.boxplot(data=IrisDataframe, y= 'PetalLengthCm',x='Species', hue='Species')

violin_plot =sns.violinplot(data=IrisDataframe, y= 'PetalLengthCm',x='Species', hue='Species')