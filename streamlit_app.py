import streamlit as st

# Custom CSS
st.markdown(
    """
    <style>
    .st-ae, .st-af, .st-ag, .st-ah, .st-ai, .st-aj, .st-ak {
        background-color: #4B0082; /* Màu nền sidebar */
        color: white;
        padding: 20px;
    }
    .st-al {
        font-size: 32px;
        font-weight: bold;
        color: white;
        margin-bottom: 20px;
    }
    .st-au, .st-av, .st-aw {
        border: none;
        border-top: 1px solid #FFA500; /* Màu cam cho đường gạch ngang */
        margin: 20px 0;
    }
    .st-am, .st-an, .st-ao, .st-ap, .st-aq, .st-ar, .st-as, .st-at {
        color: white;
        font-size: 24px;
        text-decoration: none;
        display: block;
        margin: 10px 0;
    }
    .st-am:hover, .st-an:hover, .st-ao:hover, .st-ap:hover, .st-aq:hover, .st-ar:hover, .st-as:hover, .st-at:hover {
        color: #FFA500; /* Màu cam khi hover */
    }
    .main-content {
        background-image: url('https://example.com/path/to/image.jpg'); /* Đường dẫn hình nền */
        background-size: cover;
        background-position: center;
        height: 100vh;
        padding: 50px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Thiết lập trạng thái ban đầu
if 'page' not in st.session_state:
    st.session_state['page'] = 'Cổ phiếu chọn lọc'

# Sidebar content
def set_page(page_name):
    st.session_state['page'] = page_name

st.sidebar.markdown("<div class='st-ae st-af st-ag st-ah st-ai st-aj st-ak'>", unsafe_allow_html=True)
st.sidebar.markdown("<h1 class='st-al'>VNWEALTH</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<a href='#' class='st-am st-an st-ao st-ap st-aq st-ar st-as st-at' onclick='window.setPage(\"Cổ phiếu chọn lọc\")'>Cổ phiếu chọn lọc</a>", unsafe_allow_html=True)
st.sidebar.markdown("<hr class='st-au st-av st-aw'>", unsafe_allow_html=True)
st.sidebar.markdown("<a href='#' class='st-am st-an st-ao st-ap st-aq st-ar st-as st-at' onclick='window.setPage(\"Đầu tư danh mục\")'>Đầu tư danh mục</a>", unsafe_allow_html=True)
st.sidebar.markdown("<hr class='st-au st-av st-aw'>", unsafe_allow_html=True)
st.sidebar.markdown("<a href='#' class='st-am st-an st-ao st-ap st-aq st-ar st-as st-at' onclick='window.setPage(\"Thông tin thị trường\")'>Thông tin thị trường</a>", unsafe_allow_html=True)
st.sidebar.markdown("<hr class='st-au st-av st-aw'>", unsafe_allow_html=True)
st.sidebar.markdown("<a href='#' class='st-am st-an st-ao st-ap st-aq st-ar st-as st-at' onclick='window.setPage(\"Flash deal\")'>Flash deal</a>", unsafe_allow_html=True)
st.sidebar.markdown("<hr class='st-au st-av st-aw'>", unsafe_allow_html=True)
st.sidebar.markdown("<a href='#' class='st-am st-an st-ao st-ap st-aq st-ar st-as st-at' onclick='window.setPage(\"Hướng dẫn\")'>Hướng dẫn</a>", unsafe_allow_html=True)
st.sidebar.markdown("<hr class='st-au st-av st-aw'>", unsafe_allow_html=True)
st.sidebar.markdown("<a href='#' class='st-am st-an st-ao st-ap st-aq st-ar st-as st-at' onclick='window.setPage(\"Liên hệ\")'>Liên hệ</a>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)

# Main content based on sidebar selection
if st.session_state['page'] == 'Cổ phiếu chọn lọc':
    st.title("Cổ phiếu chọn lọc")
elif st.session_state['page'] == 'Đầu tư danh mục':
    st.title("Đầu tư danh mục")
elif st.session_state['page'] == 'Thông tin thị trường':
    st.title("Thông tin thị trường")
elif st.session_state['page'] == 'Flash deal':
    st.title("Flash deal")
elif st.session_state['page'] == 'Hướng dẫn':
    st.title("Hướng dẫn")
elif st.session_state['page'] == 'Liên hệ':
    st.title("Liên hệ")
