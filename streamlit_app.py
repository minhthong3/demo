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
        width: 24px;
        height: 24px;
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

selected_item = None
for item, icon in menu_items.items():
    if st.sidebar.radio("", [item], key=item):
        selected_item = item

# Main content based on sidebar selection
if selected_item:
    st.title(selected_item)
    if selected_item == "Trang chủ":
        st.header("Trang chủ")
        st.write("Nội dung của Trang chủ...")
    elif selected_item == "Phân tích cơ bản":
        st.header("Phân tích cơ bản")
        st.write("Nội dung của Phân tích cơ bản...")
    elif selected_item == "Bộ lọc chi tiết":
        st.header("Bộ lọc chi tiết")
        st.write("Nội dung của Bộ lọc chi tiết...")
    elif selected_item == "Bản đồ cổ đông":
        st.header("Bản đồ cổ đông")
        st.write("Nội dung của Bản đồ cổ đông...")

# Additional main page content
st.write("Chào mừng đến với trang web của chúng tôi! Ở đây bạn có thể tìm hiểu thêm về các giá trị, đội ngũ và các dịch vụ mà chúng tôi cung cấp. Hãy liên hệ với chúng tôi hoặc đặt một buổi tư vấn.")
