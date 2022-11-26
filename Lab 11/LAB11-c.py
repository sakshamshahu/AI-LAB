from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("mushrooms.csv")

num_dataset = dataset.copy()
label =LabelEncoder()
for col in num_dataset.columns:
    num_dataset[col] = label.fit_transform(num_dataset[col])

x =num_dataset.drop(["class"], axis =1)
y =num_dataset["class"].values

x_train, x_test, y_train, y_test = train_test_split(x,y, random_state=42, test_size=0.25)

svm = SVC(random_state=42, gamma="auto").fit(x_train,y_train)
print("Test Accuracy: {}%".format(svm.score(x_test,y_test)*100,2))

from sklearn.metrics import confusion_matrix
y_pred_svm = svm.predict(x_test)
y_true_svm = y_test
cm = confusion_matrix(y_true_svm, y_pred_svm)
f, ax = plt.subplots(figsize =(5,5))
sns.heatmap(cm,annot = True,linewidths=0.5,linecolor="red",fmt = ".0f",ax=ax)
plt.xlabel("y_pred_lr")
plt.ylabel("y_true_lr")
plt.show()