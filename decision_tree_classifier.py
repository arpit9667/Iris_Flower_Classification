import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree

## decoding the string value of the species 
def decode(num):
    for i in num:
        if i==0:
            print("setosa")
        elif i==1:
            print("versicolor")
        else:
            print("virginica")

## Reading the dataset loaded in the system  
iris = pd.read_csv('iris.csv')

## creating target and feature variable 
X =  iris.drop('species', axis=1).values
y = iris['species'].values

## spliting the dataset into Training and Testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42, stratify=y)

## Create a DecisionTreeClassifier: dtc
dtc = tree.DecisionTreeClassifier()

## Fit the classifier to the training data
dtc.fit(X_train,y_train)

## Print the accuracy
print(dtc.score(X_test,y_test))

## Taking user input for a certain feature set
d1 = float(input("Enter sepal length : "))
d2 = float(input("Enter sepal width : "))
d3 = float(input("Enter petal length : "))
d4 = float(input("Enter petal width : "))

data = [d1, d2, d3, d4]

## predictind the species for the user-given input 
print(decode(clf.predict([data])))

