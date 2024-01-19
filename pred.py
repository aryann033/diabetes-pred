import streamlit as stlite
import numpy as np
import pandas as pd
import pickle
from streamlit_option_menu import option_menu
data = pd.read_csv(r'C:\Users\DELL\Downloads\diabetes\diabetes.csv')

selected = option_menu(
    menu_title=None,
    options=["Predict Diabetes","Contribute to our Dataset"],
    icons=["search","search","book"],
    menu_icon= "cast",
    default_index=0,
    orientation="horizontal",
)

if selected == "Predict Diabetes":
    stlite.title("DIABETES PREDICTION APP")
    Pregnancies = stlite.number_input("Pregnancies", min_value=0, max_value=100, step=1)
    Glucose = stlite.number_input("Glucose", min_value=0, max_value=200, step=1)
    Bp = stlite.number_input("Bp", min_value=0, max_value=100, step=1)
    Skinthickness = stlite.number_input("Skinthickness", min_value=0, max_value=100, step=1)
    Insulin = stlite.number_input("Insulin", min_value=0, max_value=100, step=1)
    Bmi = stlite.number_input("Bmi", min_value=0.0, max_value=100.0, step=0.1)
    Dpf = stlite.number_input("Diabetes Prediction Function", min_value=0.000, max_value=100.000, step=0.001,format="%0.3f")
    Age = stlite.number_input("Age", min_value=0, max_value=100, step=1)

    pred= ([[Pregnancies, Glucose, Bp, Skinthickness, Insulin, Bmi, Dpf, Age]])

    if stlite.button("Predict"):
        stlite.write(pred)
        if pred[0] == 1:
            stlite.write("The person is diabetic")
        if pred[0] == 0:
            stlite.write("The person is not diabetic")

if selected == "Contribute to our Dataset":

    stlite.header("Contribute to our Dataset")
    Preg = stlite.number_input("Enter Pregnancies",0,20)
    Gluc = stlite.number_input("Enter Glucose",0,200,step=20)
    Bp = stlite.number_input("Enter Bp",0,200)
    Skinth = stlite.number_input("Enter Skinthickness", 0.00,100.00,step=10.0)
    Ins = stlite.number_input("Enter Insulin",0,20)
    Bmi = stlite.number_input("Enter Bmi",0.00,100.00, step=10.0)
    Dpf = stlite.number_input("Enter Diabetes Prediction Function",0.00,100.00)
    Age = stlite.number_input("Enter Age",0,100, step=1)
    out = stlite.number_input("Output(0 or 1)",0,1)

    if stlite.button("Submit"):
        to_add = {"Pregnancies":[Preg], "Glucose":[Gluc], "Bp":[Bp], "Skinthickness":[Skinth], "Insulin":[Ins], "Bmi":[Bmi], "Diabetes Prediction Function":[Dpf], "Age":[Age], "Outcome":[out]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv(r'C:\Users\DELL\Downloads\diabetes\diabetes.csv', mode='a', header=False, index= False)
        stlite.success("Submitted")
    if  stlite.checkbox("Show Table"):
        stlite.table(data) 
