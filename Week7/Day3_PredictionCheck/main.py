# Week 7 - Day 3 - Prediction Check
# Train an image classifier and inspect its predictions.

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

tf.keras.utils.set_random_seed(42)
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

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
model.fit(X_train, y_train, epochs=5, batch_size=64, verbose=0)

probabilities = model.predict(X_test[:10], verbose=0)
predictions = np.argmax(probabilities, axis=1)

for i in range(10):
    print("Image", i, "| Actual:", y_test[i], "| Predicted:", predictions[i])

fig, axes = plt.subplots(2, 5, figsize=(10, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(X_test[i], cmap="gray")
    ax.set_title(f"True: {y_test[i]} / Pred: {predictions[i]}")
    ax.axis("off")
plt.tight_layout()
plt.show()
