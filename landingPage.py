import streamlit as st
import os

# Đường dẫn đến hình ảnh
image_url = "images/27324.jpg"

# Đọc file CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    # Kiểm tra xem tệp CSS có tồn tại không
    css_file = "style.css"
    if os.path.exists(css_file):
        load_css(css_file)
    else:
        st.error("File CSS không tồn tại. Hãy đảm bảo rằng tệp style.css nằm cùng thư mục với app.py")

    st.sidebar.title("Pages")
    menu_options = ["Cổ phiếu chọn lọc", "Đầu tư danh mục", "Thông tin thị trường", "Flash deal", "Hướng dẫn", "Liên hệ"]
    menu_selection = st.sidebar.radio("", menu_options)

    if menu_selection == "Cổ phiếu chọn lọc":
        page_co_phieu_chon_loc()
    elif menu_selection == "Đầu tư danh mục":
        page_dau_tu_danh_muc()
    elif menu_selection == "Thông tin thị trường":
        page_thong_tin_thi_truong()
    elif menu_selection == "Flash deal":
        page_flash_deal()
    elif menu_selection == "Hướng dẫn":
        page_huong_dan()
    elif menu_selection == "Liên hệ":
        page_lien_he()

def page_co_phieu_chon_loc():
    st.markdown(f'''
    <div style="display: flex; height: 100vh;">
        <div class="sidebar">
            <h2>VNWEALTH</h2>
            <a href="#">Cổ phiếu chọn lọc</a>
            <hr>
            <a href="#">Đầu tư danh mục</a>
            <hr>
            <a href="#">Thông tin thị trường</a>
            <hr>
            <a href="#">Flash deal</a>
            <hr>
            <a href="#">Hướng dẫn</a>
            <hr>
            <a href="#">Liên hệ</a>
        </div>
        <div class="main-content" style="background-image: url('{image_url}');"></div>
    </div>
    ''', unsafe_allow_html=True)
    st.subheader("Cổ phiếu chọn lọc")
    st.write("Nội dung cho Cổ phiếu chọn lọc...")

def page_dau_tu_danh_muc():
    st.markdown(f'''
    <div style="display: flex; height: 100vh;">
        <div class="sidebar">
            <h2>VNWEALTH</h2>
            <a href="#">Cổ phiếu chọn lọc</a>
            <hr>
            <a href="#">Đầu tư danh mục</a>
            <hr>
            <a href="#">Thông tin thị trường</a>
            <hr>
            <a href="#">Flash deal</a>
            <hr>
            <a href="#">Hướng dẫn</a>
            <hr>
            <a href="#">Liên hệ</a>
        </div>
        <div class="main-content" style="background-image: url('{image_url}');"></div>
    </div>
    ''', unsafe_allow_html=True)
    st.subheader("Đầu tư danh mục")
    st.write("Nội dung cho Đầu tư danh mục...")

def page_thong_tin_thi_truong():
    st.markdown(f'''
    <div style="display: flex; height: 100vh;">
        <div class="sidebar">
            <h2>VNWEALTH</h2>
            <a href="#">Cổ phiếu chọn lọc</a>
            <hr>
            <a href="#">Đầu tư danh mục</a>
            <hr>
            <a href="#">Thông tin thị trường</a>
            <hr>
            <a href="#">Flash deal</a>
            <hr>
            <a href="#">Hướng dẫn</a>
            <hr>
            <a href="#">Liên hệ</a>
        </div>
        <div class="main-content" style="background-image: url('{image_url}');"></div>
    </div>
    ''', unsafe_allow_html=True)
    st.subheader("Thông tin thị trường")
    st.write("Nội dung cho Thông tin thị trường...")

def page_flash_deal():
    st.markdown(f'''
    <div style="display: flex; height: 100vh;">
        <div class="sidebar">
            <h2>VNWEALTH</h2>
            <a href="#">Cổ phiếu chọn lọc</a>
            <hr>
            <a href="#">Đầu tư danh mục</a>
            <hr>
            <a href="#">Thông tin thị trường</a>
            <hr>
            <a href="#">Flash deal</a>
            <hr>
            <a href="#">Hướng dẫn</a>
            <hr>
            <a href="#">Liên hệ</a>
        </div>
        <div class="main-content" style="background-image: url('{image_url}');"></div>
    </div>
    ''', unsafe_allow_html=True)
    st.subheader("Flash deal")
    st.write("Nội dung cho Flash deal...")

def page_huong_dan():
    st.markdown(f'''
    <div style="display: flex; height: 100vh;">
        <div class="sidebar">
            <h2>VNWEALTH</h2>
            <a href="#">Cổ phiếu chọn lọc</a>
            <hr>
            <a href="#">Đầu tư danh mục</a>
            <hr>
            <a href="#">Thông tin thị trường</a>
            <hr>
            <a href="#">Flash deal</a>
            <hr>
            <a href="#">Hướng dẫn</a>
            <hr>
            <a href="#">Liên hệ</a>
        </div>
        <div class="main-content" style="background-image: url('{image_url}');"></div>
    </div>
    ''', unsafe_allow_html=True)
    st.subheader("Hướng dẫn")
    st.write("Nội dung cho Hướng dẫn...")

def page_lien_he():
    st.markdown(f'''
    <div style="display: flex; height: 100vh;">
        <div class="sidebar">
            <h2>VNWEALTH</h2>
            <a href="#">Cổ phiếu chọn lọc</a>
            <hr>
            <a href="#">Đầu tư danh mục</a>
            <hr>
            <a href="#">Thông tin thị trường</a>
            <hr>
            <a href="#">Flash deal</a>
            <hr>
            <a href="#">Hướng dẫn</a>
            <hr>
            <a href="#">Liên hệ</a>
        </div>
        <div class="main-content" style="background-image: url('{image_url}');"></div>
    </div>
    ''', unsafe_allow_html=True)
    st.subheader("Liên hệ")
    st.write("Nội dung cho Liên hệ...")

if __name__ == "__main__":
    main()
