import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("mushrooms.csv")

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

from sklearn.metrics import confusion_matrix
y_pred_model1 = model1.predict(x_test)
y_true_model1 = y_test
cm = confusion_matrix(y_true_model1, y_pred_model1)
f, ax = plt.subplots(figsize =(5,5))
sns.heatmap(cm,annot = True,linewidths=0.5,linecolor="red",fmt = ".0f",ax=ax)
plt.xlabel("y_pred_lr")
plt.ylabel("y_true_lr")
plt.show()