import numpy as np
import pickle 
import streamlit as st

# Load the machine learning model
loaded_model = pickle.load(open('lc.pkl', 'rb'))

# Set the title and page layout
st.title('Lung Cancer Checkup')
st.markdown(
    """
    <style>
    .main-container {
        background-color: #f7f7f7;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
    }
    .results-container {
        margin-top: 2rem;
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
    }
    .header {
        text-align: center;
        font-size: 24px;
        margin-bottom: 1rem;
        color: #333333;
        font-weight: bold;
    }
    .subheader {
        font-size: 18px;
        margin-top: 1.5rem;
        color: #666666;
    }
    .result-message {
        font-size: 24px;
        margin-top: 1.5rem;
        text-align: center;
        font-weight: bold;
    }
    .safe-message {
        color: #1ca745;
    }
    .affected-message {
        color: #e53935;
    }
    .footer {
        text-align: center;
        color: #888888;
        margin-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Input fields for user data
with st.container():
    st.markdown("<div class='header'>User Information</div>", unsafe_allow_html=True)
with st.form("user_input_form"):
    col1, col2 = st.columns(2)  # Divide the container into two columns
    with col1:
        AGE = st.number_input("Age")
        GENDER = st.selectbox("Gender", ("Male", "Female"))
        if GENDER == "Male":
            GENDER = 0
        else:
            GENDER = 1
        SMOKING = st.selectbox("Smoking", ("No", "Yes"))
        if SMOKING == "Yes":
            SMOKING = 2
        else:
            SMOKING = 1
        YELLOW_FINGERS = st.selectbox("Yellow Fingers", ("No", "Yes"))
        if YELLOW_FINGERS == "Yes":
            YELLOW_FINGERS = 2
        else:
            YELLOW_FINGERS = 1        
        ANXIETY = st.selectbox("Anxiety", ("No", "Yes"))
        if ANXIETY == "Yes":
            ANXIETY = 2
        else:
            ANXIETY = 1        
    with col2:
        PEER_PRESSURE = st.selectbox("Peer Pressure", ("No", "Yes"))
        if PEER_PRESSURE == "Yes":
            PEER_PRESSURE = 2
        else:
            PEER_PRESSURE = 1        
        CHRONIC_DISEASE = st.selectbox("Chronic Disease", ("No", "Yes"))
        if CHRONIC_DISEASE == "Yes":
            CHRONIC_DISEASE = 2
        else:
            CHRONIC_DISEASE = 1
        FATIGUE = st.selectbox("Fatigue", ("No", "Yes"))
        if FATIGUE == "Yes":
            FATIGUE = 2
        else:
            FATIGUE = 1        
        ALLERGY = st.selectbox("Allergy", ("No", "Yes"))
        if ALLERGY == "Yes":
            ALLERGY = 2
        else:
            ALLERGY = 1        
        WHEEZING = st.selectbox("Wheezing", ("No", "Yes"))
        if WHEEZING == "Yes":
            WHEEZING = 2
        else:
            WHEEZING = 1
    # Additional input fields
    ALCOHOL_CONSUMING = st.selectbox("Alcohol Consumption", ("No", "Yes"))
    if ALCOHOL_CONSUMING == "Yes":
        ALCOHOL_CONSUMING = 2
    else:
        ALCOHOL_CONSUMING = 1
    COUGHING = st.selectbox("Cough", ("No", "Yes"))
    if COUGHING == "Yes":
        COUGHING = 2
    else:
        COUGHING = 1
    SHORTNESS_OF_BREATH = st.selectbox("Shortness of Breath", ("No", "Yes"))
    if SHORTNESS_OF_BREATH == "Yes":
        SHORTNESS_OF_BREATH = 2
    else:
        SHORTNESS_OF_BREATH = 1
    SWALLOWING_DIFFICULTY = st.selectbox("Swallowing Difficulty", ("No", "Yes"))
    if SWALLOWING_DIFFICULTY == "Yes":
        SWALLOWING_DIFFICULTY = 2
    else:
        SWALLOWING_DIFFICULTY = 1
    CHEST_PAIN = st.selectbox("Chest Pain", ("No", "Yes"))
    if CHEST_PAIN  == "Yes":
        CHEST_PAIN  = 2
    else:
        CHEST_PAIN  = 1
    submit_button = st.form_submit_button(label="Test Results")

# Display results
if submit_button:
    with st.container():
        st.markdown("<div class='header'>Test Results</div>", unsafe_allow_html=True)
        with st.spinner("Analyzing..."):
            classifier = loaded_model.predict([[GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE,ALLERGY,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]])

        result_container = st.container()
        with result_container:
            st.markdown("<div class='subheader'>Diagnosis</div>", unsafe_allow_html=True)
            if classifier[0] == 0:
                st.markdown("<div class='result-message safe-message'>You are SAFE!</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='result-message affected-message'>You might be affected by LUNG CANCER</div>", unsafe_allow_html=True)

# Footer and attribution
st.markdown("<div class='footer'>This app is for educational purposes.</div>", unsafe_allow_html=True)
st.markdown("<div class='footer'>Founder: Santhosh Reddy Padala</div>", unsafe_allow_html=True)

