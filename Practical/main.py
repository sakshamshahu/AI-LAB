from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import seaborn as sns
from matplotlib import pyplot as plt

dataset = pd.read_csv("mushrooms.csv")
print(dataset['class'].unique())

class_size = dataset['class'].size
print(class_size)

plt.figure()
pd.Series(dataset['class']).value_counts().sort_index().plot(kind = 'bar',color =["r", "b"])
plt.xlabel("Mushroom Class")
plt.ylabel("Count")
plt.title('Number of poisonous/edible mushrooms')
plt.show()

num_dataset = dataset.copy()
label =LabelEncoder()
for col in num_dataset.columns:
    num_dataset[col] = label.fit_transform(num_dataset[col])

x =num_dataset.drop(["class"], axis =1)
y =num_dataset["class"].values #.values returns the numpy representation of the values and also removes the axis label

x_train, x_test, y_train, y_test = train_test_split(x,y, random_state=42, test_size=0.25)

model1 =LogisticRegression(solver="newton-cg").fit(x_train,y_train)
model2 =LogisticRegression().fit(x_train,y_train)
print("Test Accuracy (newtoncg): {}%".format(model1.score(x_test,y_test)*100))
print("Test Accuracy: {}%".format(model2.score(x_test,y_test)*100))

y1 = model1.predict(x_test)
y2 = y_test
cm = confusion_matrix(y2, y1)
f, ax = plt.subplots(figsize =(4,4))
sns.heatmap(cm,annot = True,linecolor="green",fmt = ".0f", ax=ax, linewidths=0.3)
plt.xlabel("Predicted y")
plt.ylabel("Actual y")
plt.show()

class_lol = dataset["class"].to_numpy()

for i in range (0,6000):
    if class_lol[i] == 'e':
        dropped_data= dataset.drop(dataset.index[i])

print(dropped_data)