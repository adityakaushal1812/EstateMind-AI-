EstateMind AI
=============

EstateMind AI is a machine learning–based web application designed to
predict house prices using key property features and regression models.
The project provides a secure, login-protected, multi-page dashboard
built using Streamlit.

--------------------------------------------------
FEATURES
--------------------------------------------------
- AI-powered house price prediction
- Machine Learning regression model
- Login-protected access
- Multi-page Streamlit dashboard
- Clean and responsive user interface
- Feature-based price estimation

--------------------------------------------------
TECHNOLOGIES USED
--------------------------------------------------
- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib / Pickle

--------------------------------------------------
PROJECT STRUCTURE
--------------------------------------------------

EstateMind-AI/
|
|-- app.py
|-- requirements.txt
|-- Procfile
|-- runtime.txt
|
|-- model/
|   |-- house_price_model.pkl
|
|-- pages/
|   |-- 0_Login.py
|   |-- Prediction.py
|   |-- Analytics.py
|   |-- About.py
|
|-- README.txt

--------------------------------------------------
HOW TO RUN LOCALLY
--------------------------------------------------
1. Clone the repository:
   git clone https://github.com/adityakaushal1812/EstateMind-AI.git

2. Go to project folder:
   cd EstateMind-AI

3. Install dependencies:
   pip install -r requirements.txt

4. Run the app:
   streamlit run app.py

--------------------------------------------------
LOGIN CREDENTIALS (DEMO)
--------------------------------------------------
Username: admin
Password: admin123

Username: user
Password: user123

--------------------------------------------------
DEPLOYMENT
--------------------------------------------------
This project is deployed on Render as a Python Web Service.

Build Command:
pip install -r requirements.txt

Start Command:
streamlit run app.py --server.port $PORT --server.address 0.0.0.0

--------------------------------------------------
USE CASES
--------------------------------------------------
- NIELIT Academic Project
- Machine Learning demonstrations
- Real-estate price analysis
- Hackathons and portfolio projects

--------------------------------------------------
DEVELOPER
--------------------------------------------------
Developed by: Aditya Kaushal
NIELIT Academic Project – 2026

--------------------------------------------------
LICENSE
--------------------------------------------------
MIT License
