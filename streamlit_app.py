import streamlit as st

# Sidebar title
st.sidebar.title("VNWEALTH")

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
    "",
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
