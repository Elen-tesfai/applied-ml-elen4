# Lab 05: Ensemble Models - Wine Quality Prediction

## Overview
In this lab, we apply ensemble machine learning models, specifically Random Forest and Gradient Boosting, to predict the quality of red wines. We utilize the Wine Quality dataset, which includes chemical features of wines, and explore how ensemble methods can improve the accuracy of wine quality prediction.

## Objective
The goal of this lab is to:
- Train Random Forest and Gradient Boosting classifiers to predict wine quality based on physicochemical features.
- Evaluate and compare the performance of these models using various metrics such as accuracy, F1 score, and confusion matrix.

## Steps
The following steps are performed throughout the notebook:

### 1. Importing Libraries
Necessary libraries are imported for data manipulation, model training, and evaluation. This includes libraries like pandas, numpy, matplotlib, scikit-learn, etc.

### 2. Loading the Data
The Wine Quality dataset is loaded and inspected. The dataset contains 12 features, including alcohol content, acidity levels, and other chemical properties, along with the wine quality label.

### 3. Exploratory Data Analysis (EDA)
Initial exploration of the data:
- **Check for missing values:** We ensure there are no missing values in the dataset.
- **Visualize distributions of features:** We plot histograms and other visualizations for features like alcohol content, acidity, and quality.
- **Explore correlations:** We examine the relationships between features to understand which might be useful for prediction. For example, we found that higher alcohol content correlates with higher wine quality.

### 4. Preprocessing
- The target variable (wine quality) is transformed into categorical values (low, medium, and high quality) to create a classification task.
- The data is then split into training and test sets.

### 5. Model Training
We train the following ensemble models:
- Random Forest Classifier
- Gradient Boosting Classifier

Both models are trained on the same training set, and their performance is evaluated using the test set.

### 6. Model Evaluation
The models' performance is evaluated using the following metrics:
- Accuracy
- F1 Score
- Confusion Matrix

### 7. Results Comparison
- After training both models, we compared their performance using metrics like accuracy, F1 score, and confusion matrix. This allowed us to evaluate which model performed best for predicting wine quality.

## Requirements
To run the notebook, you’ll need to install the following Python libraries:

```bash
pip install pandas numpy matplotlib scikit-learn
```
## How to Generate the Results Table:
To generate the results table as a PNG image, run the following script:

```bash
python generate_table.py
```
This will create a PNG file (`ensemble_models_table.png`) containing the comparison table of model performance.

## Conclusion:
This lab demonstrated the application of ensemble methods like Random Forest and Gradient Boosting to predict wine quality. By training and evaluating both models, we gained insights into their performance and how they can be used in classification tasks like this one.