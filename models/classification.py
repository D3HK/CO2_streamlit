import streamlit as st


def show_classification_models():
    st.header("Select a Classification Model")
    classification_model = st.radio(
        "Choose a classification model:", ["Logistic Regression", "Random Forest Classifier"]
    )

    if classification_model == "Logistic Regression":
        st.markdown("""
        ### Logistic Regression
        The Logistic Regression model implemented for the CO2 emission classification task demonstrates a high level of 
        accuracy. With an accuracy score of 97.05%, the model is proficient in correctly classifying the emission levels 
        into low, medium, and high categories. Such performance indicates a strong prediction capability across 
        the dataset, suggesting that the logistic regression handles the given categorical transformation and feature 
        set effectively.

        In terms of precision, recall, and F1 score, the model yields consistently high values of 97.03%, 97.05%, 
        and 97.04%, respectively. High precision implies that the model makes a few false positive predictions, 
        while the high recall signifies that it identifies most of the true positive instances accurately. The F1 score, 
        being the harmonic mean of precision and recall, further corroborates the balance achieved in capturing both 
        false positives and false negatives. Thus, this evaluation reinforces the robustness of the logistic regression 
        model in handling multi-class classification problems.

        The confusion matrix reveals the prediction distribution across the actual and predicted categories. 
        The counts on the diagonal represent correct predictions, indicating a large number of accurately classified 
        instances across all emission categories. However, there are some confusions observed, especially between the 
        'low' and 'high' emission categories, which could be due to overlapping characteristics in the feature space.

        graphs: confusion matrix heatmap
        """)
    elif classification_model == "Random Forest Classifier":
        st.markdown("""
        ### Random Forest Classifier
        The Random Forest Classifier model was utilized in this project to classify CO2 emissions into categories based 
        on their levels: low, medium, and high. The dataset was preprocessed by discretizing the emissions into these 
        defined categories and encoding them numerically for model training. Subsequently, the data was split into 
        training and testing sets to evaluate the model's performance accurately.

        In terms of model evaluation, the Random Forest achieved a high level of performance, 
        with an accuracy of 99.43%. Precision, recall, and F1 scores were similarly high, indicating that the model 
        is effectively classifying CO2 emission levels with minimal error rates. The confusion matrix reflects 
        a low number of misclassifications, reinforcing the model's robustness in categorizing the data accurately.
        """)

