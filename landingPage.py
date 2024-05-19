import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def get_image_as_base64(image_path):
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="BMP")
    return base64.b64encode(buffered.getvalue()).decode()

# Cấu hình bố cục trang
st.set_page_config(layout="wide")

# Đường dẫn đến hình ảnh của bạn
main_image_path = "images/AI-Bot.bmp"  # Thay thế bằng đường dẫn đến hình ảnh của bạn
logo_image_path = "images/confused person 2.bmp"  # Thay thế bằng đường dẫn đến logo của bạn

# Chuyển đổi hình ảnh sang base64
main_image_base64 = get_image_as_base64(main_image_path)
logo_image_base64 = get_image_as_base64(logo_image_path)

# Thêm nội dung chính
st.markdown(f"""
    <style>
    .main-content {{
        display: flex;
    }}
    .sidebar {{
        background-color: #ff6600;
        padding: 20px;
        height: 100vh;
        position: fixed;
        width: 250px;
        top: 0;
        left: 0;
        overflow: hidden;
    }}
    .sidebar h2 {{
        color: white;
    }}
    .sidebar a {{
        display: block;
        color: white;
        text-decoration: none;
        margin: 20px 0;
    }}
    .sidebar a:hover {{
        text-decoration: underline;
    }}
    .main-section {{
        margin-left: 270px;  /* Để tạo khoảng cách cho phần bên trái cố định */
        padding: 40px;
        flex-grow: 1;
    }}
    .main-section img {{
        width: 100%;
    }}
    .logo {{
        max-width: 200px;
    }}
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
            <img src="data:image/bmp;base64,{main_image_base64}" alt="Main Image">
            <div>
                <img class="logo" src="data:image/bmp;base64,{logo_image_base64}" alt="Logo">
                <h1>Strategic Branding</h1>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
