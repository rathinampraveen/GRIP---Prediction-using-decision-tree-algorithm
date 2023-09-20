# -*- coding: utf-8 -*-
"""Prediction_using_Decision_tree_algorithm(Praveen R).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OanZ59_AzmbZUGKrymJri3ISbSIwe6-R

### **Predicting the flower species based on the Sepal length, Sepal width, patel length and patel width**

### Decision tree

A decision tree is a non-parametric supervised learning algorithm, which is utilized for both classification and regression tasks. It has a hierarchical, tree structure, which consists of a root node, branches, internal nodes and leaf nodes.

Using this algorithm, we are going to predict the flower species.

### How decision trees work
Decision trees work in a step-wise manner, meaning that they perform a step-by-step process instead of following a continuous process. Decision trees follow a tree-like structure, where the nodes of a tree are split using the features based on defined criteria. The main criteria based on which decision trees split are:

**Gini impurity:** Measures the impurity in a node.

**Entropy:** Measures the randomness of the system.

**Variance:** This is normally used in the Regression model, which is a measure of the variation of each data point from the mean.

### Importing the necessary libraries
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

from sklearn import tree
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

"""### Loading the dataset"""

df = load_iris()
df = sns.load_dataset('iris')
df.head(10)

df.tail(10)

"""### Dataset information"""

df.info()

"""### Dataset shape"""

df.shape

"""### Descriptive statistics of the dataset"""

df.describe()

"""### Visulaizing the dataset to identify the pattern"""

plt.scatter(df["sepal_length"],df["sepal_width"])
plt.show()

"""### Checking the relationsip between features with each other using pairplot"""

sns.pairplot((df), hue='species')
plt.show()

"""### Counting the number of specific species for the prediction"""

df["species"].value_counts()

"""### Selecting the features to build the decision tree model"""

X = df.iloc[:, :-2]
y = df['species']

"""### Spliting the data, Training and testing the data for the decision tree model"""

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.4, random_state=42)
treemodel = DecisionTreeClassifier()
treemodel.fit(X_train, y_train)

"""### Visulaizing the decision tree and classification report of our decision tree model and checking the model accuracy score:"""

plt.figure(figsize=(10, 10))
tree.plot_tree(treemodel, filled=True)
ypred = treemodel.predict(X_test)
score = accuracy_score(ypred, y_test)
print("Accuracy score of our decision tree model is: ",score*100,"%.")
print("---------Classification report of our model----------")
print(classification_report(ypred, y_test))

"""Thankyou!"""