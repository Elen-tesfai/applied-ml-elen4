# lab04 - Titanic Regression Model

## Overview
In this project, we aim to predict the Fare of passengers aboard the Titanic using various regression models. We explore the data, preprocess it, and train multiple models to evaluate their performance in predicting a continuous variable. The models tested include:
- **Linear Regression**
- **Ridge Regression** (L2 penalty)
- **ElasticNet** (L1 + L2 combined)
- **Polynomial Regression**

The goal is to assess the performance of these models and draw insights into which model works best for predicting Titanic fares.

## Table of Contents
1. [Introduction](#introduction)
2. [Data Exploration and Preparation](#data-exploration-and-preparation)
    - [2.1 Inspecting Missing Values](#21-inspecting-missing-values)
    - [2.2 Handling Missing Values](#22-handling-missing-values)
    - [2.3 Encoding Categorical Variables](#23-encoding-categorical-variables)
3. [Feature Selection and Justification](#feature-selection-and-justification)
4. [Model Training and Evaluation](#model-training-and-evaluation)
    - [4.1 Linear Regression](#41-linear-regression)
    - [4.2 Ridge Regression](#42-ridge-regression)
    - [4.3 ElasticNet Regression](#43-elasticnet-regression)
    - [4.4 Polynomial Regression](#44-polynomial-regression)
5. [Model Comparison and Reflections](#model-comparison-and-reflections)
    - [5.1 Comparison of Models](#51-comparison-of-models)
    - [5.2 Best Performing Model](#52-best-performing-model)
    - [5.3 Visualizations](#53-visualizations)
6. [Final Thoughts & Insights](#final-thoughts--insights)
    - [6.1 Summarize Findings](#61-summarize-findings)
    - [6.2 Discuss Challenges](#62-discuss-challenges)
    - [6.3 Optional Next Steps](#63-optional-next-steps)

---

## 1. Introduction
This project uses the Titanic dataset to predict the continuous variable **Fare**. Regression models are implemented to predict the fare paid by passengers based on various features such as class, age, gender, and embarked location. We aim to determine which regression model performs best.

---

## Section 1: Import and Inspect the Data
In this section, we will load the Titanic dataset, explore its structure, and identify any issues such as missing values.

### Reflection 1:
1) **How many data instances are there?**
2) **How many features are there?**
3) **What are the names of the features?**
4) **Are there any missing values?**
5) **Are there any non-numeric features?**
6) **Are the data instances sorted on any of the attributes?**
7) **What are the units of age?**
8) **What are the minimum, median, and maximum age?**
9) **What two features have the highest correlation?**
10) **Are there any categorical features that might be useful for prediction?**

---

## Section 2: Data Exploration and Preparation

### 2.1 Inspecting Missing Values
The Titanic dataset contains both numerical and categorical variables, including **Age**, **Fare**, **Pclass**, and **Sex**. We first load and inspect the data to understand the structure and identify any issues like missing values.

#### Reflection 2.1:
- What patterns or anomalies do you notice?
- Do any features stand out as potential predictors?
- Are there any visible class imbalances?

### 2.2 Handling Missing Values
- Handle missing values for features like **Age** and **Embarked**.
- Encode categorical features such as **Sex** and **Embarked**.
- Normalize or scale numerical features where necessary.
- Select relevant features for regression analysis.

### 2.3 Encoding Categorical Variables
Categorical variables need to be transformed into numerical values to use them in the regression models. Techniques like **one-hot encoding** are used for this transformation.

#### Reflection 2.3:
- Why might family size be a useful feature for predicting survival?
- Why convert categorical data to numeric?

---

## Section 3: Feature Selection and Justification

### 3.1 Choose Features and Target
Define the target variable (**Fare**) and the feature variables (independent variables).

### 3.2 Define X and y
Here, we define `X` as the feature variables and `y` as the target variable (Fare).

#### Reflection 3:
- Why were these features selected?
- Are there any features that are likely to be highly predictive of Fare?

---

## Section 4: Model Training and Evaluation

### 4.1 Linear Regression
Linear regression is a fundamental regression technique used to model the relationship between the target variable and input features. We train this model to make predictions for Titanic fares.

### 4.2 Ridge Regression
Ridge regression adds an **L2 regularization** term to the linear regression model. This helps reduce overfitting by penalizing large coefficients in the model. We use Ridge regression to test whether regularization improves prediction accuracy.

### 4.3 ElasticNet Regression
ElasticNet is a combination of both **L1 (Lasso)** and **L2 (Ridge)** regularization. We use this model to evaluate a balance between Lasso and Ridge regularization, which could potentially offer better model performance for the Titanic dataset.

### 4.4 Polynomial Regression
Polynomial regression is used to model non-linear relationships between features and the target variable. By adding polynomial features, we can capture more complex patterns in the data that linear models may miss.

---

## Section 5: Model Comparison and Reflections

### 5.1 Comparison of Models
We compare the performance of all four regression models (Linear Regression, Ridge, ElasticNet, and Polynomial) using common evaluation metrics such as **R²**, **Mean Absolute Error (MAE)**, and **Root Mean Squared Error (RMSE)**.

### 5.2 Best Performing Model
After evaluating all the models, we identify the one that performs best based on the chosen evaluation metrics. We provide insights into why that particular model might have outperformed others.

### 5.3 Visualizations
We visualize model predictions to understand the fit, especially for polynomial regression. We also visualize important feature correlations and residuals to better understand the model's performance.

---

## Section 6: Final Thoughts & Insights

### 6.1 Summarize Findings
- What features were most useful?
- Which regression model performed best?
- How did model complexity or regularization affect the results?

### 6.2 Discuss Challenges
- Was fare difficult to predict? Why?
- Did skew or outliers impact the models?

### 6.3 Optional Next Steps
- Try different features besides the ones used (e.g., **Pclass**, **Sex** if you didn't use them this time).
- Try predicting **Age** instead of **Fare**.
- Explore **log transformation** of **Fare** to reduce skew.

---