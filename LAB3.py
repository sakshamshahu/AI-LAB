import pandas as pd
import numpy as np
'''
Q1- Display some rows randomly  --
Q2- Print the shape of the dataset --
Q3- Print all the rows where the petal length is b/w 1.2 to 1.5 cm.
Q4- Count the species 
Q5- Petal length mean median sum and min,max value.
Q6- Delete the ID column
'''
raw = pd.read_csv('Iris.csv')
print(raw)
raw1 =pd.DataFrame(raw)
print(raw1)

print(raw1.sample(5))
print(raw1.sample(frac=0.03))
print('\n','The Shape is: ',np.shape(raw))

Length_Find = raw1['PetalLengthCm'].between(1.2,1.5, inclusive=False)
print(Length_Find)

length=raw1.query('PetalLengthCm > 1.2 & PetalLengthCm < 1.5')
print(length,'\n')

print(raw1['Species'].value_counts(dropna=False))
Petal_Length = raw1['PetalLengthCm']
print(np.mean(Petal_Length))
print(np.median(Petal_Length))
print(np.sum(Petal_Length))
print(np.min(Petal_Length))
print(np.max(Petal_Length))

del raw1['Id']
print(raw1)