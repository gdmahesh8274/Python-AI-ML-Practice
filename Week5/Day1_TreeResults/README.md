# Week 5 - Day 1 - Tree Results

## Decision Tree

A Decision Tree makes predictions by splitting the data using feature values.

The Iris dataset is divided into training and testing sets. The model learns from the training data and is evaluated using the testing data.

## Tree Depth Experiment

The experiment tests these maximum depths:

- 1
- 2
- 3
- 4
- 5
- No maximum depth

## Interpretation

A very small tree may be too simple and can underfit the data.

A deeper tree can learn more detailed patterns, but an unnecessarily deep tree may overfit the training data.

The best depth should be selected by comparing model performance on unseen testing data.

## Evaluation

Accuracy is used to compare the predictions with the actual classes.

The experiment helps show how changing `max_depth` affects Decision Tree performance.
