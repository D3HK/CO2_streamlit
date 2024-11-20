import streamlit as st


def show_classification_models():
    st.header("Select a Classification Model")
    # Using radio buttons for model selection
    classification_model = st.radio(
        "Choose a classification model:", ["Logistic Regression", "Random Forest Classifier"]
    )

    # Executing corresponding code based on the selected classification model
    if classification_model == "Logistic Regression":
        st.write("### Logistic Regression")
        st.write("Description and parameters for Logistic Regression...")
        # Code for Logistic Regression goes here
    elif classification_model == "Random Forest Classifier":
        st.write("### Random Forest Classifier")
        st.write("Description and parameters for Random Forest Classifier...")
        # Code for Random Forest Classifier goes here
