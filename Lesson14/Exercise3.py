from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

X,y=make_classification(n_samples=1500,n_features=25,random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

basic_model=DecisionTreeClassifier(max_depth=2,random_state=42)
basic_model.fit(X_train,y_train)

train_accuracy_basic=accuracy_score(y_train,basic_model.predict(X_train))
test_accuracy_basic=accuracy_score(y_test,basic_model.predict(X_test))

overfit_model=DecisionTreeClassifier(max_depth=None,random_state=42)
overfit_model.fit(X_train,y_train)

train_accuracy_overfitmodel=accuracy_score(y_train,overfit_model.predict(X_train))
test_accuracy_overfitmodel=accuracy_score(y_test,overfit_model.predict(X_test))

complex_model=DecisionTreeClassifier(max_depth=6,random_state=42)
complex_model.fit(X_train,y_train)

train_accuracy_complexmodel=accuracy_score(y_train,complex_model.predict(X_train))
test_accuracy_complexmodel=accuracy_score(y_test,complex_model.predict(X_test))


print(f"Basic Train Score:{train_accuracy_basic}")
print(f"Basic Test Score:{test_accuracy_basic}")

print(f"Overfit Model Train Score:{train_accuracy_overfitmodel}")
print(f"Overfit Model Test Score:{test_accuracy_overfitmodel}")

print(f"Complex Model Train Score:{train_accuracy_complexmodel}")
print(f"Complex Model Test Score:{test_accuracy_complexmodel}")


