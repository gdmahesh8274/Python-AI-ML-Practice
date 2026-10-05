# Week 4 Day 5 - Notebook Explanation

## Dataset

The project uses the Iris dataset from scikit-learn. The target is the flower class, and the input features describe flower measurements.

## Train-Test Split

The dataset is divided into training data and testing data. Training data teaches the model, while testing data checks how well the trained model performs on unseen examples.

## Feature Scaling

StandardScaler is used because KNN depends on distances between data points. Scaling keeps features with larger numeric values from dominating the distance calculation.

## Models

### Logistic Regression

Logistic Regression is used as a classification model. It learns relationships between the features and the flower classes.

### K-Nearest Neighbors

KNN predicts a class by looking at nearby training examples. This project uses three neighbors.

## Evaluation

Accuracy measures how many predictions are correct.

The confusion matrix shows correct and incorrect predictions by class.

The classification report displays precision, recall, and F1-score.

The project compares the accuracy of both models and prints the better model, or reports a tie.
