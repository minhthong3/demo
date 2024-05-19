import streamlit as st

# Set the page layout
st.set_page_config(layout="wide")

# Add the main content
st.markdown("""
    <style>
    .main-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .sidebar {
        background-color: #ff6600;
        padding: 20px;
        height: 100vh;
    }
    .sidebar h2 {
        color: white;
    }
    .sidebar a {
        display: block;
        color: white;
        text-decoration: none;
        margin: 20px 0;
    }
    .sidebar a:hover {
        text-decoration: underline;
    }
    .main-section {
        flex-grow: 1;
        padding: 40px;
    }
    .main-section img {
        width: 100%;
    }
    .logo {
        max-width: 200px;
    }
    </style>
    <div class="main-content">
        <div class="sidebar">
            <h2>Learn about our company</h2>
            <a href="#">Our Values</a>
            <a href="#">The Team</a>
            <a href="#">Our Services</a>
            <a href="#">Newsletter</a>
            <a href="#">Book a Consultation</a>
            <a href="#">Contact Us</a>
        </div>
        <div class="main-section">
            <img src="data:image/png;base64,{}" alt="Main Image">
            <div>
                <img class="logo" src="data:image/png;base64,{}" alt="Logo">
                <h1>Strategic Branding</h1>
            </div>
        </div>
    </div>
""".format(
    st.image("path_to_your_main_image.png", use_column_width=True),  # Replace with the path to your image
    st.image("path_to_your_logo_image.png", use_column_width=True)  # Replace with the path to your logo
), unsafe_allow_html=True)
