# Import libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.semi_supervised import LabelSpreading
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Read CSV file
df = pd.read_csv("customer_churn.csv")

print(df.head())


# Select features and target
X = df.drop("Churn", axis=1)
y = df["Churn"]


# Convert target into numbers
y = y.map({"No": 0, "Yes": 1})


# Convert categorical columns into numbers
X = pd.get_dummies(X)


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ---------- SUPERVISED ----------

model1 = DecisionTreeClassifier()

model1.fit(X_train, y_train)

pred1 = model1.predict(X_test)

acc1 = accuracy_score(y_test, pred1)

print("Supervised Accuracy:", acc1)


# ---------- SEMI-SUPERVISED ----------

y_semi = y_train.copy()

# Hide some labels
y_semi.iloc[::2] = -1

model2 = LabelSpreading()

model2.fit(X_train, y_semi)

pred2 = model2.predict(X_test)

acc2 = accuracy_score(y_test, pred2)

print("Semi-Supervised Accuracy:", acc2)


# ---------- ENSEMBLE ----------

model3 = RandomForestClassifier(n_estimators=10)

model3.fit(X_train, y_train)

pred3 = model3.predict(X_test)

acc3 = accuracy_score(y_test, pred3)

print("Ensemble Accuracy:", acc3)


# ---------- COMPARISON ----------

print("\nPerformance Comparison")

print("Decision Tree   :", acc1)
print("Label Spreading :", acc2)
print("Random Forest   :", acc3)
