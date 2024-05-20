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
        background-image: url('file-JFigYS9NjXwnisMrGk4QnqWK'); /* Đường dẫn hình nền */
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

# Sidebar content
st.sidebar.markdown("<div class='st-ae st-af st-ag st-ah st-ai st-aj st-ak'>", unsafe_allow_html=True)
st.sidebar.markdown("<h1 class='st-al'>VNWEALTH</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<a href='#' class='st-am st-an st-ao st-ap st-aq st-ar st-as st-at'>Cổ phiếu chọn lọc</a>", unsafe_allow_html=True)
st.sidebar.markdown("<hr class='st-au st-av st-aw'>", unsafe_allow_html=True)
st.sidebar.markdown("<a href='#' class='st-am st-an st-ao st-ap st-aq st-ar st-as st-at'>Đầu tư danh mục</a>", unsafe_allow_html=True)
st.sidebar.markdown("<hr class='st-au st-av st-aw'>", unsafe_allow_html=True)
st.sidebar.markdown("<a href='#' class='st-am st-an st-ao st-ap st-aq st-ar st-as st-at'>Thông tin thị trường</a>", unsafe_allow_html=True)
st.sidebar.markdown("<hr class='st-au st-av st-aw'>", unsafe_allow_html=True)
st.sidebar.markdown("<a href='#' class='st-am st-an st-ao st-ap st-aq st-ar st-as st-at'>Flash deal</a>", unsafe_allow_html=True)
st.sidebar.markdown("<hr class='st-au st-av st-aw'>", unsafe_allow_html=True)
st.sidebar.markdown("<a href='#' class='st-am st-an st-ao st-ap st-aq st-ar st-as st-at'>Hướng dẫn</a>", unsafe_allow_html=True)
st.sidebar.markdown("<hr class='st-au st-av st-aw'>", unsafe_allow_html=True)
st.sidebar.markdown("<a href='#' class='st-am st-an st-ao st-ap st-aq st-ar st-as st-at'>Liên hệ</a>", unsafe_allow_html=True)
st.sidebar.markdown("</div>", unsafe_allow_html=True)

# Main content
st.markdown(
    """
    <div class='main-content'>
        <!-- Nội dung chính của bạn ở đây -->
    </div>
    """,
    unsafe_allow_html=True
)

st.title("Chào mừng bạn đến với VNWEALTH")
st.write("Tại đây, bạn có thể tìm hiểu thêm về thị trường, các cổ phiếu chọn lọc, cách đầu tư danh mục, và các Flash Deal hiện tại. Hãy liên hệ với chúng tôi nếu bạn cần hỗ trợ hoặc hướng dẫn sử dụng.")
