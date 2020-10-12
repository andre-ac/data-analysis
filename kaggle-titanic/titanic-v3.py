import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree

train_dir = './data/train.csv'
test_dir = './data/test.csv' 

train_data = pd.read_csv(train_dir)
test_data = pd.read_csv(test_dir)

#Using a decision tree

y = train_data['Survived']

features = ["Pclass", "Sex","Age", "SibSp", "Parch","Fare","Embarked"]
X = pd.get_dummies(train_data[features]).fillna(0)
X_test = pd.get_dummies(test_data[features]).fillna(0)

model = tree.DecisionTreeClassifier()
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('my_submissionv3.csv', index=False)