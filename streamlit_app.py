import streamlit as st
from PIL import Image

# Load the image
image = Image.open("images/27324.jpg")

# Custom CSS
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #ff5722; /* Adjust this to match your orange sidebar */
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

# Sidebar menu
menu = st.sidebar.radio(
    "Navigate",
    ("Our Values", "The Team", "Our Services", "Newsletter", "Book a Consultation", "Contact Us")
)

# Main content based on sidebar selection
if menu == "Our Values":
    st.header("Our Values")
    st.write("Content for Our Values section...")
elif menu == "The Team":
    st.header("The Team")
    st.write("Content for The Team section...")
elif menu == "Our Services":
    st.header("Our Services")
    st.write("Content for Our Services section...")
elif menu == "Newsletter":
    st.header("Newsletter")
    st.write("Content for Newsletter section...")
elif menu == "Book a Consultation":
    st.header("Book a Consultation")
    st.write("Content for Book a Consultation section...")
elif menu == "Contact Us":
    st.header("Contact Us")
    st.write("Content for Contact Us section...")

# Additional main page content
st.image(image, caption='Strategic Branding', use_column_width=True)
st.write("Welcome to our website! Here you can learn more about our values, the team, and the services we offer. Feel free to contact us or book a consultation.")
