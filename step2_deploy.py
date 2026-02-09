
import os
os.chdir(r'F:\practice\fraud')

import streamlit as st
import pandas as pd
import joblib

model=joblib.load('fraud_detection_pipeline.pkl')

st.title('Fraud Detection App')
st.markdown(":blue[Curious whether a transaction is fraudulent? Enter the transaction details and click *Predict* to find out! :balloon:]")
st.divider()

transaction_type=st.selectbox('Transaction Type',['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'])
amount=st.number_input("Amount",min_value=0.0, value=1000.0)

oldbalanceOrg=st.number_input("Old Balance (Sender)",min_value=0.0, value=1000.0)
newbalanceOrig=st.number_input("New Balance (Sender)",min_value=0.0, value=1000.0)

oldbalanceDest=st.number_input("Old Balance (Receiver)",min_value=0.0, value=1000.0)
newbalanceDest=st.number_input("New Balance (Receiver)",min_value=0.0, value=1000.0)

if st.button("Predict"):
    input_data=pd.DataFrame([{
        "type":transaction_type,
        "amount":amount,
        "oldbalanceOrg":oldbalanceOrg,
        "newbalanceOrig":newbalanceOrig,
        "oldbalanceDest":oldbalanceDest,
        "newbalanceDest":newbalanceDest
        }])
    prediction=model.predict(input_data)[0]
    st.subheader(f"Prediction: '{int(prediction)}'")
    if prediction==1:
        st.error("This transaction can be fraud")
    else:
        st.success("This transaction looks like it is not a fraud")
