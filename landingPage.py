import streamlit as st

# Use local CSS for styling
def local_css(file_name):
    with open(file_name, "r") as f:  # Sửa lỗi cú pháp ở đây bằng cách thêm dấu phẩy
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the CSS
local_css("style.css")

# Sidebar
st.sidebar.title("VNWEALTH")
menu_items = ["Cổ phiếu chọn lọc", "Đầu tư danh mục", "Thông tin thị trường", "Flash deal", "Hướng dẫn", "Liên hệ"]
for item in menu_items:
    st.sidebar.write(item)

# Main Content
st.image("images/27324.jpg", use_column_width=True)  # Adjust path as needed
