import pickle 
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('cervical_cancer.sav', 'rb'))

# Judul web
st.title('Predicted Risk of Cervical Cancer')

col1, col2, col3 = st.columns(3)
with col1:
    behavior_sexualRisk = st.text_input('Behavior Sexual Risk')
with col2:
    behavior_eating = st.text_input('Behavior Eating')
with col3:
    behavior_personalHygine = st.text_input('Behavior Personal Hygiene')
with col1:
    intention_aggregation = st.text_input('Intention Aggregation')
with col2:
    intention_commitment =st.text_input('Intention Commitment')
with col3:
    attitude_consistency = st.text_input('Attitude Consistency')
with col1:
    attitude_spontaneity = st.text_input('Attitude Spontaneity')
with col2:
    norm_significantPerson = st.text_input('Norm Significant Person')
with col3:
    norm_fulfillment = st.text_input('Norm Fulfillment')
with col1:
    perception_vulnerability = st.text_input('Perception Vulnerability')
with col2:
    perception_severity = st.text_input('Perception Severity')
with col3:
    motivation_strength = st.text_input('Motivation Strength')
with col1:
    motivation_willingness = st.text_input('Motivation Willingness')
with col2:
    socialSupport_emotionality = st.text_input('Social Support Emotionality')
with col3:
    socialSupport_appreciation = st.text_input('Social Support Appreciation')
with col1:
    socialSupport_instrumental = st.text_input('Social Support Instrumental')
with col2:
    empowerment_knowledge = st.text_input('Empowerment Knowledge')
with col3:
    empowerment_abilities = st.text_input('Empowerment Abilities')
with col1:
    empowerment_desires = st.text_input('Empowerment Desires')

# code for prediction
cervical_cancer_diagnosis =''

# membuat tombol prediksi
if st.button('Prediction Results'):
    cervical_cancer_prediction = model.predict([[behavior_sexualRisk, behavior_eating, behavior_personalHygine, intention_aggregation, intention_commitment, attitude_consistency, attitude_spontaneity, norm_significantPerson, norm_fulfillment, perception_vulnerability, perception_severity, motivation_strength, motivation_willingness, socialSupport_emotionality, socialSupport_appreciation, socialSupport_instrumental, empowerment_knowledge, empowerment_abilities, empowerment_desires]])

    if (cervical_cancer_prediction[0]==1):
        cervical_cancer_diagnosis = 'Patient at Risk for Cervical Cancer'
    else: 
        cervical_cancer_diagnosis = 'Patient is Not at Risk for Cervical Cancer'
    st.success(cervical_cancer_diagnosis)
