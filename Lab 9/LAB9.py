#Logistic Regression on IRIS Dataset

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

dataset = pd.read_csv("Iris.csv")
dataset = dataset.drop(columns= "Id")

X = dataset.drop(columns = ['Species'])
Y = dataset['Species']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25)

model = LogisticRegression().fit(X_train,Y_train)
print(model.score(X_test,Y_test)*100)
