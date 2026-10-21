# Week 7 - Day 2 - TensorFlow Setup
# Install first: python -m pip install tensorflow

try:
    import tensorflow as tf
except ImportError:
    print("TensorFlow is not installed.")
    print("Run: python -m pip install tensorflow")
    raise SystemExit(1)

print("TensorFlow version:", tf.__version__)
print("Available GPUs:", tf.config.list_physical_devices("GPU"))
print("TensorFlow setup is ready.")
