import streamlit as st

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="EstateMind AI",
    page_icon="🏠",
    layout="wide"
)

# ======================
# SESSION STATE
# ======================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login first
if not st.session_state.logged_in:
    st.switch_page("pages/0_Login.py")

# ======================
#  CSS
# ======================
st.markdown("""
<style>
            
/* Hide default Streamlit multipage navigation */
[data-testid="stSidebarNav"] {
    display: none;
}
section[data-testid="stSidebar"] {
    background-color: #f8fafc;
}
section[data-testid="stSidebar"] > div:first-child {
    padding-top: 0.5rem;
}
section[data-testid="stSidebar"] button {
    width: 100%;
    border-radius: 10px;
    margin-bottom: 8px;
    font-weight: 600;
}
.sidebar-title {
    font-size: 26px;
    font-weight: 800;
    text-align: center;
    margin-top: 0px;
    margin-bottom: 4px;
}
.sidebar-subtitle {
    font-size: 13px;
    text-align: center;
    color: #475569;
    margin-bottom: 14px;
}
.sidebar-footer {
    position: sticky;
    bottom: 0;
    padding-top: 10px;
    background: #f8fafc;
}
            
.hero-wrapper {
    display: flex;
    justify-content: center;
    margin-top: 30px;
    width: 100%;
}
.hero-card {
    width: 100%;
    max-width: 900px;
    padding: 40px;
    border-radius: 18px;
    # text-align: center;
    color: #0f172a;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
}

/* ===== FEATURE CARDS ===== */
.card {
    # background: #f8fafc;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    height: 180px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
}
.sidebar-btn {
    width: 100%;
    padding: 10px;
    border-radius: 10px;
    border: 1px solid #d1d5db;
    background-color: #ffffff;
    font-weight: 600;
    font-size: 16px;
    cursor: pointer;
    margin-bottom: 12px;
    text-align: center;
    color: #0f172a;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.sidebar-btn:hover {
    background-color: #f8fafc;
}
            
html {
    scroll-behavior: smooth;
}

</style>
""", unsafe_allow_html=True)

# ======================
# SIDEBAR
# ======================
with st.sidebar:
    # Header
    st.markdown('<div class="sidebar-title">🏠 EstateMind AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-subtitle">Predict • Analyze • Decide</div>', unsafe_allow_html=True)
    st.divider()

    # Navigation (UI only for now)
    if st.button("🏠 Home"):
        st.switch_page("app.py")

    if st.button("🔮 Prediction"):
        st.switch_page("pages/Prediction.py")

    if st.button("📊 Analytics"):
        st.switch_page("pages/Analytics.py")
    if st.button("ℹ️ About Project"):
        st.switch_page("pages/About.py")
    
    st.divider()

    if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.switch_page("pages/0_Login.py")


# ======================
# MAIN PAGE
# ======================
# =======================
# HERO SECTION (FIXED CENTER)
# =======================
st.markdown("""
<div class="hero-wrapper">
    <div style="width:100%;max-width:900px; text-align:center;">     
    <div class="hero-card">
        <h2>🏠 “AI-powered Real Estate price prediction.”</h2>
        <p style="font-size:18px;opacity:0.9;">
“A machine learning based system for predicting house prices using Real Estate data.”
        </p>
            </div>
    </div>
</div>
""", unsafe_allow_html=True)
# ======================
# get started button
# ======================
st.write("")
left, center, right = st.columns([4,2,4])
with center:
    if st.button("🚀 Get Started", use_container_width=True):
        st.switch_page("pages/prediction.py")
st.divider()

# FEATURES
# =======================
st.markdown("## ✨ Key Features")

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="card">
        <h4>🤖 AI-Based Prediction</h4>
        <p>Random Forest Regression for accurate price estimation.</p>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="card">
        <h4>📊 Explainable ML</h4>
        <p>Feature importance to understand pricing factors.</p>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="card">
        <h4>🧭 Multi-Page Dashboard</h4>
        <p>Prediction, Analytics, and About pages.</p>
    </div>
    """, unsafe_allow_html=True)
# =======================
