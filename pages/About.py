import streamlit as st

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="About | EstateMind AI",
    page_icon="ℹ️",
    layout="wide"
)

# ======================
# SESSION STATE
# ======================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ======================
# LOGIN GUARD
# ======================
if not st.session_state.logged_in:
    st.switch_page("pages/0_Login.py")

# ======================
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
# ABOUT CONTENT
# ======================
st.markdown("""
<div class="about-card">

<h1>ℹ️ About EstateMind AI</h1>

<p>
<strong>EstateMind AI</strong> is an intelligent, machine learning–based web application
designed to predict residential property prices using key real-estate features.
The system combines data analysis with advanced regression techniques to provide
accurate and reliable price estimations.
</p>

<h3>🎯 Project Objectives</h3>
<ul>
    <li>Develop an AI-powered house price prediction system</li>
    <li>Analyze the effect of property features on pricing</li>
    <li>Create an interactive and user-friendly dashboard</li>
    <li>Demonstrate real-world application of Machine Learning</li>
</ul>

<h3>⚙️ How the System Works</h3>
<ol>
    <li>User enters property details such as size, rooms, and location-related features</li>
    <li>The data is processed by a trained Random Forest Regression model</li>
    <li>The model predicts the estimated market price of the house</li>
</ol>

<h3>🧠 Technologies Used</h3>
<ul>
    <li><strong>Python</strong> – Core programming language</li>
    <li><strong>Scikit-learn</strong> – Machine learning model training</li>
    <li><strong>Random Forest Regressor</strong> – Prediction algorithm</li>
    <li><strong>Streamlit</strong> – Web application framework</li>
    <li><strong>Pandas & NumPy</strong> – Data processing</li>
</ul>

<h3>✨ Key Features</h3>
<ul>
    <li>AI-based house price prediction</li>
    <li>Explainable and feature-driven estimation</li>
    <li>Secure login-protected access</li>
    <li>Clean and responsive multi-page UI</li>
</ul>

<h3>📌 Use Cases</h3>
<ul>
    <li>Academic and diploma projects</li>
    <li>Machine Learning demonstrations</li>
    <li>Real-estate price analysis practice</li>
    <li>Hackathons and technical evaluations</li>
</ul>

<hr>

<p style="text-align:center; color:gray;">
Developed by <strong>Aditya Kaushal</strong><br>
© 2026 • EstateMind AI
</p>

</div>
""", unsafe_allow_html=True)
