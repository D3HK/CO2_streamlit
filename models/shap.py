import streamlit as st


def show_shap():
    st.markdown("""
    ### SHAP methods
    In our code, we apply various SHAP methods to interpret different machine learning models.

    1. **XGBoost Model SHAP Explanation:**
    
       We use SHAP to explain the XGBoost model. We create an explainer object using `shap.Explainer` and calculate 
       SHAP values on the training dataset `X_train`. The summary plot shows the overall impact of each feature on the 
       model's predictions, helping us identify which features most significantly influenced the XGBoost model's output.
    
    2. **Feedforward Neural Network SHAP Explanation:**
       
       For our feedforward neural network model (FNN), we calculate SHAP values using `shap.KernelExplainer`, which is 
       suitable for any non-tree-based models. We compute SHAP values for a subsample of the test data. The summary plot 
       visually represents the influence of each feature on the model's prediction.
    
    3. **Random Forest Classifier SHAP Visualization:**
    
       We apply SHAP to our Random Forest Classifier model using `shap.TreeExplainer`, specific for tree-based models, to 
       calculate SHAP values for the test dataset. The resulting summary plot provides insight into feature importance 
       and their impacts on the predicted class target.
    
    4. **Logistic Regression SHAP Explanation:**
    
       For the logistic regression model, we use `shap.LinearExplainer` to compute SHAP values for the test data. The 
       summary plot illustrates how each feature influences and interacts with the model's output.
    
    In all these cases, SHAP enhances model interpretability by showing which features contribute the most to variations 
    in predictions, allowing us to gain deeper insights into how the model makes decisions.
    """)
