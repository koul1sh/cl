import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

df = pd.DataFrame(X, columns=feature_names)
df['target'] = y

print("Head of the Iris dataset:")
print(df.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = LogisticRegression(max_iter=200)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))

samples = [[5.1, 3.5, 1.4, 0.2],
           [6.0, 2.2, 4.0, 1.0],
           [6.9, 3.2, 5.7, 2.3]]

print("\nPredictions for Sample Inputs:")
for features in samples:
    input_array = np.array([features])
    pred_class = clf.predict(input_array)
    class_name = target_names[pred_class[0]]
    print(f"{features} -> Predicted class: {class_name}")
