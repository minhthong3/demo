import streamlit as st

# Custom CSS
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #2c3e50;
        color: white;
    }
    .main {
        background-color: #34495e;
        color: white;
        padding: 0;  /* Xóa padding */
        margin: 0;
    }
    .sidebar .sidebar-content, .main {
        padding: 0;
        margin: 0;
    }
    .sidebar .sidebar-content {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
        text-align: left;
        padding-left: 20px;
    }
    .sidebar-content h1 {
        margin-top: 20px;
        color: #ffffff;
    }
    .sidebar-content p {
        color: #ffffff;
    }
    .sidebar .sidebar-radio input[type="radio"] {
        display: none;
    }
    .sidebar .sidebar-radio label {
        display: flex;
        align-items: center;
        color: white;
        font-size: 18px;
        cursor: pointer;
        padding: 10px 0;
        width: 100%;
    }
    .sidebar .sidebar-radio label span {
        margin-left: 10px;
    }
    .sidebar .sidebar-radio label:hover {
        background-color: #3a539b;
    }
    .sidebar .sidebar-radio input[type="radio"]:checked + label {
        background-color: #1e3799;
    }
    .sidebar .sidebar-radio label img {
        width: 16px;  /* Giảm kích thước logo */
        height: 16px;  /* Giảm kích thước logo */
        margin-right: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar title
st.sidebar.title("Learn about our company")

# Sidebar menu with custom icons
menu_items = {
    "Trang chủ": "https://img.icons8.com/ios-filled/50/ffffff/home.png",
    "Phân tích cơ bản": "https://img.icons8.com/ios-filled/50/ffffff/combo-chart.png",
    "Bộ lọc chi tiết": "https://img.icons8.com/ios-filled/50/ffffff/search.png",
    "Bản đồ cổ đông": "https://img.icons8.com/ios-filled/50/ffffff/map.png"
}

# Custom sidebar with icons
for item, icon in menu_items.items():
    st.sidebar.markdown(
        f"""
        <div class="sidebar-radio">
            <input type="radio" id="{item}" name="menu" value="{item}">
            <label for="{item}">
                <img src="{icon}" alt="{item} icon">
                <span>{item}</span>
            </label>
        </div>
        """, unsafe_allow_html=True)

# Detect which item is selected
selected_item = st.sidebar.radio(
    "Navigate",
    list(menu_items.keys()),
    format_func=lambda x: ""
)

# Main content based on sidebar selection
def trang_chu():
    st.header("Trang chủ")
    st.write("Nội dung của Trang chủ...")

def phan_tich_co_ban():
    st.header("Phân tích cơ bản")
    st.write("Nội dung của Phân tích cơ bản...")

def bo_loc_chi_tiet():
    st.header("Bộ lọc chi tiết")
    st.write("Nội dung của Bộ lọc chi tiết...")

def ban_do_co_dong():
    st.header("Bản đồ cổ đông")
    st.write("Nội dung của Bản đồ cổ đông...")

# Page navigation
page_functions = {
    "Trang chủ": trang_chu,
    "Phân tích cơ bản": phan_tich_co_ban,
    "Bộ lọc chi tiết": bo_loc_chi_tiet,
    "Bản đồ cổ đông": ban_do_co_dong
}

if selected_item:
    page_functions[selected_item]()

# Additional main page content
st.write("Chào mừng đến với trang web của chúng tôi! Ở đây bạn có thể tìm hiểu thêm về các giá trị, đội ngũ và các dịch vụ mà chúng tôi cung cấp. Hãy liên hệ với chúng tôi hoặc đặt một buổi tư vấn.")
