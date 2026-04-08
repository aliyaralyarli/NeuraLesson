from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

X,y=make_classification(n_samples=1000,n_features=20,random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

for i in range(1,16):
    train_model = DecisionTreeClassifier(max_depth=i, random_state=42)
    train_model.fit(X_train, y_train)

    train_accuracy_train_model = accuracy_score(y_train, train_model.predict(X_train))
    test_accuracy_test_model = accuracy_score(y_test, train_model.predict(X_test))

    print(f"Train Model Training Accuracy: {train_accuracy_train_model}")
    print(f"Test Model Training Accuracy: {test_accuracy_test_model}")
