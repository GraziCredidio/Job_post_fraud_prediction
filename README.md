# Fraudulent job postings prediction

## Overview
Nowadays, the digital Job Market has been flooded with fraudulent job postings. These frauds can come in many different ways, and are sometimes difficult to spot. There is a need of tools to help job seekers identify job positions that are likely scams, and prevent them to being eposed to malicious intentions. This can be achieved through proper training of a Classification Machine Learning Model that incorporates Natural Language Processing (NLP) techniques. The final product of this project is an interactive web application, in which the users can input the information from the job posting and will get as a response how likely it is to be legitimate or not. 

## Data source
The original dataset was retrieved from Kaggle (link [here](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)). It comprises of aroun 18K job descriptions, out of which 800 are fake, consisting of both textual information and meta-information about the jobs. 

## Methodology and technical stack
Stop words were removed and text features were lemmatized using `nltk`. The TF-IDF algorithm from `sklearn` was used for text vectorization. Categorical variables were one-hot encoded. Train-test split was done with a 0.3 ratio. Training dataset was balanced through random oversampling with `imblearn`. The performances of Logistic regression, Random Forest, Multinomial Naive Bayes, Support Vector Machine and XGBoost classification models were analyzed through metrics of accuracy, precision, recall and F1-score. Confusion matrices were displayed as visual aids of model performance evaluation. The XGBoost model was saved using `joblib` and an easily-shareble web application was constructed with `streamlit`, in which the user can input job postings information and the model predicts its autenticity.

## Development steps
1. Exploratory Data Analysis (EDA)
2. Data cleaning & preprocessing
+ Replacement of NAs
+ Removal of special characters and stop words
+ Tokenization
+ Lemmatization
+ Vectorization (TF-IDF)
3. Train-test split
4. Data balancing (oversampling)
5. Model training
6. Performance evaluation
7. Model deployment to a web application (using Streamlit)

## Installation
