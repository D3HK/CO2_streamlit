import streamlit as st
from models import regression, classification, nn_regression, nn_classification, shap


def show_introduction():
    st.title("CO2 Emissions Project")
    st.write("Climate change is one of the most pressing environmental issues facing humanity in the 21st century. "
             "It is driven by the increased concentration of greenhouse gases in the atmosphere, "
             "primarily carbon dioxide (CO2), which is generated from the burning of fossil fuels such as coal, oil, "
             "and natural gas. These emissions contribute to the greenhouse effect, which leads to global warming. "
             "Climate change is already impacting weather patterns, "
             "causing extreme natural phenomena such as hurricanes, "
             "floods, and droughts, while also resulting in biodiversity loss and the degradation of ecosystems.\n\n"

             "CO2 emissions negatively affect the environment by influencing ecological systems and human health. "
             "Rising temperatures lead to the melting of glaciers and an increase in sea levels, "
             "threatening coastal regions and island ecosystems. Additionally, climate change induces shifts in "
             "species distribution, which may result in the extinction of some species while others may find "
             "themselves in new, uncharted conditions. Furthermore, agricultural conditions are deteriorating: "
             "changes in precipitation and temperature can significantly reduce crop yields and food quality. "
             "Thus, the issue of climate change demands urgent and coordinated measures to reduce CO2 "
             "emissions and preserve our planet for future generations.")

    st.image(
        "img/CO2_1940-2023.png",
        caption="Annual carbon dioxide (CO₂) emissions worldwide from 1940 to 2023 // © Statista 2024",
        width=800
    )
    st.write("This chart illustrates the dynamics of annual carbon dioxide (CO₂) emissions worldwide "
             "from 1940 to 2023. As seen in the graph, CO₂ emissions have significantly increased since "
             "the mid-20th century, a trend that correlates with industrialization, population growth, "
             "and an increase in the consumption of hydrocarbon resources. The most pronounced rise in "
             "emissions has occurred in recent decades, coinciding with peaks in economic development "
             "and urbanization. This trend raises serious concerns regarding climate change and its consequences "
             "for ecosystems and human health. Therefore, understanding the changes in carbon dioxide emissions "
             "over time is crucial for developing strategies to reduce their levels and mitigate the adverse "
             "effects on the environment.")


def show_dataset():
    st.title("Dataset")
    st.write("For this project we have used the Monitoring of CO2 emissions from passenger cars "
             "Regulation (EU) 2019/631 dataset.\n\n"

             "Link to the dataset: "
             "https://www.eea.europa.eu/en/datahub/datahubitem-view/fa8b1229-3db6-495d-b18e-9c9b3267c02b\n\n"

             "The Regulation (EU) No 2019/631 requires Countries to record information for each new passenger car "
             "registered in its territory. Every year, each Member State shall submit to the Commission all the "
             "information related to their new registrations. In particular, the following details are required for "
             "each new passenger car registered: manufacturer name, type approval number, type, variant, version, "
             "make and commercial name, specific emissions of CO2 (NEDC and WLTP protocols), masses of the vehicle, "
             "wheel base, track width, engine capacity and power, fuel type and mode, eco-innovations and electricity "
             "consumption.")
    st.image(
        "img/car_exhaust.jpg",
        width=800
    )


def show_preprocessing():
    st.title("Preprocessing")
    st.write("Preprocessing is necessary for cleaning and preparing raw data for analysis and modeling, "
             "thereby ensuring its quality and suitability. "
             "This stage involves correcting errors, handling missing values, "
             "and transforming data into formats suitable for use in machine learning algorithms.")

    st.image("img/data.jpg", width=800)

    st.write("The dataset consists of a large amount of data. This data can be easily manipulated in Python "
             "using various libraries, such as pandas and sklearn. "
             "Here are some steps that have been applied to this dataset:\n\n"

             "1. **Removed unnecessary columns**: The columns 'Mh' and 'VFN' have been deleted from the dataset "
             "as they were not needed for further analysis.\n\n"

             "2. **Identified and counted duplicates**: Duplicate rows in the data were detected for "
             "uniqueness verification.\n\n"

             "3. **Filled missing values**: For numerical data, the KNNImputer algorithm has been applied to fill "
             "in missing values based on neighboring records.\n\n"

             "4. **Encoded categorical variables**: Categorical variables have been encoded to ensure "
             "their readiness for analysis.\n\n"

             "5. **Merged data**: All processed data both numerical and categorical have been combined "
             "into a single dataset for further analysis.\n\n"

             "6. **Displayed results**: Finally, the processed data and information about missing "
             "values have been presented.\n\n"

             "### !!! We can include df.head() here. !!!")


def show_models():
    st.title("Models & Predictions")

    st.image("img/brain.jpg", width=800)

    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "Regression Models",
            "Classification Models",
            "NN Regression Models",
            "NN Classification Models",
            "SHAP Explanations"
        ]
    )

    with tab1:
        regression.show_regression_models()

    with tab2:
        classification.show_classification_models()

    with tab3:
        nn_regression.show_nn_regression_models()

    with tab4:
        nn_classification.show_nn_classification_models()

    with tab5:
        shap.show_shap()


def show_conclusions():
    st.title("Conclusions")
    st.write("In this section, we will summarize the main findings of the project.")


# Main application function
def main():
    # Set page configuration
    st.set_page_config(page_title="CO2 Emissions Project", page_icon="🌍", layout="wide")

    # Sidebar menu for page selection
    page = st.sidebar.radio(
        "Main menu", ["Introduction", "Dataset", "Preprocessing", "Models & Predictions", "Conclusions"]
    )

    # Call the corresponding function based on the selected page
    if page == "Introduction":
        show_introduction()
    elif page == "Dataset":
        show_dataset()
    elif page == "Preprocessing":
        show_preprocessing()
    elif page == "Models & Predictions":
        show_models()
    elif page == "Conclusions":
        show_conclusions()


if __name__ == "__main__":
    main()
