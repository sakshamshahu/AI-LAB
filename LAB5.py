import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

Raw = pd.read_csv('Iris.csv')
print(Raw)
IrisDataframe = pd.DataFrame(Raw)
print(IrisDataframe)

SepalWidth_Hist = sns.histplot(data =IrisDataframe, x='SepalWidthCm')
plt.show()

SepalLength_Hist = sns.histplot(data =IrisDataframe, x='SepalLengthCm')
plt.show()

PetalLengthCm_Hist = sns.histplot(data =IrisDataframe, x='PetalLengthCm')
plt.show()

PetalWidthCm_Hist = sns.histplot(data =IrisDataframe, x='PetalWidthCm')
plt.show()

ll=sns.jointplot(data=IrisDataframe, x='SepalLengthCm', y='PetalLengthCm', hue ='Species')
plt.show()

tt=sns.scatterplot(data=IrisDataframe, x='SepalLengthCm', y='PetalLengthCm', hue ='Species')
plt.show()

box_plot =sns.boxplot(data=IrisDataframe, y= 'PetalLengthCm',x='Species', hue='Species')
plt.show()

violin_plot =sns.violinplot(data=IrisDataframe, y= 'PetalLengthCm',x='Species', hue='Species')
plt.show()