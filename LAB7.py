from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

x =[[0],[1],[2],[3]]
y =[0,0,1,1]

neigh =knn(n_neighbors= 3) #To set the number of neighbours
neigh.fit(x,y) # This function is used for training the data set

print(neigh.predict([[1.7]])) #Testing function
print(neigh.predict_proba([[1.6]])) #Returns probability estimates for the test data x.

#Performing knn on iris dataset
iris_dataset =load_iris()

X = iris_dataset.data
Y = iris_dataset.target

X_train, X_test, Y_train,Y_test =train_test_split(X,Y,test_size=0.3, random_state=42)

knearest =knn(n_neighbors=6)
knearest.fit(X_train,Y_train)
knearest.predict(X_test)
print(knearest.score(X_test,Y_test))

