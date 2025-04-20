import streamlit as st
import pandas as pd
import os
from PIL import Image

st.markdown("<style>.stApp { color: #000000; }</style>", unsafe_allow_html=True)
background_color="#F98A60"
st.markdown(
            f"""
            <style>
            .stApp {{
                background-color: {background_color};
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
# Title of the App
st.title("Clusters of World Anthems")

# Define dataset and image folder paths using relative paths
mask_folder = "images"  # Adjusted for your project structure
dataset_path = "datasets/updateddataset.csv"

# Load the Dataset
try:
    data = pd.read_csv(dataset_path)
except FileNotFoundError:
    st.error("Dataset not found. Please check the path and file name.")
    st.stop()

# Define background colors for each cluster
background_colors = {
    'Echoes of Sacred Freedom': '#FFDDC1',  # Light peach
    'O Motherly Nature': '#D0F0C0',         # Light green
    'A Child’s Voice': '#D6EAF8',          # Light blue
    'Glorious Homeland': '#FADBD8',        # Light pink
}

# Dropdown menu for country selection
countries = data['Country'].unique()
selected_country = st.selectbox("Select a Country:", countries)

# Check Button
if st.button("Check"):
    # Extract the cluster name and anthem
    row = data[data['Country'] == selected_country]
    
    if not row.empty:
        cluster_name = row['cluster_names'].values[0]
        anthem = row['Anthem'].values[0]

        # Dynamically set background color based on the cluster
        background_color = background_colors.get(cluster_name, "#FFFFFF")  # Default to white if cluster not found
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-color: {background_color};
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        # Display WordCloud image
        st.subheader("WordCloud:")
        colormap_path = os.path.join(mask_folder, f"{cluster_name}wordcloud.png")
        if os.path.exists(colormap_path):
            colormap_image = Image.open(colormap_path)
            st.image(colormap_image, caption=f"Cluster Colormap: {cluster_name}", use_container_width=True)
        else:
            st.warning("Colormap not found for this cluster!")

        # Display the anthem
        st.subheader("Anthem:")
        st.write(anthem)
    else:
        st.error("Country data not found.")

    # Go Back Button
    if st.button("Go Back"):
        st.experimental_rerun()
