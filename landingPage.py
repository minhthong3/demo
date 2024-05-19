import streamlit as st
from PIL import Image

# Đọc hình ảnh
image = Image.open("images/27324.jpg")

# Tạo tiêu đề cho trang web
st.title("VNWEALTH")

# Chia layout thành hai phần
st.sidebar.title("Menu")
menu_options = ["Cổ phiếu chọn lọc", "Đầu tư danh mục", "Thông tin thị trường", "Flash deal", "Hướng dẫn", "Liên hệ"]
menu_selection = st.sidebar.selectbox("Chọn một mục:", menu_options)

st.image(image, use_column_width=True)

# Xử lý điều hướng dựa trên lựa chọn menu
if menu_selection == "Cổ phiếu chọn lọc":
    st.subheader("Cổ phiếu chọn lọc")
    st.write("Nội dung cho Cổ phiếu chọn lọc...")
elif menu_selection == "Đầu tư danh mục":
    st.subheader("Đầu tư danh mục")
    st.write("Nội dung cho Đầu tư danh mục...")
elif menu_selection == "Thông tin thị trường":
    st.subheader("Thông tin thị trường")
    st.write("Nội dung cho Thông tin thị trường...")
elif menu_selection == "Flash deal":
    st.subheader("Flash deal")
    st.write("Nội dung cho Flash deal...")
elif menu_selection == "Hướng dẫn":
    st.subheader("Hướng dẫn")
    st.write("Nội dung cho Hướng dẫn...")
elif menu_selection == "Liên hệ":
    st.subheader("Liên hệ")
    st.write("Nội dung cho Liên hệ...")

