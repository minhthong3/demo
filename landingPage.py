import streamlit as st
from PIL import Image

# Load the image
image = Image.open("/mnt/data/image.png")

# Set up the sidebar
st.sidebar.image(image, use_column_width=True)

# Sidebar options
st.sidebar.title("Finbox")
st.sidebar.markdown("### Minh Thông Nguyễn")
st.sidebar.button("Nâng cấp tài khoản (BASIC)")
st.sidebar.button("Cài đặt thông báo")
st.sidebar.button("Danh mục theo dõi")

# Sidebar menu
st.sidebar.markdown("### Menu")
options = st.sidebar.radio(
    "Chọn mục:",
    ("Tổng hợp", "Bộ lọc", "Khuyến nghị", "Biểu đồ kỹ thuật", "Săn tin", "Phân tích", "Blog", "Hướng dẫn chung")
)

# Main content based on the selected menu option
st.title(f"Bạn đã chọn: {options}")

if options == "Tổng hợp":
    st.write("Hiển thị nội dung tổng hợp tại đây...")
elif options == "Bộ lọc":
    st.write("Hiển thị bộ lọc tại đây...")
elif options == "Khuyến nghị":
    st.write("Hiển thị khuyến nghị tại đây...")
elif options == "Biểu đồ kỹ thuật":
    st.write("Hiển thị biểu đồ kỹ thuật tại đây...")
elif options == "Săn tin":
    st.write("Hiển thị săn tin tại đây...")
elif options == "Phân tích":
    st.write("Hiển thị phân tích tại đây...")
elif options == "Blog":
    st.write("Hiển thị blog tại đây...")
elif options == "Hướng dẫn chung":
    st.write("Hiển thị hướng dẫn chung tại đây...")

# Additional main page content
st.image(image)
st.write("Đây là ứng dụng Streamlit với sidebar tương tự như hình ảnh đã cung cấp.")
