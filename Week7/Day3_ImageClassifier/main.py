# Week 7 - Day 3 - Image Classifier
# Build a simple neural network to classify handwritten digits.

import tensorflow as tf

tf.keras.utils.set_random_seed(42)
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# Use a smaller subset so this beginner example trains faster on a CPU.
X_train = X_train[:12000].astype("float32") / 255.0
y_train = y_train[:12000]
X_test = X_test[:2000].astype("float32") / 255.0
y_test = y_test[:2000]

model = tf.keras.Sequential([
    tf.keras.Input(shape=(28, 28)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax"),
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.summary()

model.fit(X_train, y_train, epochs=5, batch_size=64, validation_split=0.1)
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print("Test loss:", round(loss, 3))
print("Test accuracy:", round(accuracy, 3))
