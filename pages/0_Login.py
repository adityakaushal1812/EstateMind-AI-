import streamlit as st

st.set_page_config(
    page_title="EstateMind AI",
    page_icon="🏠",
    layout="centered"
)

# if not st.session_state.logged_in:
#     st.switch_page("pages/0_Login.py")
# ----------------------
# Session init
# ----------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ----------------------
# CSS
# ======================
st.markdown("""
<style>

/* Hide default Streamlit multipage nav */
[data-testid="stSidebarNav"] {
    display: none !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #f8fafc;
}
section[data-testid="stSidebar"] button {
    width: 100%;
    border-radius: 12px;
    margin-bottom: 10px;
    font-weight: 600;
}

/* Sidebar header */
.sidebar-title {
    font-size: 26px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 4px;
}
.sidebar-subtitle {
    font-size: 13px;
    text-align: center;
    color: #475569;
    margin-bottom: 14px;
}

/* Content card */
.about-card {
    max-width: 900px;
    margin: 30px auto;
    padding: 40px;
    background: #f8fafc;
    border-radius: 18px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ======================
# SIDEBAR
# ======================
with st.sidebar:
    st.markdown('<div class="sidebar-title">🏠 EstateMind AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-subtitle">Predict • Analyze • Decide</div>', unsafe_allow_html=True)
    st.divider()

    if st.button("🏠 Home"):
        st.switch_page("app.py")

    if st.button("🔮 Prediction"):
        st.switch_page("pages/prediction.py")

    if st.button("📊 Analytics"):
        st.switch_page("pages/Analytics.py")
        
    if st.button("ℹ️ About Project"):
        st.switch_page("pages/About.py")

    st.divider()
# UI
# ----------------------
st.markdown("## 🔐 Login")
st.write("Please login to continue")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

# ----------------------
# Login logic
# ----------------------
if st.button("Login"):
    # demo credentials (change later)
    if username == "admin" and password == "admin123":
        st.session_state.logged_in = True
        st.session_state.user = "admin"
        st.success("Login successful")
        st.switch_page("app.py")

    elif username == "user" and password == "user123":
        st.session_state.logged_in = True
        st.session_state.user = "user"
        st.success("Login successful")
        st.switch_page("app.py")

    else:
        st.error("Invalid username or password")
