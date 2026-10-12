# Week 5 Day 5 - Project Documentation

## Objective

Predict student pass/fail results from study hours and attendance using a Decision Tree classifier.

## Dataset

The sample CSV has three columns: `Hours_Studied`, `Attendance`, and `Passed`. A value of 1 means pass and 0 means fail.

## Preprocessing

1. Load the CSV using Pandas.
2. Inspect the first rows and check missing values.
3. Select study hours and attendance as features.
4. Select pass/fail as the target.
5. Split data into training and testing sets with stratification.
6. Apply StandardScaler inside a pipeline, fitted on training data only.

## Model

Train a Decision Tree classifier with maximum depth 3 and a fixed random state.

## Evaluation

Evaluate on the held-out test set using accuracy, confusion matrix, and precision/recall/F1 classification report. The exact results are printed when running the code.

## Prediction

Use the trained pipeline to predict whether a new student with 6 study hours and 85% attendance will pass.

## Note

The dataset is small and invented for learning; results should not be treated as reliable educational predictions.
