Soil Nutrient Analysis Project
Project Banner

A Streamlit-based web application that analyzes soil nutrient levels and provides recommendations based on machine learning predictions.

Table of Contents
Features

Installation

Usage

Dataset

Model

Project Structure

Contributing

License

Features
🌱 Interactive soil nutrient analysis tool

📊 Visualize soil parameter distributions

🤖 Machine learning-powered predictions (Random Forest Classifier)

📈 Real-time results and recommendations

📁 Data persistence using Pickle

🎛 Adjustable input parameters with sliders

Installation

python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
Install the required packages:

pip install -r requirements.txt
Usage
1. First, generate the dataset and train the model:
Run the Jupyter notebook to create the dataset and trained model:

jupyter notebook create_soil_dataset.ipynb
2. Then launch the Streamlit app:
streamlit run soil_nutrient_app.py
The application will open in your default browser at http://localhost:8501

Dataset
The synthetic soil nutrient dataset contains the following features:

Feature	Description	Range
Nitrogen	Nitrogen content in ppm	0-200 ppm
Phosphorus	Phosphorus content in ppm	0-100 ppm
Potassium	Potassium content in ppm	0-300 ppm
pH	Soil pH level	3.0-10.0
Organic_Matter	Organic matter percentage	0-10%
Moisture	Soil moisture content	0-100%
Nutrient_Status	Target variable (Low/Medium/High)	Categorical
Model
The project uses a Random Forest Classifier with the following specifications:

Algorithm: Random Forest

Estimators: 100 trees

Criterion: Gini impurity

Max Depth: None (nodes expanded until pure)

Random State: 42 for reproducibility

The model achieves approximately 95% accuracy on the synthetic dataset.

Project Structure
Copy
soil-nutrient-analysis/
├── soil_nutrient_app.py        # Streamlit application
├── create_soil_dataset.ipynb   # Jupyter notebook for dataset creation
├── soil_nutrient_data.csv      # Generated soil dataset
├── soil_nutrient_model.pkl     # Trained model (Pickle file)
├── requirements.txt            # Python dependencies
└── README.md                   # This file
