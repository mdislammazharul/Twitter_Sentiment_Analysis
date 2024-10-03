import streamlit as st
import pickle
import time

st.title("Twitter Sentiment Analysis")

model = pickle.load(open('twitter_sentiment.pkl', 'rb'))

tweet = st.text_input("Enter the Tweet Here")

submit = st.button("Predict")

if submit:
    start = time.time()
    prediction = model.predict([tweet])
    end = time.time()
    st.write('Prediction time taken: ', round(end-start, 2), 'seconds')
    print(prediction[0])
    st.write("Predicted Sentiment is: ", prediction[0])