import streamlit as st

# Đường dẫn đến hình ảnh
image_url = "images/27324.jpg"

def main():
    st.sidebar.title("Menu")
    menu_options = ["Cổ phiếu chọn lọc", "Đầu tư danh mục", "Thông tin thị trường", "Flash deal", "Hướng dẫn", "Liên hệ"]
    menu_selection = st.sidebar.radio("Chọn một mục:", menu_options)

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
    st.subheader("Cổ phiếu chọn lọc")
    st.write("Nội dung cho Cổ phiếu chọn lọc...")
    st.image(image_url, use_column_width=True)

def page_dau_tu_danh_muc():
    st.subheader("Đầu tư danh mục")
    st.write("Nội dung cho Đầu tư danh mục...")
    st.image(image_url, use_column_width=True)

def page_thong_tin_thi_truong():
    st.subheader("Thông tin thị trường")
    st.write("Nội dung cho Thông tin thị trường...")
    st.image(image_url, use_column_width=True)

def page_flash_deal():
    st.subheader("Flash deal")
    st.write("Nội dung cho Flash deal...")
    st.image(image_url, use_column_width=True)

def page_huong_dan():
    st.subheader("Hướng dẫn")
    st.write("Nội dung cho Hướng dẫn...")
    st.image(image_url, use_column_width=True)

def page_lien_he():
    st.subheader("Liên hệ")
    st.write("Nội dung cho Liên hệ...")
    st.image(image_url, use_column_width=True)

if __name__ == "__main__":
    main()
