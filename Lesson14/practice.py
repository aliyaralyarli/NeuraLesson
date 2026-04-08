from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

X,y=make_classification(n_samples=1000,n_features=20,random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

over_fitting_model=DecisionTreeClassifier(max_depth=None,random_state=42)
over_fitting_model.fit(X_train,y_train)

train_accuracy_overfitting=accuracy_score(y_train,over_fitting_model.predict(X_train))
test_accuracy_overfitting=accuracy_score(y_test,over_fitting_model.predict(X_test))

regular_model=DecisionTreeClassifier(max_depth=1,random_state=42)
regular_model.fit(X_train,y_train)

train_accuracy_regularmodel=accuracy_score(y_train,regular_model.predict(X_train))
test_accuracy_regularmodel=accuracy_score(y_test,regular_model.predict(X_test))

print(f"Overfitting Train Score:{train_accuracy_overfitting}")
print(f"Overfitting Test Score:{test_accuracy_overfitting}")

print(f"Regular Model Train Score:{train_accuracy_regularmodel}")
print(f"Regular Model Test Score:{test_accuracy_regularmodel}")
