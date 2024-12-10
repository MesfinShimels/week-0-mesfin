import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit App
st.title("Solar Farm Data Analysis")
st.write("This app performs analysis on solar radiation data and provides insights.")

# File Upload
uploaded_file = st.file_uploader("Upload your dataset (CSV format):", type="csv")

if uploaded_file is not None:
    # Load the dataset
    data = pd.read_csv(uploaded_file)
    
    # Display the first few rows of the dataset
    st.subheader("Dataset Preview")
    st.write(data.head())
    
    # Dataset information
    st.subheader("Dataset Information")
    st.write(f"Number of rows: {data.shape[0]}")
    st.write(f"Number of columns: {data.shape[1]}")
    buffer = []
    data.info(buf=buffer)
    info_str = "\n".join(buffer)
    st.text(info_str)

    # Missing Values
    st.subheader("Missing Values")
    st.write(data.isnull().sum())
    
    # Basic Statistics
    st.subheader("Descriptive Statistics")
    st.write(data.describe())
    
    # Exploratory Data Analysis
    st.subheader("Exploratory Data Analysis")
    
    # Correlation Heatmap
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
    
    # Distribution of GHI
    if 'GHI' in data.columns:
        st.subheader("Global Horizontal Irradiance (GHI) Distribution")
        fig, ax = plt.subplots()
        sns.histplot(data['GHI'], kde=True, bins=30, ax=ax, color='blue')
        ax.set_title("Distribution of GHI")
        st.pyplot(fig)
    
    # Time-series Analysis of GHI
    if 'Timestamp' in data.columns:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'], errors='coerce')
        data.set_index('Timestamp', inplace=True, drop=False)
        
        st.subheader("Time Series Analysis of GHI")
        fig, ax = plt.subplots(figsize=(12, 6))
        data['GHI'].plot(ax=ax, color='orange')
        ax.set_title("Time Series of GHI")
        ax.set_ylabel("GHI (W/m²)")
        st.pyplot(fig)
    
    # Insights and Recommendations
    st.subheader("Insights and Recommendations")
    st.write("""
    - **Regions with High GHI**: Focus on areas with high GHI values for solar farm installations.
    - **Impact of Weather Variables**: Analyze the impact of relative humidity, wind speed, and temperature on solar efficiency.
    - **Cleaning Events**: Investigate the effect of cleaning events on module efficiency.
    """)
else:
    st.info("Please upload a dataset to begin anlayzed
    .")
