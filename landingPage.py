import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="VNWEALTH", layout="wide")

# CSS cho hình nền
page_bg_img = '''
<style>
.stApp {
  background-image: url("https://www.example.com/path/to/your/background/image.jpg");
  background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Tiêu đề chính và phụ
st.markdown("<h1 style='text-align: center; color: white;'>VNWEALTH</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>Đầu tư an nhàn - Lợi nhuận bền vững</h3>", unsafe_allow_html=True)

# Tạo menu điều hướng trong sidebar
page = st.sidebar.selectbox(
    "Chọn trang",
    ["Trang chủ", "Thông tin thị trường", "Đầu tư Danh mục", "Cổ phiếu chọn lọc", "Flash Deal"]
)

# Nội dung cho từng trang
def trang_chu():
    st.write("Đây là trang chủ")

def thong_tin_thi_truong():
    st.write("Đây là trang Thông tin thị trường")

def dau_tu_danh_muc():
    st.write("Đây là trang Đầu tư Danh mục")

def co_phieu_chon_loc():
    st.write("Đây là trang Cổ phiếu chọn lọc")

def flash_deal():
    st.write("Đây là trang Flash Deal")

# Hiển thị nội dung dựa trên lựa chọn
if page == "Trang chủ":
    trang_chu()
elif page == "Thông tin thị trường":
    thong_tin_thi_truong()
elif page == "Đầu tư Danh mục":
    dau_tu_danh_muc()
elif page == "Cổ phiếu chọn lọc":
    co_phieu_chon_loc()
elif page == "Flash Deal":
    flash_deal()

# Footer với biểu tượng mạng xã hội
st.markdown("""
    <div style='text-align: center;'>
        <a href='#'><img src='https://image.flaticon.com/icons/png/512/2111/2111463.png' width='30' height='30'></a>
        <a href='#'><img src='https://image.flaticon.com/icons/png/512/733/733547.png' width='30' height='30'></a>
        <a href='#'><img src='https://image.flaticon.com/icons/png/512/733/733579.png' width='30' height='30'></a>
    </div>
""", unsafe_allow_html=True)
