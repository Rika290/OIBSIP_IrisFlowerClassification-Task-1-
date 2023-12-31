# -*- coding: utf-8 -*-
"""Task-1(Iris).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BZdaRZ8ek0nCkVLHmHr2LxedKHh4cKM7

Iris Flower Classification using Machine Learning,

iris dataset from Scikit-learn library is loaded using Seaborn
"""

import seaborn as sns

"""1. **Data Collection**"""

a=sns.load_dataset('iris')

a.head(3)

a.tail(3)

"""Checking for null values"""

a.info() # implies the absence of null values in the dataset

"""Checking for duplicates"""

a.duplicated() # no duplicates

"""2. **Data Visualization**"""

sns.scatterplot(data=a,x='sepal_length',y='petal_length',hue='species')

sns.histplot(data=a['sepal_length'],bins=3)

sns.lineplot(data=a,x='sepal_length',y='sepal_width',errorbar=None)

"""Pairplot is created to view the relationship between each of the variable with others present in the data."""

sns.pairplot(data=a,hue='species')

"""Data based on each species"""

import matplotlib.pyplot as plt

sns.barplot(data=a,x='species',y='sepal_length') # Virginica is the species with highest sepal length
plt.xlabel('Species of Iris Flower')
plt.ylabel('Length of sepal')
plt.title("Species vs Sepal(length)")
plt.show()

sns.barplot(data=a,x='species',y='petal_length')# Virginica is the species with highest petal length
plt.xlabel('Species of Iris Flower')
plt.ylabel('Length of Petal')
plt.title("Species vs Petal(length)")
plt.show()

sns.barplot(data=a,x='species',y='sepal_width') # Setosa is the species with highest sepal width
plt.xlabel('Species of Iris Flower')
plt.ylabel('Width of sepal')
plt.title("Species vs Sepal(width)")
plt.show()

sns.barplot(data=a,x='species',y='petal_width') # Virginica is the species with highest petal width
plt.xlabel('Species of Iris Flower')
plt.ylabel('Width of petal')
plt.title("Species vs Petal(width)")
plt.show()

"""From above 4 graphs, we can conclude that the species Virginica is higher in terms of size.

3. **Data Pre-processing**

Splitting the data into input and output
"""

x=a.drop(columns='species') # x- input
y=a['species'] # y - output

"""Since, the data has to be classified use of categorical value is to be noted. So, to make easier, the 3 classes are converted into numerics.i.e, 'setosa'=1, 'versicolor'=2, 'virginica'=3."""

y=y.replace({'setosa':1, 'versicolor':2, 'virginica':3})

"""Standardising the input data"""

from sklearn.preprocessing import StandardScaler

std=StandardScaler()

import pandas as pd

x=pd.DataFrame(data=std.fit_transform(x),columns=x.columns)

"""Data gets divided into training and testing data"""

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

"""4. **Model building**

As, the data is composed of multi class variable, 2 algorithms are used for model training - (1) K Nearest Classification; (2) Random Forests

(1) K Nearest Classification
"""

from sklearn.neighbors import KNeighborsClassifier

kc=KNeighborsClassifier(n_neighbors=2) # defining a model

kc.fit(x_train,y_train) # training the model

score_1=kc.score(x_train,y_train)
print('Accuracy Score for KNeighborsClassifier model with training data =',score_1)
score_2=kc.score(x_test,y_test)
print('Accuracy Score for KNeighborsClassifier model with test data =',score_2)

kc_a=KNeighborsClassifier(n_neighbors=5) # same model with increased number of neighbors

kc_a.fit(x_train,y_train)# training

score_1=kc_a.score(x_train,y_train)
print('Accuracy Score for KNeighborsClassifier model with training data =',score_1)
score_2=kc_a.score(x_test,y_test)
print('Accuracy Score for KNeighborsClassifier model with test data =',score_2)

"""(2) Random Forests"""

from sklearn.ensemble import RandomForestClassifier

rfc=RandomForestClassifier(n_estimators=10) # building the model

rfc.fit(x_train,y_train)# training the model

rfc.fit(x_train,y_train)
scorea=rfc.score(x_train,y_train)
print('Accuracy Score for RandomForestClassifier model with training data =',scorea)
scoreb=rfc.score(x_test,y_test)
print('Accuracy Score for RandomForestClassifier model with test data =',scoreb)

rfc_a=RandomForestClassifier(n_estimators=50)
rfc_a.fit(x_train,y_train)

score_a=rfc_a.score(x_train,y_train)
print('Accuracy Score for RandomForestClassifier model with training data =',score_a)
score_b=rfc_a.score(x_test,y_test)
print('Accuracy Score for RandomForestClassifier model with test data =',score_b)

"""By comparing (1) and (2), when using random forest classifier,overfitting of model is observed. But the model "kc_a" built using KNeighborsClassifier algorithm with  n_neighbors=5  is better, and hence selected for flower iris classification."""

import pickle

pickle.dump(kc_a,open('/content/drive/MyDrive/ONE/iris_classification_model.pkl','wb'))

"""The model chosen for iris flower classification is saved using the module pickle in Google Drive which can be later used for the same."""