import streamlit as st


def show_neural_network():
    st.header("Neural Network")
    neural_network = st.radio(
        "Choose a classification model:", [
            "Feedforward Neural Network",
            "Multi-class classification"
        ]
    )

    if neural_network == "Feedforward Neural Network":
        st.markdown("""
        ### Feedforward Neural Network
        This project focuses on predicting CO2 emissions using a Feedforward Neural Network (FNN) model. 
        The model is designed with a simple yet effective architecture comprising a two-layer neural network with 
        dropout regularization to prevent overfitting. It uses the 'Ewltp (g/km)' column as the target variable, 
        representing CO2 emissions in grams per kilometer.

        Data preprocessing includes loading the dataset and splitting it into training and testing sets. 
        The model is trained for 20 epochs. It employs the Adam optimizer and mean squared error as the loss function, 
        reflecting its regression-focused design. Throughout the training process, the model's performance improves, 
        as indicated by decreasing loss and mean absolute error (MAE) metrics on both training and validation sets.

        Evaluating the model's performance showed that it achieved a validation loss of 1210.126 and a validation MAE 
        of 30.1204 by the 20th epoch. This demonstrates the model's capacity to learn from the data and make relatively 
        accurate predictions about CO2 emissions, although there is still room for improvement.
        """)

    elif neural_network == "Multi-class classification":
        st.markdown("""
        ### Multi-class classification
        This data science project involves building a neural network model to classify CO2 emissions into categories 
        of low, medium, and high, based on given features from the dataset. The dataset is preprocessed to handle 
        categorical variables and class imbalance, ensuring that the model is trained effectively even with potentially 
        skewed data distributions. Feature normalization is applied to improve model convergence and accuracy.

        The constructed model uses a Sequential neural network architecture with layers designed to capture complex 
        patterns in the data. It consists of two dense layers with 128 and 64 neurons respectively, employing ReLU 
        activation function for non-linearity. Dropout layers with a rate of 0.3 are included for regularization to 
        prevent overfitting, and a softmax activation function is utilized at the output layer to facilitate multi-class 
        classification. The model is compiled with the Adam optimizer and categorical crossentropy loss function.

        During model training, the final test accuracy achieved was 99.68%, suggesting that it effectively learned the 
        patterns of CO2 emissions for the categorized classes. The evaluation metrics further highlighted its 
        performance: the confusion matrix revealed strong predictive accuracy across all classes, with classification 
        report metrics such as precision, recall, and F1-score demonstrating consistent and reliable predictions. 
        For example, the F1-score for the 'high' category was particularly impressive, showcasing the model's ability 
        to correctly classify the majority category.
        """)

        st.image(
            "img/graphs/multi_class.png",
            caption="Confusion matrix heatmap",
        )

