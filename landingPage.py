import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import os

# Hàm để chuyển đổi hình ảnh sang base64
def get_image_as_base64(image_path):
    try:
        img = Image.open(image_path)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return ""

# Đường dẫn đến hình ảnh của bạn
sidebar_image_path = "images/VN.png"  # Thay thế bằng đường dẫn đến hình ảnh trên thanh điều hướng
background_image_path = "images/27324.jpg"  # Thay thế bằng đường dẫn đến hình ảnh nền

# Kiểm tra xem các tệp có tồn tại không
if not os.path.exists(sidebar_image_path):
    st.error(f"Sidebar image not found at path: {sidebar_image_path}")
if not os.path.exists(background_image_path):
    st.error(f"Background image not found at path: {background_image_path}")

# Chuyển đổi hình ảnh sang base64
sidebar_image_base64 = get_image_as_base64(sidebar_image_path)
background_image_base64 = get_image_as_base64(background_image_path)

# Cấu hình bố cục trang
st.set_page_config(layout="wide")

# Tạo sidebar và điều hướng
st.sidebar.image(Image.open(BytesIO(base64.b64decode(sidebar_image_base64))), use_column_width=True)
st.sidebar.title("Minh Thông Nguyễn")

# Các mục trong sidebar
pages = {
    "Nâng cấp tài khoản (BASIC)": "upgrade",
    "Cài đặt thông báo": "settings",
    "Danh mục theo dõi": "watchlist",
    "Tổng hợp": "summary",
    "Bộ lọc": "filter",
    "Khuyến nghị": "recommendations",
    "Biểu đồ kỹ thuật": "technical_charts",
    "Sàn tin": "news",
    "Phân tích": "analysis",
    "Blog": "blog",
    "Hướng dẫn chung": "guide",
}

# Lựa chọn trang từ sidebar
selection = st.sidebar.radio("Chọn trang", list(pages.keys()))

# Thêm nội dung chính
st.markdown(f"""
    <style>
    body {{
        margin: 0;
        font-family: Arial, sans-serif;
    }}
    .container {{
        display: flex;
        height: 100vh;
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
        width: 100%;
        border-radius: 10px;
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
        overflow-y: auto;
        color: white;
    }}
    .main h1 {{
        color: white;
    }}
    </style>
    <div class="container">
        <div class="sidebar">
            <img src="data:image/png;base64,{sidebar_image_base64}" alt="User Image">
            <h2>Minh Thông Nguyễn</h2>
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
            <p>Here is the content of the main section. This content will scroll while the sidebar remains fixed.</p>
            <!-- Add more content here as needed -->
        </div>
    </div>
""", unsafe_allow_html=True)

# Nội dung của từng trang
if pages[selection] == "upgrade":
    st.title("Nâng cấp tài khoản (BASIC)")
    st.write("Nội dung trang Nâng cấp tài khoản (BASIC)")
elif pages[selection] == "settings":
    st.title("Cài đặt thông báo")
    st.write("Nội dung trang Cài đặt thông báo")
elif pages[selection] == "watchlist":
    st.title("Danh mục theo dõi")
    st.write("Nội dung trang Danh mục theo dõi")
elif pages[selection] == "summary":
    st.title("Tổng hợp")
    st.write("Nội dung trang Tổng hợp")
elif pages[selection] == "filter":
    st.title("Bộ lọc")
    st.write("Nội dung trang Bộ lọc")
elif pages[selection] == "recommendations":
    st.title("Khuyến nghị")
    st.write("Nội dung trang Khuyến nghị")
elif pages[selection] == "technical_charts":
    st.title("Biểu đồ kỹ thuật")
    st.write("Nội dung trang Biểu đồ kỹ thuật")
elif pages[selection] == "news":
    st.title("Sàn tin")
    st.write("Nội dung trang Sàn tin")
elif pages[selection] == "analysis":
    st.title("Phân tích")
    st.write("Nội dung trang Phân tích")
elif pages[selection] == "blog":
    st.title("Blog")
    st.write("Nội dung trang Blog")
elif pages[selection] == "guide":
    st.title("Hướng dẫn chung")
    st.write("Nội dung trang Hướng dẫn chung")
