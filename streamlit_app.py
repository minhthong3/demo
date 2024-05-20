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
st.sidebar.title("VNWEALTH")

# Sidebar menu with custom icons
menu_items = {
    "Our Values": "🌟",
    "The Team": "👥",
    "Our Services": "💼",
    "Newsletter": "📰",
    "Book a Consultation": "📅",
    "Contact Us": "📞"
}

selected_item = st.sidebar.radio(
    "",
    list(menu_items.keys()),
    format_func=lambda x: f"{menu_items[x]} {x}"
)

# Main content based on sidebar selection
st.title(selected_item)
if selected_item == "Our Values":
    st.header("Our Values")
    st.write("Content for Our Values section...")
elif selected_item == "The Team":
    st.header("The Team")
    st.write("Content for The Team section...")
elif selected_item == "Our Services":
    st.header("Our Services")
    st.write("Content for Our Services section...")
elif selected_item == "Newsletter":
    st.header("Newsletter")
    st.write("Content for Newsletter section...")
elif selected_item == "Book a Consultation":
    st.header("Book a Consultation")
    st.write("Content for Book a Consultation section...")
elif selected_item == "Contact Us":
    st.header("Contact Us")
    st.write("Content for Contact Us section...")

# Additional main page content
st.write("Welcome to our website! Here you can learn more about our values, the team, and the services we offer. Feel free to contact us or book a consultation.")
