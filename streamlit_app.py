import streamlit as st

# Custom CSS
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #ff5722; /* Adjust this to match your orange sidebar */
        color: white;
    }
    .main {
        background-color: #f8f8f8;
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
        background-color: #e64a19;
    }
    .sidebar .sidebar-radio input[type="radio"]:checked + label {
        background-color: #d84315;
    }
    .sidebar .sidebar-radio label img {
        width: 24px;
        height: 24px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar title
st.sidebar.title("Learn about our company")

# Sidebar menu with custom icons
menu_items = {
    "Thông tin thị trường": "📈",
    "Cổ phiếu chọn lọc": "⭐",
    "Đầu tư Danh mục": "📊",
    "Flash Deal": "⚡",
    "Hướng dẫn sử dụng": "📘",
    "Liên hệ": "📞"
}

selected_item = st.sidebar.radio(
    "Navigate",
    list(menu_items.keys()),
    format_func=lambda x: f"{menu_items[x]} {x}"
)

# Main content based on sidebar selection
st.title(selected_item)
if selected_item == "Thông tin thị trường":
    st.header("Thông tin thị trường")
    st.write("Nội dung cho phần Thông tin thị trường...")
elif selected_item == "Cổ phiếu chọn lọc":
    st.header("Cổ phiếu chọn lọc")
    st.write("Nội dung cho phần Cổ phiếu chọn lọc...")
elif selected_item == "Đầu tư Danh mục":
    st.header("Đầu tư Danh mục")
    st.write("Nội dung cho phần Đầu tư Danh mục...")
elif selected_item == "Flash Deal":
    st.header("Flash Deal")
    st.write("Nội dung cho phần Flash Deal...")
elif selected_item == "Hướng dẫn sử dụng":
    st.header("Hướng dẫn sử dụng")
    st.write("Nội dung cho phần Hướng dẫn sử dụng...")
elif selected_item == "Liên hệ":
    st.header("Liên hệ")
    st.write("Nội dung cho phần Liên hệ...")

# Additional main page content
st.write("Chào mừng bạn đến với trang web của chúng tôi! Tại đây, bạn có thể tìm
