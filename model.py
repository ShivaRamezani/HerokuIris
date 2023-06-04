# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier


df = pd.read_csv('Iris.csv')
df = df.drop('Id',axis = 1)
X = df.drop('Species',axis = 1)
y = df['Species']

dtree = DecisionTreeClassifier()
dtree.fit(X, y)

# Saving model to disk
pickle.dump(dtree, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
#print(model.predict([[5.1, 3.5, 1.4, 0.2]]))