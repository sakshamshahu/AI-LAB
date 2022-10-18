#Simple Cereal Dataset Analysis
from cProfile import label
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

CerealImport = pd.read_csv('cereal.csv')

CerealImportDataframe = pd.DataFrame(CerealImport)
print(CerealImportDataframe)

print(CerealImportDataframe.sample(7))
print(CerealImportDataframe.sample(frac=0.08))

print('\n','The Shape is: ',np.shape(CerealImportDataframe))

TopRatings=CerealImportDataframe.query('rating > 65 & rating< 100')
print("\nSome of the Cereal with Highest rating are:- \n ",TopRatings)

CalorieCount = CerealImportDataframe['calories']
print('\nMean calories of all cereals combined is: ',np.mean(CalorieCount))



x  = TopRatings['name']
y = TopRatings['rating']
plt.title('Ratings graph')
plt.xlabel('Cereal Name')
plt.ylabel('Rating points')
plt.plot(x,y,color ='b',marker ='D',markerfacecolor='cyan',linestyle='--',linewidth='3',label = 'Cereal Rating Comparison')
plt.show()
