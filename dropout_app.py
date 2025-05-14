import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing
from prediction import prediction


col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=130)
with col2:
    st.header('Status prediction app (Prototype)')


input_data = {
    "Age_at_enrollment": int(st.number_input(label='Age_at_enrollment', value=23)),
    "Previous_qualification_grade": float(st.number_input(label='Previous_qualification_grade', value=3)),
    "Admission_grade": float(st.number_input(label='Admission_grade', value=4)),
    "Curricular_units_1st_sem_enrolled": int(st.number_input(label='Curricular_units_1st_sem_enrolled', value=4)),
    "Curricular_units_1st_sem_credited": int(st.number_input(label='Curricular_units_1st_sem_credited', value=3)),
    "Curricular_units_1st_sem_evaluations": int(st.number_input(label='Curricular_units_1st_sem_evaluations', value=7)),
    "Curricular_units_1st_sem_approved": int(st.number_input(label='Curricular_units_1st_sem_approved', value=3)),
    "Curricular_units_1st_sem_without_evaluations": int(st.number_input(label='Curricular_units_1st_sem_without_evaluations', value=0)),
    "Curricular_units_1st_sem_grade": float(st.number_input(label='Curricular_units_1st_sem_grade', value=110.0)),
    "Curricular_units_2nd_sem_enrolled": int(st.number_input(label='Curricular_units_2nd_sem_enrolled', value=4)),
    "Curricular_units_2nd_sem_credited": int(st.number_input(label='Curricular_units_2nd_sem_credited', value=3)),
    "Curricular_units_2nd_sem_evaluations": int(st.number_input(label='Curricular_units_2nd_sem_evaluations', value=7)),
    "Curricular_units_2nd_sem_approved": int(st.number_input(label='Curricular_units_2nd_sem_approved', value=3)),
    "Curricular_units_2nd_sem_without_evaluations": int(st.number_input(label='Curricular_units_2nd_sem_without_evaluations', value=0)),
    "Curricular_units_2nd_sem_grade": float(st.number_input(label='Curricular_units_2nd_sem_grade', value=100.0)),
}
 
data = pd.DataFrame(input_data)


col1, col2, col3 = st.columns(3)
 
with col1:
       
    Age_at_enrollment = int(st.number_input(label='Age_at_enrollment', value=23))
    data["Age_at_enrollment"] = Age_at_enrollment
 
with col2:
    Previous_qualification_grade = float(st.number_input(label='Previous_qualification_grade', value=100.0))
    data["Previous_qualification_grade"] = Previous_qualification_grade
 
with col3:
    Admission_grade = float(st.number_input(label='Admission_grade', value=100.0))
    data["Admission_grade"] = Admission_grade
 
 
 
col1, col2, col3 = st.columns(3)
 
with col1:
    Curricular_units_1st_sem_enrolled = int(st.number_input(label='Curricular_units_1st_sem_enrolled', value=4))
    data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled
 
with col2:
    # st.header("Kolom 1")
    Curricular_units_1st_sem_credited = int(st.number_input(label='Curricular_units_1st_sem_credited', value=3))
    data["Curricular_units_1st_sem_credited"] = Curricular_units_1st_sem_credited
 
with col3:
    Curricular_units_1st_sem_evaluations = int(st.number_input(label='Curricular_units_1st_sem_evaluations', value=7))
    data["Curricular_units_1st_sem_evaluations"] = Curricular_units_1st_sem_evaluations



col1, col2, col3 = st.columns(3)
with col1:
    Curricular_units_1st_sem_approved = int(st.number_input(label='Curricular_units_1st_sem_approved', value=3))
    data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved
 
with col2:
    Curricular_units_1st_sem_without_evaluations = int(st.number_input(label='Curricular_units_1st_sem_without_evaluations', value=0))
    data["Curricular_units_1st_sem_without_evaluations"] = Curricular_units_1st_sem_without_evaluations
 
with col3:
    Curricular_units_1st_sem_grade = float(st.number_input(label='Curricular_units_1st_sem_grade', value=11.27))
    data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade
 



col1, col2, col3 = st.columns(3)
 
with col1:
    Curricular_units_2nd_sem_enrolled = int(st.number_input(label='Curricular_units_2nd_sem_enrolled', value=4))
    data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled
 
with col2:
    # st.header("Kolom 1")
    Curricular_units_2nd_sem_credited = int(st.number_input(label='Curricular_units_2nd_sem_credited', value=3))
    data["Curricular_units_2nd_sem_credited"] = Curricular_units_2nd_sem_credited
 
with col3:
    Curricular_units_2nd_sem_evaluations = int(st.number_input(label='Curricular_units_2nd_sem_evaluations', value=7))
    data["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations



col1, col2, col3 = st.columns(3)
with col1:
    Curricular_units_2nd_sem_approved = int(st.number_input(label='Curricular_units_2nd_sem_approved', value=3))
    data["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved
 
with col2:
    Curricular_units_2nd_sem_without_evaluations = int(st.number_input(label='Curricular_units_2nd_sem_without_evaluations', value=0))
    data["Curricular_units_2nd_sem_without_evaluations"] = Curricular_units_2nd_sem_without_evaluations
 
with col3:
    Curricular_units_2nd_sem_grade = float(st.number_input(label='Curricular_units_2nd_sem_grade', value=11.27))
    data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade
 

 
with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)


if st.button('Predict'):
    st.write("Cek data sebelum preprocessing:")
    st.dataframe(data)
    st.write("Apakah ada null?:", data.isnull().any())
    if data.empty or data.isnull().any().any():
        st.error("Data tidak lengkap atau ada kesalahan input. Silakan periksa kembali semua isian.")
    else:
        new_data = data_preprocessing(data=data)
        with st.expander("View the Preprocessed Data"):
            st.dataframe(data=new_data, width=800, height=10)
        st.write("Status prediction: {}".format(prediction(new_data)))
    # new_data = data_preprocessing(data=data)
    # with st.expander("View the Preprocessed Data"):
    #     st.dataframe(data=new_data, width=800, height=10)
    # st.write("Status prediction: {}".format(prediction(new_data)))

    
