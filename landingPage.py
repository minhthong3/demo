import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="VNWEALTH", layout="wide")

# CSS cho hình nền và sidebar
page_bg_img = '''
<style>
.stApp {
  background-image: url("https://www.example.com/path/to/your/background/image.jpg");  /* Thay thế đường dẫn bằng đường dẫn thực tế của bạn */
  background-size: cover;
}

.sidebar .sidebar-content {
  background-color: #4A148C;  /* Màu tím cho sidebar */
  padding: 10px;
}

.sidebar .sidebar-content a {
  color: white;
  text-decoration: none;
  font-size: 18px;
  display: block;
  margin: 20px 0;
}

.sidebar .sidebar-content a:hover {
  color: #FFB300;  /* Màu vàng khi hover */
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Tiêu đề trong sidebar
st.sidebar.markdown("<h1 style='color: white;'>VNWEALTH</h1>", unsafe_allow_html=True)

# Các liên kết trong sidebar
pages = {
    "Cổ phiếu chọn lọc": "co_phieu_chon_loc",
    "Đầu tư danh mục": "dau_tu_danh_muc",
    "Thông tin thị trường": "thong_tin_thi_truong",
    "Flash deal": "flash_deal",
    "Hướng dẫn": "huong_dan",
    "Liên hệ": "lien_he"
}

# Tạo các liên kết trong sidebar
for page_name, page_key in pages.items():
    st.sidebar.markdown(f"<a href='#{page_key}'>{page_name}</a>", unsafe_allow_html=True)

# Nội dung trang chính
st.markdown("<div id='co_phieu_chon_loc'></div>", unsafe_allow_html=True)
st.header("Cổ phiếu chọn lọc")
st.write("Nội dung cho Cổ phiếu chọn lọc...")

st.markdown("<div id='dau_tu_danh_muc'></div>", unsafe_allow_html=True)
st.header("Đầu tư danh mục")
st.write("Nội dung cho Đầu tư danh mục...")

st.markdown("<div id='thong_tin_thi_truong'></div>", unsafe_allow_html=True)
st.header("Thông tin thị trường")
st.write("Nội dung cho Thông tin thị trường...")

st.markdown("<div id='flash_deal'></div>", unsafe_allow_html=True)
st.header("Flash deal")
st.write("Nội dung cho Flash deal...")

st.markdown("<div id='huong_dan'></div>", unsafe_allow_html=True)
st.header("Hướng dẫn")
st.write("Nội dung cho Hướng dẫn...")

st.markdown("<div id='lien_he'></div>", unsafe_allow_html=True)
st.header("Liên hệ")
st.write("Nội dung cho Liên hệ...")

# Footer với biểu tượng mạng xã hội
st.markdown("""
    <div style='text-align: center;'>
        <a href='#'><img src='https://image.flaticon.com/icons/png/512/2111/2111463.png' width='30' height='30'></a>
        <a href='#'><img src='https://image.flaticon.com/icons/png/512/733/733547.png' width='30' height='30'></a>
        <a href='#'><img src='https://image.flaticon.com/icons/png/512/733/733579.png' width='30' height='30'></a>
    </div>
""", unsafe_allow_html=True)
