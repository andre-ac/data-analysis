import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


train_dir = './data/train.csv'
test_dir = './data/test.csv' 

train_data = pd.read_csv(train_dir)
test_data = pd.read_csv(test_dir)

#Using a KNN


features_temp = ["Pclass", "Sex","Age", "SibSp", "Parch","Fare","Embarked","Survived"]
features = ["Pclass", "Sex","Age", "SibSp", "Parch","Fare","Embarked"]
X_temp = pd.get_dummies(train_data[features_temp]).dropna()

y = X_temp["Survived"]
X = X_temp.drop(columns=["Survived"])

#getting awful results, possible due to this, panda's knn seems to be unable to handle NaN's 
X_test = pd.get_dummies(test_data[features]).fillna(0)

model = KNeighborsClassifier(n_neighbors=29)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('my_submissionv2.csv', index=False)
