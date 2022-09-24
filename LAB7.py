from sklearn.neighbors import KNeighborsClassifier as knn

x =[[0],[1],[2],[3]]
y =[0,0,1,1]

neigh =knn(n_neighbors= 3) #To set the number of neighbours
neigh.fit(x,y) # This function is used for training the data set

print(neigh.predict([[1.7]])) #Testing function
print(neigh.predict_proba([[1.6]])) #Returns probability estimates for the test data x.


