import streamlit as st
import pandas as pd
import base64


# Function to set a background image with custom text styles
def set_bg_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string});
            background-size: cover; /* Ensures the image covers the viewport */
            background-position: center; /* Centers the image */
            background-repeat: no-repeat; /* Prevents repeating */
            background-attachment: scroll; /* Image scrolls with the page */
            height: 100vh; /* Full height of the viewport */
            width: 100vw; /* Full width of the viewport */
        }}
        /* Custom header styling */
        .header {{
            color: white; /* Change header color to white */
            font-weight: bold; /* Make header text bold */
            text-shadow: 2px 2px 4px black; /* Add black text shadow for better readability */
            font-size: 24px; /* Increase font size */
        }}
        .title {{
            color: white; /* Change title color to white */
            font-weight: bold; /* Make title text bold */
            text-shadow: 2px 2px 4px black; /* Add black text shadow for better readability */
            font-size: 45px; /* Increase font size */
        }}
        /* Back arrow button styling */
        .back-arrow {{
            position: absolute;
            top: -284px;
            left: -78px;
            z-index: 1000;
            border-radius: 200%; /* Round shape */
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* Shadow effect */       
        }}
        .back-arrow img {{
            width: 50px; /* Width of the back arrow icon */
            height: 50px; /* Height of the back arrow icon */
        }}
        /* Custom CSS for selectbox */
        .stSelectbox label {{
            color: black; /* Change label color */
            font-size: 24px; /* Change label font size */
            font-weight: bold; /* Make label text bold */
        }}
        </style>
    """


# Function to encode an image to base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


# Set the page title and layout
st.set_page_config(page_title="Smart Farming Practices", layout="wide")
st.markdown('<h1 class="title">Smart Farming Practices</h1>', unsafe_allow_html=True)

# Load the updated CSV file
file_path = "smart farming practices.csv"
df = pd.read_csv(file_path)

# Define icons for each criteria
icons = {
    "Growth Rate": "arrow-up",
    "Leaf Color": "leaf",
    "Disease Resistance": "shield-alt",
    "Yield Prediction": "chart-line",
    "Soil Moisture": "water",
    "Nutrient Levels": "flask",
    "pH Level": "vial",
    "Temperature": "thermometer-half",
    "Pesticide Levels": "bug",
    "Application Accuracy": "bullseye",
    "Toxicity Levels": "skull-crossbones",
    "Residuals": "filter",
    "Field Variability": "map",
    "Resource Efficiency": "recycle",
    "Cost Reduction": "dollar-sign",
    "Yield Improvement": "seedling",
    "Weather Prediction": "cloud-sun",
    "Market Trends": "chart-bar",
    "Yield Forecasting": "chart-pie",
    "Risk Management": "exclamation-triangle",
    "Reservoir Levels": "water",
    "Irrigation Scheduling": "calendar-alt",
    "Flood Prediction": "water-rise",
    "Water Quality": "water"
}


# Function to display criteria in a ring form with icons and progress bars
def display_criteria_circle(title, criteria):
    st.markdown(f"""
        <h2 class="custom-header">{title}</h2>
    """, unsafe_allow_html=True)
    cols = st.columns(len(criteria))
    for i, (metric, value) in enumerate(criteria.items()):
        progress = int(value.strip('%'))
        icon = icons.get(metric, "circle")
        with cols[i]:
            st.markdown(f"""
                <div style="display: flex; flex-direction: column; align-items: center; height: 200px; width: 200px; position: relative;">
                    <div style="display: flex; justify-content: center; align-items: center; height: 150px; width: 150px; position: relative;">
                        <div style="position: absolute; height: 130px; width: 130px; border-radius: 50%; border: 10px solid skyblue; display: flex; justify-content: center; align-items: center; background-color: white; color: black; font-size: 16px; text-align: center; flex-direction: column;">
                            <div><i class="fas fa-{icon}"></i></div>
                            <div>{metric}</div>
                            <div style="font-size: 24px;"><b>{value}</b></div>
                        </div>
                        <div style="position: absolute; height: 150px; width: 150px; border-radius: 50%; border: 10px solid skyblue; border-color: rgba(0, 0, 255, 0.3);"></div>
                    </div>
                    <div style="margin-top: 10px; width: 100%;">
                        <div style="width: 100%; height: 8px; background-color: rgba(200, 200, 200, 1.5); border-radius: 4px; overflow: hidden;">
                            <div style="height: 100%; width: {progress}%; background-color: #3FA2F6;"></div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)


# Function to display circular percentage indicators with icons and ring form
def display_circular_percentage(title, percentage):
    st.markdown(f"""
        <h2 class="custom-header">{title}</h2>
    """, unsafe_allow_html=True)
    progress = int(percentage.strip('%'))
    icon = icons.get(title, "circle")
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 200px; width: 200px; position: relative;">
            <div style="position: absolute; height: 180px; width: 180px; border-radius: 50%; border: 10px solid skyblue; display: flex; justify-content: center; align-items: center; background-color: white; color: black; font-size: 16px; flex-direction: column;">
                <div><i class="fas fa-{icon}"></i></div>
                <div>{title}</div>
                <div style="font-size: 24px;"><b>{percentage}</b></div>
            </div>
            <div style="position: absolute; height: 200px; width: 200px; border-radius: 50%; border: 10px solid skyblue; border-color: rgba(0, 0, 255, 0.3);"></div>
        </div>
    """, unsafe_allow_html=True)


# Plant selection dropdown
st.markdown('<h6 class="header">Select a Field:</h6>', unsafe_allow_html=True)
plant_names = ["Field_A", "Field_B", "Field_C", "Field_D", "Field_E"]
selected_plant = st.selectbox("Field Type", plant_names)

# Filter data based on selected plant
plant_data = df[df['Field'] == selected_plant]

# Set background image
st.markdown(set_bg_image('b8.jpg'), unsafe_allow_html=True)

# Load font-awesome for icons
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
""", unsafe_allow_html=True)

