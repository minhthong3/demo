import streamlit as st
from PIL import Image

# Load image
image = Image.open('images/27324.jpg')

# Custom CSS to style the page
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #4B0082;
        color: white;
        position: fixed;
        height: 100%;
    }
    .main .block-container {
        padding-top: 2rem;
        padding-left: 18rem;
    }
    .sidebar .sidebar-content a {
        color: white;
        text-decoration: none;
        font-size: 18px;
        line-height: 2.5;
    }
    .sidebar .sidebar-content a:hover {
        text-decoration: underline;
    }
    .sidebar .sidebar-content hr {
        border: 1px solid #FF8C00;
    }
    .main img {
        max-width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar content
st.sidebar.markdown("""
    <div>
        <h2>VNWEALTH</h2>
        <a href="#">Cổ phiếu chọn lọc</a>
        <hr>
        <a href="#">Đầu tư danh mục</a>
        <hr>
        <a href="#">Thông tin thị trường</a>
        <hr>
        <a href="#">Flash deal</a>
        <hr>
        <a href="#">Hướng dẫn</a>
        <hr>
        <a href="#">Liên hệ</a>
    </div>
    """, unsafe_allow_html=True)

# Main content
st.image(image, caption='Thị trường chứng khoán')
