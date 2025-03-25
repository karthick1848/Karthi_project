import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

# Load the model and encoder
try:
    with open('soil_nutrient_model.pkl', 'rb') as f:
        model_data = pickle.load(f)
    model = model_data['model']
    encoder = model_data['encoder']
except FileNotFoundError:
    st.error("Model file not found. Please train the model first.")
    model = None
    encoder = None

# Load sample data for reference
try:
    sample_data = pd.read_csv('soil_nutrient_data.csv')
except FileNotFoundError:
    sample_data = None

# App title
st.title("Soil Nutrient Analysis Tool")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Analysis", "Data Info", "Model Info"])

if page == "Analysis":
    st.header("Soil Nutrient Analysis")
    
    # Input form
    with st.form("soil_input_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            nitrogen = st.slider("Nitrogen (N) ppm", 0.0, 200.0, 50.0)
            phosphorus = st.slider("Phosphorus (P) ppm", 0.0, 100.0, 20.0)
            potassium = st.slider("Potassium (K) ppm", 0.0, 300.0, 100.0)
            
        with col2:
            ph_level = st.slider("pH Level", 3.0, 10.0, 6.5)
            organic_matter = st.slider("Organic Matter (%)", 0.0, 10.0, 2.5)
            moisture = st.slider("Moisture Content (%)", 0.0, 100.0, 30.0)
        
        submitted = st.form_submit_button("Analyze Soil")
    
    if submitted and model is not None:
        # Create input dataframe
        input_data = pd.DataFrame([[nitrogen, phosphorus, potassium, ph_level, organic_matter, moisture]],
                                columns=['Nitrogen', 'Phosphorus', 'Potassium', 'pH', 'Organic_Matter', 'Moisture'])
        
        # Make prediction
        prediction = model.predict(input_data)
        nutrient_status = encoder.inverse_transform(prediction)[0]
        
        # Display results
        st.subheader("Analysis Results")
        st.write(f"**Predicted Nutrient Status:** {nutrient_status}")
        
        # Show interpretation
        st.subheader("Interpretation")
        if nutrient_status == "Low":
            st.warning("Your soil has low nutrient levels. Consider adding organic compost or appropriate fertilizers.")
        elif nutrient_status == "Medium":
            st.info("Your soil has medium nutrient levels. Maintenance fertilization may be needed.")
        else:
            st.success("Your soil has high nutrient levels. No immediate fertilization needed.")
        
        # Show input values
        st.subheader("Input Values")
        st.write(input_data)

elif page == "Data Info":
    st.header("Soil Nutrient Data Information")
    if sample_data is not None:
        st.write("Sample data from the dataset:")
        st.dataframe(sample_data.head())
        
        st.subheader("Data Statistics")
        st.write(sample_data.describe())
        
        st.subheader("Nutrient Status Distribution")
        st.bar_chart(sample_data['Nutrient_Status'].value_counts())
    else:
        st.warning("Sample data file not found.")

elif page == "Model Info":
    st.header("Model Information")
    if model is not None:
        st.write("This application uses a Random Forest Classifier to predict soil nutrient status.")
        st.write("**Model Parameters:**")
        st.write(model.get_params())
    else:
        st.warning("Model not loaded.")
