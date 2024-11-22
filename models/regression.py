import streamlit as st


def show_regression_models():
    st.header("Select a Regression Model")

    regression_model = st.radio("Choose a regression model:",
                                ["XGBoost", "KNeighbors", "Random Forest",
                                 "LightGBM", "Linear Regression",
                                 "Decision Tree", "Support Vector Regression"])

    if regression_model == "XGBoost":
        st.markdown("""
        ### XGBoost Regressor
        In this project, an XGBoost model was implemented to predict CO2 emissions (Ewltp) based on the provided 
        dataset. The dataset was split into training and testing sets with an 80:20 ratio. After preprocessing and 
        normalizing the data using StandardScaler, hyperparameter tuning was performed using GridSearchCV. 
        The optimal parameters determined through this process included the use of 300 trees with a maximum depth of 7, 
        a learning rate of 0.2, and utilization of 80% of features and 100% of samples for each tree.

        The model's performance was evaluated using Mean Squared Error (MSE) and the R-squared coefficient (R²). 
        The achieved MSE was 35.82, indicating high accuracy in predicting CO2 emissions. The R² value of 0.9887 
        demonstrates that approximately 98.87% of the variation in CO2 emissions can be explained by the model. 
        The model's performance on the training set showed an R² of 0.9955, demonstrating a good fit to the data.

        These results confirm the high effectiveness of the XGBoost model in predicting CO2 emissions and its capability 
        to provide precise analysis, which is a significant contribution to the project focused on assessing the 
        environmental impact of vehicles.
        """)

    elif regression_model == "KNeighbors":
        st.markdown("""
        ### KNeighbors Regressor
        """)

    elif regression_model == "Random Forest":
        st.markdown("""
        ### Random Forest Regressor
        """)

    elif regression_model == "LightGBM":
        st.markdown("""
        ### LightGBM Regressor
        """)

    elif regression_model == "Linear Regression":
        st.markdown("""
        ### Linear Regression
        """)

    elif regression_model == "Decision Tree":
        st.markdown("""
        ### Decision Tree Regressor
        """)

    elif regression_model == "Support Vector Regression":
        st.markdown("""
        ### Support Vector Regression
        """)

