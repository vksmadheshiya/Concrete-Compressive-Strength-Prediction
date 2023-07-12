import streamlit as st
import pandas as pd
import pickle
import joblib
import numpy as np
import pandas as pd

# streamlit framework
st.title('Concrete compressive Strength Predictor')
model = joblib.load('XGBoost_Regressor_model.pkl')

age=st.text_input("Age (in days)")
cement=st.text_input("Cement (in kg) : ")
water=st.text_input("Water (in kg) :")
fa=st.text_input("Fly ash (in kg) :")
sp=st.text_input("Superplasticizer (in kg) :")
bfs=st.text_input("Blast furnace slag (in kg) :")

f_list = [age, cement, water, fa, sp, bfs]

final_features = np.array(f_list).reshape(-1, 6)
df = pd.DataFrame(final_features)



if age and cement and water and fa and sp and bfs:
    if model:
        prediction = model.predict(df)
        result = "%.2f" % round(prediction[0], 2)
        "RESULT" 
        df
        st.write(f" # The predicted compressive strength of the concrete. is '{result}' MPa.")
    else:
        st.write("Some Error Occured")

