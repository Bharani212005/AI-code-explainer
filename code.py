import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AQ.Ab8RN6K2NPfayBv_2oHIiODJG7I3EU_WKhuQxy9as_wEP6J7gQ")
model=genai.GenerativeModel("gemini-2.5-flash")
qns=st.text_input("Enter the question:")
if st.button("submit"):
    res=model.generate_content(qns+"you want to explaine the given code")
    st.write(res.text)