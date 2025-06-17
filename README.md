# Student Performance Indicator

## Project Overview

The Student Performance Indicator is a machine learning project designed to predict students' math scores using various demographic and academic features. The workflow covers the full ML lifecycle: data analysis, feature engineering, model training, evaluation, deployment, and cloud automation.

---

## 1. Problem Statement

**Goal:** Predict students' math scores and analyze how factors like gender, ethnicity, parental education, lunch type, test preparation, and reading/writing scores affect performance.

---

## 2. Data Collection

- **Source:** Kaggle dataset with 8 columns and 1000 rows.
- **Features:**
  - gender
  - race/ethnicity
  - parental level of education
  - lunch
  - test preparation course
  - math score
  - reading score
  - writing score

---

## 3. Data Checks

- Checked for missing values and duplicates (none found).
- Verified data types and unique values.
- Explored statistical summaries (mean, std, min, max, etc.).

---

## 4. Exploratory Data Analysis (EDA)

- Visualized distributions using histograms, KDE plots, and boxplots.
- Performed univariate, bivariate, and multivariate analyses to understand relationships.

**Key Insights:**
- Female students performed better overall, but males scored higher in math.
- Students with standard lunch performed better than those with free/reduced lunch.
- Completing the test preparation course improved scores significantly.

---

## 5. Feature Engineering

- Added new columns: Total Score and Average Score.
- Identified numerical and categorical features for preprocessing.

---

## 6. Data Preprocessing

- Applied one-hot encoding to categorical features.
- Standardized numerical features using `StandardScaler`.
- Combined preprocessing steps using `ColumnTransformer`.

---

## 7. Model Training

- Split data into training and testing sets (80-20 split).
- Trained multiple regression models:
  - Linear Regression
  - Ridge Regression
  - Random Forest Regressor
  - CatBoost Regressor
  - AdaBoost Regressor
- Evaluated models using R² score, MAE, and RMSE.
- **Best Model:** Linear Regression (R² = 88.04%).

---

## 8. Prediction Pipeline

- Built a pipeline to preprocess input data and make predictions using the trained model.
- Saved the model and preprocessor for deployment.

---

## 9. Web Application

- Developed a Flask web app with HTML templates.
- Users input student details; the app predicts math scores and displays results.

---

## 10. Deployment

- Dockerized the application for portability.
- **AWS Deployment:**
  - Used EC2 to host the container.
  - Stored Docker images in ECR.
  - Managed credentials and automation with IAM and GitHub Actions.
  - Automated CI/CD pipeline with GitHub Actions and self-hosted runner on EC2.
  - Exposed port 8080 for web access.

---

## 11. Cloud Automation

- **CI/CD:**  
  Code pushed to GitHub triggers tests, Docker build, image push to ECR, and deployment to EC2.
- **Secrets Management:**  
  AWS credentials and ECR details managed via GitHub Secrets.

---

## 12. Cleanup

- Steps to terminate EC2, delete ECR repo, remove IAM user, and clean up GitHub runner after testing.

---

## Summary

This project demonstrates a complete ML workflow from data analysis to cloud deployment, providing a robust, automated system for predicting student math performance based on multiple input features.