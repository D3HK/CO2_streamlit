import streamlit as st


def show_regression_models():
    st.header("Select a Regression Model")

    regression_model = st.radio("Choose a regression model:",
                                [
                                    "XGBoost",
                                    "KNeighbors",
                                    "Random Forest",
                                    "LightGBM",
                                    "Linear Regression",
                                    "Decision Tree",
                                    "Support Vector Regression"
                                ])

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
        
        graphs: Predicted vs. Actual Scatter Plot, Learning Curves
        """)

    elif regression_model == "KNeighbors":
        st.markdown("""
        ### KNeighbors Regressor
        
        The K-Nearest Neighbors (KNN) Regressor model was applied to predict CO2 emissions, specifically targeting the 
        'Ewltp (g/km)' output variable. Initially, the dataset was split into training and testing sets with an 80-20 
        ratio. Data normalization was conducted using a StandardScaler to ensure that all features contribute equally 
        to the distance calculations in the KNN algorithm. The KNN regressor was configured with 2 neighbors, 
        learning from the normalized training data.

        The model demonstrated excellent performance, achieving a training score of 0.9951 and a testing score of 0.9846. 
        These high R-squared values indicate that the model has successfully captured the variability in the data, 
        providing accurate predictions on unseen data. The slight drop in performance from training to test sets 
        suggests a well-balanced model with minimal overfitting, indicating its robustness and reliability in predicting 
        CO2 emissions based on the features provided.
        
        graphs: Scatter Plot, Residuals Plot, Correlation Matrix.
        """)

    elif regression_model == "Random Forest":
        st.markdown("""
        ### Random Forest Regressor
        
        The Random Forest Regressor model was employed to predict CO2 emissions using a given dataset. 
        The dataset was divided into features and target variables, and further split into training and testing sets, 
        maintaining a test size of 20%. The features were normalized to ensure consistent scaling across inputs.

        The model achieved a high R-squared value of 0.988 on the test set, indicating that it explains 98.8% of the 
        variance in CO2 emissions. The Mean Squared Error is 37.937, reflecting the average squared difference between 
        the predicted and actual values.

        The model also shows a high training score of 0.998, suggesting excellent fit on the training data without 
        significant overfitting on the test data. These results demonstrate the model's robust predictive capability 
        and its effectiveness in capturing the underlying patterns related to CO2 emissions.
        
        graphs: Feature Importance Bar Plot, Residuals Plot, Actual vs. Predicted Values Scatter Plot.
        """)

    elif regression_model == "LightGBM":
        st.markdown("""
        ### LightGBM Regressor
        The LightGBM Regressor model is a machine learning algorithm utilized to predict CO2 emissions based on a set 
        of features derived from the dataset. LightGBM is known for its efficiency and speed, especially when dealing 
        with large datasets, making it a suitable choice for this project. The model was trained on a dataset with 
        multiple features, excluding the target variable 'Ewltp (g/km)' and an additional 'Fuel consumption' column. 
        The data was split into training and testing sets, and standardized to enhance the model's performance.

        In evaluating the model's performance, two critical metrics were considered: the Mean Squared Error (MSE) 
        and the R-squared value. The MSE for this model was calculated to be approximately 59.83, indicating the average 
        squared difference between the observed and predicted values. A lower MSE suggests better model performance. 
        The R-squared value of approximately 0.981 signifies a high degree of correlation between the predicted and 
        real values, indicating that the model explains a substantial portion of the variance in the dataset.

        Furthermore, the training score of the model was 0.9827, and the testing score was 0.9811, signifying that 
        the model generalizes well and does not overfit the training data. The relatively close training and testing 
        scores demonstrate the model's stability and reliability in predicting CO2 emissions across unseen data.

        graphs: Feature Importance chart, Residual Plot, Predicted vs. Actual Values plot.
        """)

    elif regression_model == "Linear Regression":
        st.markdown("""
        ### Linear Regression
        The project involves analyzing CO2 emissions using a Linear Regression model to make predictions and evaluate 
        its performance. The dataset was split into features and the target variable, followed by further division 
        into training and testing sets to ensure the robustness of the model validation process.

        The data was standardized using StandardScaler to improve the model's convergence and overall performance. 
        The Linear Regression model was then fitted to the training data to capture the relationship between features and 
        the target variable. After training, predictions were made on the test dataset to assess the model's efficacy.

        The model's performance was evaluated using metrics such as Mean Squared Error (MSE) and R-squared. 
        The Linear Regression model achieved an MSE of 137.24, indicating the average squared difference between 
        predicted and actual values. The R-squared value was approximately 0.957, suggesting that the model explains 
        around 95.7% of the variance in the target variable. Additionally, the training set score was 0.954, and the 
        testing set score was 0.957, illustrating that the model generalizes well to unseen data.

        """)

    elif regression_model == "Decision Tree":
        st.markdown("""
        ### Decision Tree Regressor
        The Decision Tree Regressor is a versatile machine learning model employed in predicting CO2 emissions. 
        In this project, the model was trained and tested using historical emission data. It utilizes a tree-like 
        structure to make predictions based on the input features, thereby capturing non-linear relationships 
        within the data.

        The performance of the Decision Tree Regressor was evaluated using metrics such as Mean Squared Error (MSE) 
        and R-squared (R²). The MSE, calculated at 43.30, indicates the model's average squared difference between 
        the predicted and actual values. A lower MSE is generally favorable, implying that the Decision Tree Regressor 
        makes predictions close to the actual emissions. The R-squared value of 0.9863 suggests a strong fitting 
        performance, highlighting that approximately 98.63% of the variance in CO2 emissions is accounted for by the 
        independent variables in the model.

        Further evaluation of the model shows a perfect score on the training data (Score_Train: 1.0), which might 
        imply overfitting as the model performs slightly less well on the testing data (Score_Test: 0.9863). 
        This signifies that although the model is highly accurate on the data it was trained on, its predictive 
        performance slightly decreases when faced with new, unseen data.

        graphs: Feature Importance Plot, Decision Tree Diagram, Residuals Plot.
        """)

    elif regression_model == "Support Vector Regression":
        st.markdown("""
        ### Support Vector Regression
        The Support Vector Regression (SVR) model is designed to predict CO2 emissions utilizing a dataset with 
        features that are sensitive to scaling. The SVR model, implemented using the scikit-learn library, 
        applies a pipeline to first standardize the input features, ensuring that each feature contributes equally 
        to the result. This preprocessing step is critical for the optimal performance of SVR, which is sensitive 
        to feature scaling.

        The performance of the SVR model is evaluated using multiple metrics, including the Mean Squared Error (MSE) 
        and R-squared (R²). An MSE value of 116.30 indicates the average squared difference between the predicted 
        and actual values. Meanwhile, an R-squared value of 0.963 demonstrates that the model explains approximately 
        96.3% of the variance in the CO2 emissions data, a strong indication of model accuracy and effectiveness.

        Additionally, the score of the SVR model on both training and test datasets is consistent, with values of 
        approximately 0.962 and 0.963, respectively. This consistency suggests that the model has captured the 
        underlying patterns of the training data well and generalizes effectively to unseen data without overfitting.

        graphs: Predicted vs. Actual Values Scatter Plot, Residuals Plot, Error Distribution Histogram.
        """)
