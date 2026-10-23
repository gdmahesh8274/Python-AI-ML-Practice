# Week 7 - Day 3 - Image Data Introduction
# MNIST contains 28x28 grayscale images of handwritten digits.

import matplotlib.pyplot as plt
import tensorflow as tf

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

print("Training images:", X_train.shape)
print("Test images:", X_test.shape)
print("One image shape:", X_train[0].shape)
print("Pixel values range from", X_train.min(), "to", X_train.max())
print("First image label:", y_train[0])

plt.imshow(X_train[0], cmap="gray")
plt.title(f"Handwritten digit: {y_train[0]}")
plt.axis("off")
plt.show()

# Normalize pixel values from 0-255 to 0-1 for neural networks.
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0
print("Normalized pixel range:", X_train.min(), "to", X_train.max())
