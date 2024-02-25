# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ewruOv9wr59J8GgRd4NdJapLcN5bD7bI
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

titanic_data=pd.read_csv('/content/train.csv')

titanic_data.head()

titanic_data.shape

titanic_data.info()

titanic_data.isnull().sum()

titanic_data=titanic_data.drop(columns='Cabin',axis=1)

titanic_data['Age'].fillna(titanic_data['Age'].mean(),inplace=True)

print(titanic_data['Embarked'].mode())

titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0],inplace=True)

titanic_data.isnull().sum()

titanic_data.describe()

titanic_data['Survived'].value_counts()

sns.set()

sns.countplot(x='Survived', data=titanic_data)

sns.countplot(x='Sex', data=titanic_data)

sns.countplot(x='Sex',hue='Survived',data=titanic_data)

sns.countplot(x='Pclass', data=titanic_data)

sns.countplot(x='Pclass',hue='Survived',data=titanic_data)

titanic_data.replace({'Sex':{'male':0,'female':1},'Embarked':{'S':0,'C':1,'Q':2}},inplace=True)

titanic_data.head()

X=titanic_data.drop(columns=['PassengerId','Name','Ticket','Survived'],axis=1)
Y=titanic_data['Survived']

print(X)

print(Y)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

model=LogisticRegression()

model.fit(X_train,Y_train)

X_train_prediction=model.predict(X_train)

print(X_train_prediction)

training_data_accuracy=accuracy_score(Y_train,X_train_prediction)
print(training_data_accuracy)