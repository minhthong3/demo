import streamlit as st

# Đường dẫn đến hình ảnh
image_url = "images/27324.jpg"

# Đọc file CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    load_css("styles.css")

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
            <a href="#" onclick="showPage('Cổ phiếu chọn lọc')">Cổ phiếu chọn lọc</a>
            <hr>
            <a href="#" onclick="showPage('Đầu tư danh mục')">Đầu tư danh mục</a>
            <hr>
            <a href="#" onclick="showPage('Thông tin thị trường')">Thông tin thị trường</a>
            <hr>
            <a href="#" onclick="showPage('Flash deal')">Flash deal</a>
            <hr>
            <a href="#" onclick="showPage('Hướng dẫn')">Hướng dẫn</a>
            <hr>
            <a href="#" onclick="showPage('Liên hệ')">Liên hệ</a>
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
            <a href="#" onclick="showPage('Cổ phiếu chọn lọc')">Cổ phiếu chọn lọc</a>
            <hr>
            <a href="#" onclick="showPage('Đầu tư danh mục')">Đầu tư danh mục</a>
            <hr>
            <a href="#" onclick="showPage('Thông tin thị trường')">Thông tin thị trường</a>
            <hr>
            <a href="#" onclick="showPage('Flash deal')">Flash deal</a>
            <hr>
            <a href="#" onclick="showPage('Hướng dẫn')">Hướng dẫn</a>
            <hr>
            <a href="#" onclick="showPage('Liên hệ')">Liên hệ</a>
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
            <a href="#" onclick="showPage('Cổ phiếu chọn lọc')">Cổ phiếu chọn lọc</a>
            <hr>
            <a href="#" onclick="showPage('Đầu tư danh mục')">Đầu tư danh mục</a>
            <hr>
            <a href="#" onclick="showPage('Thông tin thị trường')">Thông tin thị trường</a>
            <hr>
            <a href="#" onclick="showPage('Flash deal')">Flash deal</a>
            <hr>
            <a href="#" onclick="showPage('Hướng dẫn')">Hướng dẫn</a>
            <hr>
            <a href="#" onclick="showPage('Liên hệ')">Liên hệ</a>
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
            <a href="#" onclick="showPage('Cổ phiếu chọn lọc')">Cổ phiếu chọn lọc</a>
            <hr>
            <a href="#" onclick="showPage('Đầu tư danh mục')">Đầu tư danh mục</a>
            <hr>
            <a href="#" onclick="showPage('Thông tin thị trường')">Thông tin thị trường</a>
            <hr>
            <a href="#" onclick="showPage('Flash deal')">Flash deal</a>
            <hr>
            <a href="#" onclick="showPage('Hướng dẫn')">Hướng dẫn</a>
            <hr>
            <a href="#" onclick="showPage('Liên hệ')">Liên hệ</a>
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
            <a href="#" onclick="showPage('Cổ phiếu chọn lọc')">Cổ phiếu chọn lọc</a>
            <hr>
            <a href="#" onclick="showPage('Đầu tư danh mục')">Đầu tư danh mục</a>
            <hr>
            <a href="#" onclick="showPage('Thông tin thị trường')">Thông tin thị trường</a>
            <hr>
            <a href="#" onclick="showPage('Flash deal')">Flash deal</a>
            <hr>
            <a href="#" onclick="showPage('Hướng dẫn')">Hướng dẫn</a>
            <hr>
            <a href="#" onclick="showPage('Liên hệ')">Liên hệ</a>
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
            <a href="#" onclick="showPage('Cổ phiếu chọn lọc')">Cổ phiếu chọn lọc</a>
            <hr>
            <a href="#" onclick="showPage('Đầu tư danh mục')">Đầu tư danh mục</a>
            <hr>
            <a href="#" onclick="showPage('Thông tin thị trường')">Thông tin thị trường</a>
            <hr>
            <a href="#" onclick="showPage('Flash deal')">Flash deal</a>
            <hr>
            <a href="#" onclick="showPage('Hướng dẫn')">Hướng dẫn</a>
            <hr>
            <a href="#" onclick="showPage('Liên hệ')">Liên hệ</a>
        </div>
        <div class="main-content" style="background-image: url('{image_url}');"></div>
    </div>
    ''', unsafe_allow_html=True)
    st.subheader("Liên hệ")
    st.write("Nội dung cho Liên hệ...")

if __name__ == "__main__":
    main()
