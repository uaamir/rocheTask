# -*- coding: utf-8 -*-
"""
Task 1.py
Iris Classification 
Created on Tue Jun 25 22:32:31 2019

@author: MAK
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix



iris = datasets.load_iris()


data = iris.data
labels=iris.target

#splitting data into train and test 30%
x_train,x_test,y_train,y_test = train_test_split(data,labels,test_size=0.30)

dt_classifier = tree.DecisionTreeClassifier()


dt_classifier.fit(x_train,y_train)

predictions = dt_classifier.predict(x_test)
print( "Accuracy ")
print(accuracy_score(y_test,predictions)) # Acuracy

print("\nConfusion Matrix")
print(confusion_matrix(y_test,predictions)) # Confusion Matrix
