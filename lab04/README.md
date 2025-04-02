# lab04 - Titanic Regression Model

## Overview
In this project, we aim to predict the `Fare` of passengers aboard the Titanic using various regression models. We explore the data, preprocess it, and train multiple models to evaluate their performance in predicting a continuous variable. The models tested include:
- Linear Regression
- Ridge Regression (L2 penalty)
- ElasticNet (L1 + L2 combined)
- Polynomial Regression

The goal is to assess the performance of these models and draw insights into which model works best for predicting Titanic fares.

## Table of Contents
1. [Introduction](#introduction)
2. [Data Exploration and Preparation](#data-exploration-and-preparation)
3. [Feature Selection and Justification](#feature-selection-and-justification)
4. [Model Training and Evaluation](#model-training-and-evaluation)
    1. [Linear Regression](#linear-regression)
    2. [Ridge Regression](#ridge-regression)
    3. [ElasticNet](#elasticnet)
    4. [Polynomial Regression](#polynomial-regression)
5. [Model Comparison and Reflections](#model-comparison-and-reflections)
6. [Final Thoughts](#final-thoughts)

## 1. Introduction
This project uses the Titanic dataset to predict the continuous variable `Fare`. Regression models are implemented to predict the fare paid by passengers based on various features such as class, age, gender, and embarked location. We aim to determine which regression model performs best.

## 2. Data Exploration and Preparation
### 2.1 Inspecting the Data
The Titanic dataset contains both numerical and categorical variables, including `Age`, `Fare`, `Pclass`, and `Sex`. We first load and inspect the data to understand the structure and identify any issues like missing values.

### 2.2 Data Cleaning and Preprocessing
- Handle missing values for features like `Age` and `Embarked`.
- Encode categorical features such as `Sex` and `Embarked`.
- Normalize or scale numerical features where necessary.
- Select relevant features for regression analysis.

## 3. Feature Selection and Justification
### 3.1 Correlation Analysis
We perform correlation analysis to identify the relationship between different features and the target variable (`Fare`). Features that show a strong correlation with `Fare` are selected for regression modeling.

## 4. Model Training and Evaluation
### 4.1 Linear Regression
Linear regression is a fundamental regression technique used to model the relationship between the target variable and input features. We train this model to make predictions for Titanic fares.

### 4.2 Ridge Regression
Ridge regression adds an L2 regularization term to the linear regression model. This helps reduce overfitting by penalizing large coefficients in the model. We use Ridge regression to test whether regularization improves prediction accuracy.

### 4.3 ElasticNet Regression
ElasticNet is a combination of both L1 (Lasso) and L2 (Ridge) regularization. We use this model to evaluate a balance between Lasso and Ridge regularization, which could potentially offer better model performance for the Titanic dataset.

### 4.4 Polynomial Regression
Polynomial regression is used to model non-linear relationships between features and the target variable. By adding polynomial features, we can capture more complex patterns in the data that linear models may miss.

## 5. Model Comparison and Reflections
### 5.1 Comparison of Models
We compare the performance of all four regression models (Linear Regression, Ridge, ElasticNet, and Polynomial) using common evaluation metrics such as R², Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE).

### 5.2 Best Performing Model
After evaluating all the models, we identify the one that performs best based on the chosen evaluation metrics. We provide insights into why that particular model might have outperformed others.

### 5.3 Visualizations
We visualize model predictions to understand the fit, especially for polynomial regression. We also visualize important feature correlations and residuals to better understand the model's performance.

## 6. Final Thoughts
Based on our analysis, we conclude that **[Insert the best model here]** performed the best for predicting Titanic fares. However, further tuning and feature engineering could improve the model's predictions even more. We discuss next steps for future improvements and analysis.

---

## Links

- [Your Applied ML Repository](https://github.com/your-username/titanic-regression-model)
- [Lab04 Folder in Repository](https://github.com/your-username/titanic-regression-model/tree/main/lab04)
- [Lab04 Notebook File](https://github.com/your-username/titanic-regression-model/blob/main/lab04/lab04_notebook.ipynb)

## Additional Information

- **Operating System**: Windows
- **Name**: Elen
- **Time Spent**: [Approximate time spent on the lab]
