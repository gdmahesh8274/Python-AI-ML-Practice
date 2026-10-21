# Week 7 - Day 2 - Plot Training and Validation Loss/Accuracy

from pathlib import Path

import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

tf.keras.utils.set_random_seed(42)
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train).astype("float32")
X_test = scaler.transform(X_test).astype("float32")

model = tf.keras.Sequential([
    tf.keras.Input(shape=(4,)),
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(3, activation="softmax"),
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

history = model.fit(
    X_train, y_train, epochs=80, batch_size=16,
    validation_split=0.2, verbose=0
)

output_folder = Path(__file__).parent

plt.figure()
plt.plot(history.history["loss"], label="Training loss")
plt.plot(history.history["val_loss"], label="Validation loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Neural Network Loss")
plt.legend()
plt.tight_layout()
plt.savefig(output_folder / "loss_plot.png")
plt.close()

plt.figure()
plt.plot(history.history["accuracy"], label="Training accuracy")
plt.plot(history.history["val_accuracy"], label="Validation accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("Neural Network Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig(output_folder / "accuracy_plot.png")
plt.close()

loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print("Test loss:", round(loss, 3))
print("Test accuracy:", round(accuracy, 3))
print("Saved loss_plot.png and accuracy_plot.png")
