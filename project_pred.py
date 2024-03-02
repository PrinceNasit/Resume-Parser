import pandas as pd
data1 = pd.read_csv('Projects.csv')

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import joblib

vectorizer_ = TfidfVectorizer(max_features=1000)

model_ = RandomForestClassifier()

data1["Description"] = data1["Description"].str.lower() 
data1["Description"] = data1["Description"].str.replace("[^a-zA-Z0-9 ]", "", regex=True)  

features = vectorizer_.fit_transform(data1["Description"])

X_train, X_test, y_train, y_test = train_test_split(features, data1["Skill Set"], test_size=0.2)

model_.fit(X_train, y_train)

y_pred = model_.predict(X_test)

f1 = f1_score(y_test, y_pred, average="micro")
print('Model for skills extraction from project descriptions loaded...')
print(f"F1-score (micro): {f1:.4f}")

# joblib.dump(model1,'project_.pkl')

def prediction(description):
    new_features = vectorizer_.transform(description)
    predictions = model_.predict(new_features)
    return predictions