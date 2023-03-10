import streamlit as st
st.title('medical diagnostic web app')
st.title('is the patient diabetic?' )
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler


#load the pickled model
model=open('rfc.pickle','rb')
clf=pickle.load(model)
model.close()

#step2: get the input from front end user
pregs=st.number_input('Pregnancies',0,17,0)
Glucose=st.slider('Glucose',40,200,40)
bp=st.slider('BloodPressure',20,140,20)
skin=st.slider('SkinThickness',7.0,99.0,7.0)
insulin=st.slider('Insulin',14,850,14)
bmi=st.slider('BMI',18,67,18)
dpf=st.slider('DiabetesPedigreeFunction',0.05,2.50,0.05)
age=st.slider('Age',21,82,21)

#step 3:collect the front end user input as model input data

data={'Pregnancies':pregs,'Glucose':Glucose,'BloodPressure':bp,'SkinThickness':skin,'Insulin':insulin,'BMI':bmi,
      'DiabetesPedigreeFunction':dpf,
     'Age':age}
input_data=pd.DataFrame([data])

#step 4: get the predictions and print the results
preds = clf.predict(input_data)[0]
if st.button('predict'):
    if preds==1:
        st.error('Diabetic')
    if preds==0:
        st.success('non-diabetic')
