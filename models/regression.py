import streamlit as st


def show_regression_models():
    st.header("Select a Regression Model")
    # Using radio buttons for model selection
    regression_model = st.radio("Choose a regression model:",
                                ["XGBoost", "KNeighbors", "Random Forest",
                                 "LightGBM", "Linear Regression",
                                 "Decision Tree", "Support Vector Regression"])

    # Executing corresponding code based on the selected regression model
    if regression_model == "XGBoost":
        st.write("### XGBoost Regressor")
        st.write("Description and parameters for XGBoost...")
        # Code for XGBoost Regressor goes here
    elif regression_model == "KNeighbors":
        st.write("### KNeighbors Regressor")
        st.write("Description and parameters for KNeighbors...")
        # Code for KNeighbors Regressor goes here
    elif regression_model == "Random Forest":
        st.write("### Random Forest Regressor")
        st.write("Description and parameters for Random Forest...")
        # Code for Random Forest Regressor goes here
    elif regression_model == "LightGBM":
        st.write("### LightGBM Regressor")
        st.write("Description and parameters for LightGBM...")
        # Code for LightGBM Regressor goes here
    elif regression_model == "Linear Regression":
        st.write("### Linear Regression")
        st.write("Description and parameters for Linear Regression...")
        # Code for Linear Regression goes here
    elif regression_model == "Decision Tree":
        st.write("### Decision Tree Regressor")
        st.write("Description and parameters for Decision Tree...")
        # Code for Decision Tree Regressor goes here
    elif regression_model == "Support Vector Regression":
        st.write("### Support Vector Regression")
        st.write("Description and parameters for Support Vector Regression...")
        # Code for Support Vector Regression goes here
