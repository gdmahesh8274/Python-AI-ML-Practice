# Week 7 - Day 3 - Model Improvement
# Compare a basic neural network with a larger one using the same data.

import tensorflow as tf

tf.keras.utils.set_random_seed(42)
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

X_train = X_train[:12000].astype("float32") / 255.0
y_train = y_train[:12000]
X_test = X_test[:2000].astype("float32") / 255.0
y_test = y_test[:2000]

def build_model(hidden_layers):
    layers = [tf.keras.Input(shape=(28, 28)), tf.keras.layers.Flatten()]
    for neurons in hidden_layers:
        layers.append(tf.keras.layers.Dense(neurons, activation="relu"))
    layers.append(tf.keras.layers.Dense(10, activation="softmax"))
    model = tf.keras.Sequential(layers)
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model

experiments = [
    ("Basic model", [32]),
    ("Improved model", [128, 64]),
]

for name, hidden_layers in experiments:
    tf.keras.utils.set_random_seed(42)
    model = build_model(hidden_layers)
    history = model.fit(
        X_train, y_train, epochs=5, batch_size=64,
        validation_split=0.1, verbose=0
    )
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
    print(name)
    print("Validation accuracy:", round(history.history["val_accuracy"][-1], 3))
    print("Test accuracy:", round(accuracy, 3))
    print("-" * 30)

print("More layers may help, but compare results rather than assuming.")
