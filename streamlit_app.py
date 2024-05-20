import streamlit as st

# Custom CSS
st.markdown(
    """
    <style>
    .sideNavigation_sideNavigationContainer__G0dDv {
        height: 100%;
        display: grid;
        grid-template-columns: 260px auto;
    }
    .sideNavigation_sideNavigationMenuContainer__cDKfX {
        background-color: #2c3e50;
        display: flex;
        flex-direction: column;
        overflow: hidden;
        z-index: 10;
        padding: 10px;
        color: white;
    }
    .sideNavigation_itemList__LeEZ0 {
        overflow: overlay;
        color: white;
    }
    .sideNavigation_sideNavigationBodyContainer__lmizj {
        overflow: scroll;
        position: relative;
        color: white;
    }
    .sideNavigation_header__mUzX3 {
        margin-top: 1.5rem;
        color: white;
    }
    .sideNavigation_title__dL9t2 {
        font-weight: 400;
        line-height: 2.25rem;
        color: white;
    }
    .sideNavigation_subTitle__VSPgg {
        color: white;
        font-size: .875rem;
        font-weight: 400;
        line-height: 1rem;
    }
    .sidebar .sidebar-content, .main {
        padding: 0;
        margin: 0;
        color: white;
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
    .main {
        background: url('background_image_url.jpg') no-repeat center center fixed;
        background-size: cover;
        color: white;
        padding: 20px;
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
st.write("Chào mừng bạn đến với trang web của chúng tôi! Tại đây, bạn có thể tìm hiểu thêm về thị trường, các cổ phiếu chọn lọc, cách đầu tư danh mục, và các Flash Deal hiện tại. Hãy liên hệ với chúng tôi nếu bạn cần hỗ trợ hoặc hướng dẫn sử dụng.")
