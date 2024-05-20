import streamlit as st
from PIL import Image

# Load the image
image = Image.open("images/27324.jpg")

# Custom CSS
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-image: url(https://via.placeholder.com/150);
        background-repeat: no-repeat;
        background-size: cover;
        color: white;
    }
    .main {
        background-color: #f8f8f8;
    }
    .sidebar .sidebar-content, .main {
        padding: 0;
        margin: 0;
    }
    .sidebar .sidebar-content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    .sidebar-content h1 {
        margin-top: 20px;
        color: #ffffff;
    }
    .sidebar-content p {
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar with custom image and menu
st.sidebar.image(image, use_column_width=True)
st.sidebar.title("Learn about our company")
st.sidebar.markdown("<div style='color: white;'>Our Values</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='color: white;'>The Team</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='color: white;'>Our Services</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='color: white;'>Newsletter</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='color: white;'>Book a Consultation</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div style='color: white;'>Contact Us</div>", unsafe_allow_html=True)

# Main content
st.image(image, caption='Strategic Branding', use_column_width=True)
st.write("Welcome to our website! Here you can learn more about our values, the team, and the services we offer. Feel free to contact us or book a consultation.")