# Add back arrow
encoded_back_arrow = encode_image_to_base64('AL5.png')
st.markdown(f"""
    <div class="back-arrow">
        <a href="https://kisangpt-6swjrp2hvbgx7l48gqoesh.streamlit.app/">
            <img src="data:image/png;base64,{encoded_back_arrow}" alt="Back Arrow"/>
        </a>
    </div>
""", unsafe_allow_html=True)

# Custom CSS for tab styles and text formatting
st.markdown("""
    <style>
    /* Increase font size and change color to bold white for tab labels */
    .stTabs [role="tab"] {
        font-size: 20px !important; /* Increase tab font size */
        font-weight: bold !important; /* Make the text bold */
        color: black !important; /* Change text color to black */
        padding: 15px 25px !important; /* Increase padding inside each tab */
        background-color: lightSkyBlue !important; /* Light sky blue background */
        border: none !important; /* Remove the border */
        border-radius: 10px !important; /* Rounded corners for tabs */
        margin-right: 5px !important; /* Space between tabs */
    }
    .stTabs [role="tab"]:hover {
        background-color: deepskyblue !important; /* Darker sky blue on hover */
    }
    .stTabs [role="tab"]:focus {
        outline: none !important; /* Remove focus outline */
    }
    .stTabs .stTab {
        padding: 20px !important; /* Increase padding inside each tab */
    }
    /* Custom header styling */
    .custom-header {
        color: white !important; /* Change header color to white */
        font-weight: bold !important; /* Make header text bold */
        text-shadow: 2px 2px 4px black !important; /* Add black text shadow for better readability */
        font-size: 36px !important; /* Increase font size of headers */
    }
    .css-12oz5g7 {
        background: rgba(255, 255, 255, 0.8);
        padding: 20px; /* Increase padding for content inside the tab */
        border-radius: 5px;
    }
    .css-1d391kg, .css-163ttbj, .css-1l02zno {
        background: rgba(255, 255, 255, 0.6);
        border-radius: 5px;
        color: black;
    }
    .css-1d391kg:nth-child(odd) {
        background: rgba(200, 200, 200, 0.8);
    }
    .css-1d391kg:nth-child(even) {
        background: rgba(150, 150, 150, 0.8);
    }
    .st-tabs {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 5px;
    }
    .css-18e3th9 {
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# Tabs for different monitoring systems
tabs = st.tabs(["Plant Health", "Soil Monitoring", "Pesticide Control", "Precision Farming", "Predictive Analytics",
                "Water Level Monitoring"])

# Display data for Plant Health Monitoring
with tabs[0]:
    criteria = plant_data[["Growth Rate", "Leaf Color", "Disease Resistance", "Yield Prediction"]].iloc[0].to_dict()
    display_criteria_circle("Plant Health Monitoring", criteria)
    display_circular_percentage("Overall Health", plant_data["Growth Rate"].iloc[0])

# Display data for Soil Monitoring
with tabs[1]:
    criteria = plant_data[["Soil Moisture", "Nutrient Levels", "pH Level", "Temperature"]].iloc[0].to_dict()
    display_criteria_circle("Soil Monitoring", criteria)
    display_circular_percentage("Soil Quality", plant_data["Soil Moisture"].iloc[0])

# Display data for Pesticide Control
with tabs[2]:
    criteria = plant_data[["Pesticide Levels", "Application Accuracy", "Toxicity Levels", "Residuals"]].iloc[
        0].to_dict()
    display_criteria_circle("Pesticide Control", criteria)
    display_circular_percentage("Pesticide Efficiency", plant_data["Pesticide Levels"].iloc[0])

# Display data for Precision Farming
with tabs[3]:
    criteria = plant_data[["Field Variability", "Resource Efficiency", "Cost Reduction", "Yield Improvement"]].iloc[
        0].to_dict()
    display_criteria_circle("Precision Farming", criteria)
    display_circular_percentage("Precision Efficiency", plant_data["Resource Efficiency"].iloc[0])

# Display data for Predictive Analytics
with tabs[4]:
    criteria = plant_data[["Weather Prediction", "Market Trends", "Yield Forecasting", "Risk Management"]].iloc[
        0].to_dict()
    display_criteria_circle("Predictive Analytics", criteria)
    display_circular_percentage("Analytics Accuracy", plant_data["Weather Prediction"].iloc[0])

# Display data for Water Level Monitoring
with tabs[5]:
    criteria = plant_data[["Reservoir Levels", "Irrigation Scheduling", "Flood Prediction", "Water Quality"]].iloc[
        0].to_dict()
    display_criteria_circle("Water Level Monitoring", criteria)
    display_circular_percentage("Water Management", plant_data["Reservoir Levels"].iloc[0])
