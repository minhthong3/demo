import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Hàm để chuyển đổi hình ảnh sang base64
def get_image_as_base64(image_path):
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Đường dẫn đến hình ảnh của bạn
sidebar_image_path = ""  # Thay thế bằng đường dẫn đến hình ảnh trên thanh điều hướng
background_image_path = "images/27324.jpg"  # Thay thế bằng đường dẫn đến hình ảnh nền

# Chuyển đổi hình ảnh sang base64
sidebar_image_base64 = get_image_as_base64(sidebar_image_path)
background_image_base64 = get_image_as_base64(background_image_path)

# Cấu hình bố cục trang
st.set_page_config(layout="wide")

# Thêm nội dung chính
st.markdown(f"""
    <style>
    body {{
        margin: 0;
        font-family: Arial, sans-serif;
    }}
    .container {{
        display: flex;
    }}
    .sidebar {{
        background-color: #2c3e50;
        color: white;
        padding: 15px;
        width: 250px;
        height: 100vh;
        position: fixed;
        overflow: auto;
    }}
    .sidebar img {{
        width: 100px;
        border-radius: 50%;
    }}
    .sidebar h2 {{
        color: white;
    }}
    .sidebar a {{
        color: white;
        text-decoration: none;
        display: block;
        padding: 10px 0;
    }}
    .sidebar a:hover {{
        background-color: #34495e;
    }}
    .main {{
        margin-left: 250px;
        padding: 15px;
        background-image: url("data:image/png;base64,{background_image_base64}");
        background-size: cover;
        height: 100vh;
        color: white;
    }}
    .main h1 {{
        color: white;
    }}
    </style>
    <div class="container">
        <div class="sidebar">
            <img src="data:image/png;base64,{sidebar_image_base64}" alt="User Image">
            <h2>Finbox</h2>
            <a href="#">Minh Thông Nguyễn</a>
            <a href="#">Nâng cấp tài khoản (BASIC)</a>
            <a href="#">Cài đặt thông báo</a>
            <a href="#">Danh mục theo dõi</a>
            <a href="#">Tổng hợp</a>
            <a href="#">Bộ lọc</a>
            <a href="#">Khuyến nghị</a>
            <a href="#">Biểu đồ kỹ thuật</a>
            <a href="#">Sàn tin</a>
            <a href="#">Phân tích</a>
            <a href="#">Blog</a>
            <a href="#">Hướng dẫn chung</a>
        </div>
        <div class="main">
            <h1>Welcome to Finbox</h1>
        </div>
    </div>
""", unsafe_allow_html=True)
