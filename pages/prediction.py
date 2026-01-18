import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

# PAGE CONFIG
st.set_page_config(
    page_title="Prediction | EstateMind AI",
    page_icon="🔮",
    layout="wide"
)

# =======================
# AUTH GUARD

if not st.session_state.get("logged_in"):
    st.switch_page("pages/0_Login.py")

# CSS 
# ======================
st.markdown("""
<style>

/* Hide default Streamlit multipage nav */
[data-testid="stSidebarNav"] {
    display: none !important;
}

/* Sidebar background */
section[data-testid="stSidebar"] {
    background-color: #f8fafc;
}
section[data-testid="stSidebar"] > div:first-child {
    padding-top: 0.5rem;
}

/* Sidebar buttons */
section[data-testid="stSidebar"] button {
    width: 100%;
    border-radius: 10px;
    margin-bottom: 8px;
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
.sidebar-btn {
    width: 100%;
    padding: 10px;
    border-radius: 10px;
    border: 1px solid #d1d5db;
    background-color: #ffffff;
    font-weight: 600;
    cursor: pointer;
    margin-bottom: 8px;
    text-align: center;
}
.sidebar-btn:hover {
    background-color: #f1f5f9;
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
        st.switch_page("pages\\prediction.py")
    if st.button("📊 Analytics"):
        st.switch_page("pages\\Analytics.py")
    if st.button("ℹ️ About Project"):
        st.switch_page("pages\\About.py")

    st.divider()
    
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.switch_page("pages/0_Login.py")


st.title("🏠 Predict House Price")

st.markdown("### Enter Property Details")

col1, col2, col3 = st.columns(3)

with col1:
    bedrooms = st.number_input("Bedrooms", 0, step=1)
    bathrooms = st.number_input("Bathrooms", 0.0, step=0.5)
    floors = st.number_input("Floors", 0.0, step=0.5)
    waterfront = st.selectbox("Waterfront", [0, 1])

with col2:
    sqft_living = st.number_input("Living Area (sqft)", 0, step=100)
    sqft_lot = st.number_input("Lot Area (sqft)", 0, step=500)
    view = st.slider("View (0–4)", 0, 4, 0)
    condition = st.slider("Condition (1–5)", 1, 5, 3)

with col3:
    sqft_above = st.number_input("Above Ground Area (sqft)", 0, step=100)
    sqft_basement = st.number_input("Basement Area (sqft)", 0, step=100)
    yr_built = st.number_input("Year Built", 1800, 2025, 2000)
    yr_renovated = st.number_input("Year Renovated (0 = Never)", 0, 2025, 0)

if st.button("🔮 Predict Price", use_container_width=True):
    data = np.array([[bedrooms, bathrooms, sqft_living, sqft_lot, floors,
                      waterfront, view, condition, sqft_above,
                      sqft_basement, yr_built, yr_renovated]])
    
    price = model.predict(data)
    st.success(f"💰 Estimated Price: **${price[0]:,.2f}**")
