import streamlit as st
from transformers import pipeline

# Load sentimental analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

def main():
    st.title("Sentiment Analysis App")

    # Get user input
    user_input = st.text_area("Enter Text for sentiment analysis:")

    if st.button("Analyze Sentiment"):
        if user_input:
            # Analyze Sentiment
            result = sentiment_analyzer(user_input)[0]
            sentiment = result['label']
            confidence = result['score']
            
            #Display results
            st.success(f"Sentiment: {sentiment} (Confidence: {confidence:.2f})")
        else:
            st.warning("Please enter some text for analysis.")
        

if __name__ == "__main__":
    main()

