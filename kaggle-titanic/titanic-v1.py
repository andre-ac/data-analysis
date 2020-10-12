import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

train_dir = './data/train.csv'
test_dir = './data/test.csv' 

train_data = pd.read_csv(train_dir)
test_data = pd.read_csv(test_dir)

#Using a random forest model

y = train_data['Survived']

features = ["Pclass", "Sex","Age", "SibSp", "Parch","Fare","Embarked"]
X = pd.get_dummies(train_data[features]).dropna(inplace=True)
X_test = pd.get_dummies(test_data[features])

#model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
#model.fit(X, y)
#predictions = model.predict(X_test)

#output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
#output.to_csv('my_submission.csv', index=False)

print(X.shape)