import streamlit as st
import pandas as pd
import joblib

model = joblib.load('xgb_model.pkl')

st.title("Job Post Fraud Detection")

# User inputs
st.header("Enter the job details:")

title = st.text_input("Job Title", "Data Scientist")
department = st.text_input("Department", "Data and AI")
#company = st.text_input("Company", "Company A")
company_profile =st.text_area("Company profile", "We are a company that...")
description = st.text_area("Job Description", "Analyze data and generate insights...")
requirements = st.text_area("Requirements", "Experience with machine learning and...")
required_experience = st.selectbox("Experience level", ['Internship', 'Not Applicable', 'Mid-Senior level', 'Associate',
                                                         'Entry level', 'Executive', 'Director'])
benefits = st.text_area("Benefits", "Paid Holidays, health insurance...")
industry = st.text_area("Industry", "Information Technology")
function = st.text_area("Function", "Engineering")
employment_type = st.selectbox("Employment Type", ['Other', 'Full-time', 'Part-time', 'Contract', 'Temporary'])
required_education = st.selectbox("Education requirement", ["Bachelor's Degree", "Master's Degree", 'High School or equivalent',
                                                                'Unspecified', 'Some College Coursework Completed', 'Vocational',
                                                                'Certification', 'Associate Degree', 'Professional', 'Doctorate',
                                                                'Some High School Coursework', 'Vocational - Degree',
                                                                'Vocational - HS Diploma'])
telecommuting = st.selectbox("Telecommuting", ["Yes", "No"])
has_company_logo = st.selectbox("Company has logo?", ["Yes", "No"])
has_questions = st.selectbox("Company asks questions?", ["Yes", "No"])

# Make a prediction
if st.button("Predict"):
    with st.spinner("Predicting..."):
    # Create a dataframe for the input
        input_data = pd.DataFrame({
            'title': [title],
            'department': [department],
            'company_profile': [company_profile],
            'description': [description],
            'requirements' : [requirements],
            'required_experience' : [required_experience],
            'benefits' : [benefits],
            'industry' : [industry],
            'function' : [function],
            'employment_type': [employment_type],
            'required_education' : [required_education],
            'has_questions' : [has_questions],
            'telecommuting' :  [telecommuting],
            'has_company_logo' : [has_company_logo]
            })
        
        # Creating text column
        columns_to_concat = columns_to_concat = ['title', 'department','company_profile', 'description', 'requirements', 'benefits', 'industry', 'function']
        input_data['text'] = input_data[columns_to_concat].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
        
        prediction = model.predict(input_data)[0]
        prediction_proba = model.predict_proba(input_data)[0]
        
        st.subheader("Prediction")
        if prediction == 1:
            st.write("The job posting is likely to be fraudulent.")
        else:
            st.write("The job posting is likely to be legitimate.")

    st.subheader("Prediction Probabilities:")
    st.write(f"Legitimate: {prediction_proba[0]:.2f}")
    st.write(f"Fraudulent: {prediction_proba[1]:.2f}")