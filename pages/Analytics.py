import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

model = pickle.load(open("model.pkl", "rb"))
# =======================
# AUTH GUARD

if not st.session_state.get("logged_in"):
    st.switch_page("pages/0_Login.py")

st.set_page_config(
    page_title="Analytics | EstateMind AI",
    page_icon="📊",
    layout="wide"
)

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
        st.switch_page("pages/prediction.py")
    if st.button("📊 Analytics"):
        st.switch_page("pages/Analytics.py")
    if st.button("ℹ️ About Project"):
        st.switch_page("pages/About.py")

    st.divider()
    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.switch_page("pages/0_Login.py")

# Session init
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False



features = [
    "bedrooms","bathrooms","sqft_living","sqft_lot","floors",
    "waterfront","view","condition","sqft_above","sqft_basement",
    "yr_built","yr_renovated"
]

st.title("📊 Model Analytics")

st.markdown("### Feature Importance")

df = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
}).sort_values(by="Importance")

fig, ax = plt.subplots(figsize=(7,8))
ax.barh(df["Feature"], df["Importance"])
ax.set_xlabel("Importance Score")

st.pyplot(fig)
