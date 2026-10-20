# Week 7 - Day 1 - MLP Experiments
# Compare different hidden layer sizes on the same Iris train/test split.

import warnings

from sklearn.datasets import load_iris
from sklearn.exceptions import ConvergenceWarning
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
)

experiments = [
    (5,),
    (10,),
    (20,),
    (10, 10),
]

for layers in experiments:
    model = make_pipeline(
        StandardScaler(),
        MLPClassifier(hidden_layer_sizes=layers, max_iter=1500, random_state=42)
    )

    # A convergence warning means the model reached the iteration limit.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", ConvergenceWarning)
        model.fit(X_train, y_train)

    train_accuracy = accuracy_score(y_train, model.predict(X_train))
    test_accuracy = accuracy_score(y_test, model.predict(X_test))

    print("Hidden layers:", layers)
    print("Training accuracy:", round(train_accuracy, 3))
    print("Testing accuracy:", round(test_accuracy, 3))
    print("-" * 35)

print("Compare training and testing accuracy to spot possible overfitting.")
print("A larger network does not always perform better.")
