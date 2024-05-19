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

# Các mục trong sidebar với các biểu tượng
pages = {
    "Nâng cấp tài khoản (BASIC)": ("upgrade", "🔧"),
    "Cài đặt thông báo": ("settings", "🔔"),
    "Danh mục theo dõi": ("watchlist", "📈"),
    "Tổng hợp": ("summary", "📊"),
    "Bộ lọc": ("filter", "🔍"),
    "Khuyến nghị": ("recommendations", "💡"),
    "Biểu đồ kỹ thuật": ("technical_charts", "📉"),
    "Sàn tin": ("news", "📰"),
    "Phân tích": ("analysis", "🧠"),
    "Blog": ("blog", "📝"),
    "Hướng dẫn chung": ("guide", "📚"),
}

# Tạo sidebar và điều hướng
st.sidebar.markdown(f"<img src='data:image/png;base64,{sidebar_image_base64}' style='width:100%; border-radius:10px;'>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='color: white;'>Minh Thông Nguyễn</h2>", unsafe_allow_html=True)

# Lựa chọn trang từ sidebar
selection = st.sidebar.radio("Chọn trang", list(pages.keys()), format_func=lambda x: f"{pages[x][1]} {x}")

# Thêm nội dung chính
st.markdown(f"""
    <style>
    body {{
        margin: 0;
        font-family: Arial, sans-serif;
    }}
    .sidebar .radio {{
        background-color: #2c3e50;
        color: white;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 10px;
    }}
    .sidebar .radio:hover {{
        background-color: #34495e;
    }}
    .sidebar .radio label {{
        display: flex;
        align-items: center;
        color: white;
    }}
    .sidebar .radio label span {{
        margin-left: 10px;
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
            <img src="data:image/png;base64,{sidebar_image_base64}" alt="User Image" style="width:100%; border-radius:10px;">
            <h2 style='color: white;'>Minh Thông Nguyễn</h2>
            <div class="radio">{selection}</div>
        </div>
        <div class="main">
            <h1>Welcome to Finbox</h1>
            <p>Here is the content of the main section. This content will scroll while the sidebar remains fixed.</p>
            <!-- Add more content here as needed -->
        </div>
    </div>
""", unsafe_allow_html=True)

# Nội dung của từng trang
if pages[selection][0] == "upgrade":
    st.title("Nâng cấp tài khoản (BASIC)")
    st.write("Nội dung trang Nâng cấp tài khoản (BASIC)")
elif pages[selection][0] == "settings":
    st.title("Cài đặt thông báo")
    st.write("Nội dung trang Cài đặt thông báo")
elif pages[selection][0] == "watchlist":
    st.title("Danh mục theo dõi")
    st.write("Nội dung trang Danh mục theo dõi")
elif pages[selection][0] == "summary":
    st.title("Tổng hợp")
    st.write("Nội dung trang Tổng hợp")
elif pages[selection][0] == "filter":
    st.title("Bộ lọc")
    st.write("Nội dung trang Bộ lọc")
elif pages[selection][0] == "recommendations":
    st.title("Khuyến nghị")
    st.write("Nội dung trang Khuyến nghị")
elif pages[selection][0] == "technical_charts":
    st.title("Biểu đồ kỹ thuật")
    st.write("Nội dung trang Biểu đồ kỹ thuật")
elif pages[selection][0] == "news":
    st.title("Sàn tin")
    st.write("Nội dung trang Sàn tin")
elif pages[selection][0] == "analysis":
    st.title("Phân tích")
    st.write("Nội dung trang Phân tích")
elif pages[selection][0] == "blog":
    st.title("Blog")
    st.write("Nội dung trang Blog")
elif pages[selection][0] == "guide":
    st.title("Hướng dẫn chung")
    st.write("Nội dung trang Hướng dẫn chung")
