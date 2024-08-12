import base64
import streamlit as st


# Function to encode an image to base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


# Encode the background image
background_image_path = 'bgnew.jpeg'
encoded_background_image = encode_image_to_base64(background_image_path)

# Path to your icon images
icon_image_path = 'cropped.png'
grass_icon_image_path = 'te.png'
new_icon_image_path = 'green2.png'

# Encode the icon images
encoded_icon = encode_image_to_base64(icon_image_path)
encoded_grass_icon = encode_image_to_base64(grass_icon_image_path)
encoded_new_icon = encode_image_to_base64(new_icon_image_path)


def add_corner_gif(gif_path):
    with open(gif_path, "rb") as gif_file:
        encoded_string = base64.b64encode(gif_file.read()).decode()
        return encoded_string


# Add the corner GIF
encoded_string = add_corner_gif('chat_icon2.gif')

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded_background_image}");
        background-size: cover;
    }}
    .header {{
        width: 168%;
        height: 11%;
        background-color: rgba(255, 255, 255, 0.9);
        position: absolute;
        top: -28px;
        left: -236px;
        z-index: 1000;
        border-radius: 4px;
    }}
    .header h1 {{
        margin: 0;
        font-size: 20px;
        color: black;
    }}
    .corner-icon {{
        position: absolute;
        top: -37px;
        left: -200px;
        z-index: 1000;
        display: flex;
        flex-direction: column;
        align-items: center;
    }}
    .corner-icon img {{
        width: 90px;
        height: 65px;
        cursor: pointer;
    }}
    .corner-icon p {{
        color: white;
        font-size: 12px;
        font-weight: bold;
        text-align: center;
        margin: 5px 0 0 0;
    }}
    .corner-gif-container {{
        position: fixed;
        bottom: 10px;
        right: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 1000;
    }}
    .title {{
        position: absolute;
        margin-top: -20px;
        margin-left: -150px;
        color: white;
        font-family: 'Georgia';
        text-shadow: 6px 6px 10px rgba(0, 0, 0, 0.5);
    }}
    .main-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        position: relative;
    }}
    .left-icon {{
        width: 150px;
        height: 150px;
        border-radius: 50%;
        background: #FFD700;
        box-shadow: 0 0 0 10px rgba(255, 165, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        transition: background 0.3s, transform 0.3s;
        position: absolute;
        text-align: center;
    }}
    .left-icon img {{
        width: 90px;
        height: 90px;
    }}
    .left-icon p {{
        position: absolute;
        bottom: -30px;
        width: 100%;
        text-align: center;
        font-size: 14px;
        color: white;
        font-weight: bold;
    }}
    .left-icon:hover {{
        transform: scale(1.1);
    }}
    .right-icons {{
        position: relative;
        width: 500px;
        height: 500px;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    .right-icons .menu-item {{
        width: 120px;
        height: 120px;
        border-radius: 50%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        transition: background 0.3s, transform 0.3s;
        position: absolute;
        background: linear-gradient(145deg, #f0f0f0, #dcdcdc);
        box-shadow: 0 0 0 10px rgba(255, 255, 255, 0.5);
        text-align: center;
    }}
    .right-icons .menu-item:hover {{
        background: linear-gradient(145deg, #e6e6e6, #cccccc);
        transform: scale(1.1);
    }}
    .right-icons .menu-item img {{
        width: 40px;
        height: 40px;
    }}
    .right-icons .menu-item p {{
        margin-top: 5px;
        font-size: 12px;
        color: black;
        font-weight: bold;
        width: 115px;
        text-align: center;
        overflow: hidden;
        text-overflow: ellipsis;
    }}
    .corner-gif {{
        width: 40px;
        height: 40px;
        margin-bottom: 43px;
        margin-right: 75px;
        border-radius: 45%;
        background: #FFD700;
        box-shadow: 0 0 0 10px rgba(255, 255, 255, 0.5);
    }}
    .new-icon {{
        position: absolute;
        top: 22px;
        left: -223px;
        z-index: 1000;
    }}
    .new-icon img {{
        width: 168px;
        height: 85px;
    }}
    .grass-icon {{
        position: absolute;
        top: 30px;
        left: -222px;
        z-index: 1000;
    }}
    .grass-icon img {{
        width: 168px;
        height: 55px;
    }}
    </style>
    <div class="corner-icon">
        <a href="http://localhost:8501" target="_blank">
            <img src="data:image/jpg;base64,{encoded_icon}" alt="Leaf Icon"/>
        </a>
    </div>
     <div class="grass-icon">
        <img src="data:image/png;base64,{encoded_grass_icon}" alt="Grass Icon">
    </div>
    <div class="new-icon">
        <img src="data:image/png;base64,{encoded_new_icon}" alt="New Icon">
    </div>
   
    <div class="main-container">
        <div class="corner-gif-container">
            <a href="http://localhost:8502" target="_blank">
                <img src="data:image/gif;base64,{encoded_string}" class="corner-gif" style="background-color: #2E8B57;">
            </a>
        </div>
        <div class="left-icon">
            <img src="https://img.icons8.com/?size=100&id=15937&format=png" alt="KisanGPT"/>
        </div>
        <div class="right-icons">
            <a href="https://weather.com" target="_blank" class="menu-item" style="background-color: #2E8B57; transform: rotate(0deg) translate(200px) rotate(0deg);">
                <img src="https://img.icons8.com/?size=100&id=9247&format=png" alt="Weather Prediction and Alerts"/>
                <p>Weather Prediction and Alerts</p>
            </a>
            <a href="https://kisangpt-poc-c7ueeqrctgxnpfmnon5d3m.streamlit.app" target="_blank" class="menu-item" style="background-color: #87CEEB; transform: rotate(45deg) translate(200px) rotate(-45deg);">
                <img src="https://img.icons8.com/ios-filled/50/000000/soil.png" alt="Crop and Soil Management"/>
                <p>Crop and Soil Management</p>
            </a>
            <a href="" target="_blank" class="menu-item" style="background-color: #8B4513; transform: rotate(90deg) translate(200px) rotate(-90deg);">
                <img src="https://img.icons8.com/?size=100&id=54383&format=png" alt="Smart Farming Practices"/>
                <p>Smart Farming Practices</p>
            </a>
            <a href="https://stackoverflow.com/questions/60866205/python-streamlit-run-issue" class="menu-item" style="background-color: #FFFACD; transform: rotate(135deg) translate(200px) rotate(-135deg);">
                <img src="https://img.icons8.com/?size=100&id=HmUJDT2vb7mU&format=png" alt="Pest and Disease Control"/>
                <p>Pest and Disease Control</p>
            </a>
            <a href="https://en.wikipedia.org/wiki/OpenWeatherMap" target="_blank" class="menu-item" style="background-color: #A52A2A; transform: rotate(180deg) translate(200px) rotate(-180deg);">
                <img src="https://img.icons8.com/?size=100&id=rS0iQ61DOzEQ&format=png" alt="Market and Financial Insights"/>
                <p>Market and Financial Insights</p>
            </a>
            <a href="https://cropyeildpredictor-9z8hsxpuk84q8pxofmkkko.streamlit.app/" target="_blank" class="menu-item" style="background-color: #DAA520; transform: rotate(225deg) translate(200px) rotate(-225deg);">
                <img src="https://img.icons8.com/?size=100&id=10117&format=png" alt="Resource Management"/>
                <p>Crop Yield Predictor</p>
            </a>
            <a href="https://discuss.streamlit.io/t/getting-an-error-streamlit-is-not-recognized-as-an-internal-or-external-command-operable-program-or-batch-file/361" alt="Sustainability and Environmental Impact" target="_blank" class="menu-item" style="background-color: #808000; transform: rotate(270deg) translate(200px) rotate(-270deg);">
                <img src="https://img.icons8.com/?size=100&id=25852&format=png" alt="Sustainability and Environmental Impact"/>
                <p>Supply Chain Management</p>
            </a>
            <a href="https://www.educationalresources.com" target="_blank" class="menu-item" style="background-color: #F5F5DC; transform: rotate(315deg) translate(200px) rotate(-315deg);">
                <img src="https://img.icons8.com/ios-filled/50/000000/education.png" alt="Educational Resources"/>
                <p>Educational Resources</p>
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
