import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing
from prediction import prediction


col1, col2 = st.columns([1, 5])
with col1:
    st.image("Prediksi_logo.png", width=100)
with col2:
    st.header('Status prediction app (Prototype)')


input_data={}

col1, col2, col3 = st.columns(3)

with col1:
    input_data['Age_at_enrollment'] = int(st.number_input(label='Age_at_enrollment', value=23))

with col2:
    input_data['Previous_qualification_grade'] = float(st.number_input(label='Previous_qualification_grade', value=100.0))

with col3:
    input_data['Admission_grade'] = float(st.number_input(label='Admission_grade', value=100.0))


col1, col2, col3 = st.columns(3)

with col1:
    input_data['Curricular_units_1st_sem_enrolled'] = int(st.number_input(label='Curricular_units_1st_sem_enrolled', value=4))

with col2:
    input_data['Curricular_units_1st_sem_credited'] = int(st.number_input(label='Curricular_units_1st_sem_credited', value=3))

with col3:
    input_data['Curricular_units_1st_sem_evaluations'] = int(st.number_input(label='Curricular_units_1st_sem_evaluations', value=7))


col1, col2, col3 = st.columns(3)
with col1:
    input_data['Curricular_units_1st_sem_approved'] = int(st.number_input(label='Curricular_units_1st_sem_approved', value=3))

with col2:
    input_data['Curricular_units_1st_sem_without_evaluations'] = int(st.number_input(label='Curricular_units_1st_sem_without_evaluations', value=0))

with col3:
    input_data['Curricular_units_1st_sem_grade'] = float(st.number_input(label='Curricular_units_1st_sem_grade', value=11.27))


col1, col2, col3 = st.columns(3)

with col1:
    input_data['Curricular_units_2nd_sem_enrolled'] = int(st.number_input(label='Curricular_units_2nd_sem_enrolled', value=4))

with col2:
    input_data['Curricular_units_2nd_sem_credited'] = int(st.number_input(label='Curricular_units_2nd_sem_credited', value=3))

with col3:
    input_data['Curricular_units_2nd_sem_evaluations'] = int(st.number_input(label='Curricular_units_2nd_sem_evaluations', value=7))


col1, col2, col3 = st.columns(3)
with col1:
    input_data['Curricular_units_2nd_sem_approved'] = int(st.number_input(label='Curricular_units_2nd_sem_approved', value=3))

with col2:
    input_data['Curricular_units_2nd_sem_without_evaluations'] = int(st.number_input(label='Curricular_units_2nd_sem_without_evaluations', value=0))

with col3:
    input_data['Curricular_units_2nd_sem_grade'] = float(st.number_input(label='Curricular_units_2nd_sem_grade', value=11.27))
 

data = pd.DataFrame([input_data])

with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)


if st.button('Predict'):
    if data.empty or data.isnull().any().any():
        st.error("Data tidak lengkap atau ada kesalahan input. Silakan periksa kembali semua isian.")
    else:
        new_data = data_preprocessing(data=data)
        with st.expander("View the Preprocessed Data"):
            st.dataframe(data=new_data, width=800, height=10)
        st.write("Status prediction: {}".format(prediction(new_data)))

    
