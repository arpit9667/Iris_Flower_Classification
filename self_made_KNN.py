#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[6]:


import pandas as pd
from scipy.spatial import distance
from sklearn.metrics import accuracy_score as a_s 
from sklearn.model_selection import train_test_split

## dist function to find the euclidean distance between two data points
def dist(a, b):
    return distance.euclidean(a, b)
 
## class for classifier
class KNN:
    ## fit method for the classifier
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    ## predict method for the classifier
    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.adjacent(row)
            predictions.append(label)
        return predictions

    ## finding the adjacent data point for a given data point
    def adjacent(self, row):
        best_dist = eu(row, self.X_train[0])
        best_index = 0
        for i in range (1, len(self.X_train)):
            dist = eu(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]

## Reading the dataframe  
iris = pd.read_csv("iris.csv")

## creating feature and target variable for the model
X =  iris.drop('species', axis=1).values
y = iris['species'].values

## spliting the dataset into Training and Testing Dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42, stratify=y)

## making a instance of the KNN class: knn
knn = KNN()

##fitting the dataset into knn classifier
knn.fit(X_train, y_train)

## predicting the species for the test dataset
prediction = knn.predict(X_test)

## calculating the accuracy for the given model
print(a_s(prediction, y_test))


# In[ ]:




