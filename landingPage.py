import streamlit as st
from PIL import Image

# Load image
image = Image.open('images/27324.jpg')

# Load custom CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css('style.css')

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
