# Fraudulent job postings prediction

## Overview
Nowadays, the digital Job Market has been flooded with fraudulent job postings. These frauds can come in many different ways, and are sometimes difficult to spot. There is a need of tools to help job seekers identify job positions that are likely scams, and prevent them to being eposed to malicious intentions. This can be achieved through proper training of a Classification Machine Learning Model that incorporates Natural Language Processing (NLP) techniques. The final product of this project is an interactive web application, in which the users can input the information from the job posting and will get as a response how likely it is to be legitimate or not. 

This project was developed as part of the final assessment of the Machine Learning course at ReDI Hamburg (Spring 2024 class).

## Data source
The original dataset was retrieved from Kaggle (link [here](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)). It comprises of aroun 18K job descriptions, out of which 800 are fake, consisting of both textual information and meta-information about the jobs. 

## Tools
+ Python (main libraries: pandas, numPy, seaborn, nltk and sklearn)
+ Jupyter notebook
+ Streamlit

## Steps
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


