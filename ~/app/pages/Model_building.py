import streamlit as st
#from kmodes.kmodes import KModes
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import  base64
import pickle

st.header("WAEC & JAMB Exam Challenges Prediction")

trained_model = pickle.load(open(
    'kmodes_model.pkl', 'rb'))

# Image For Page
file_ = open("image.png", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()


import streamlit as st

# Function to make predictions
def generate_prediction(data):
    prediction = trained_model.predict(data)
    # Customize the output based on the prediction result
    if prediction[0] == 'Success':
        return 'The student is predicted to succeed in the exam'
    else:
        return 'The student is predicted to face challenges in the exam'

# Main app interface
st.title('WAEC & JAMB Exam Challenges Prediction')

# Input fields for prediction variables
try:
    gender = st.selectbox('Gender', ['Male', 'Female'])
    age = st.selectbox('Age Group', ['15-17 years', '18-20 years', '21-23 years', '24 years or older'])
    school = st.selectbox('School Type', ['Private School', 'Public School'])
    exam = st.selectbox('Exam Type', ['WAEC', 'JAMB', 'Both WAEC and JAMB'])
    location = st.selectbox('Location', ['Urban area', 'Rural area', 'Semi-urban area'])
    guardians_education = st.selectbox("Guardian's Education Level", ['Primary education', 'Secondary education', 'Tertiary education (e.g., university, polytechnic)', 'No formal education'])
    exam_readiness = st.selectbox('Exam Readiness', ['Very well prepared', 'Somewhat prepared', 'Not well prepared', 'Not prepared at all'])
    exam_preparation = st.selectbox('Exam Preparation Level', ['Extremely stressful', 'Moderately stressful', 'Not stressful'])
    after_school_study = st.selectbox('After School Study', ['Every day', 'A few times a week', 'Occasionally', 'Rarely or never'])
    exam_guidance = st.selectbox('Exam Guidance Availability', ['Very easy to access', 'Somewhat easy to access', 'Difficult to access', 'Not available at all'])
    exam_confidence = st.selectbox('Exam Confidence Level', ['Very confident', 'Somewhat confident', 'Not confident', 'Unsure'])
    health_issues = st.selectbox('Health Issues', ['Yes', 'No'])
    family_support = st.selectbox('Family Support', ['Very supportive', 'Somewhat supportive', 'Not supportive', 'Indifferent'])

    prediction_result = ""

    # Prediction code
    if st.button('Predict'):
        prediction_result = generate_prediction([[gender, age, school, exam, location, guardians_education, 
                                                  exam_readiness, cbt_technical_issues, exam_preparation, 
                                                  after_school_study, exam_guidance, exam_confidence, 
                                                  health_issues, family_support]])
except Exception as e:
    st.error(f"Error: {e}")

st.success(prediction_result)
