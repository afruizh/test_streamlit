# import streamlit as st

# st.title("My Streamlit App")
# st.write("Hello, world!")


# # read a secret
# secret = st.secrets["SERVING_ENDPOINT"]

# # show the secret
# st.write(f"SERVING_ENDPOINT: {secret}")

import streamlit as st


# Configure Streamlit page with favicon
st.set_page_config(
    page_title="Tropical Forages Chat",
    page_icon="public/grass.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
    }
)

# Apply custom CSS for background and light theme
st.markdown("""
<style>
    /* Set light theme colors */
    :root {
        --background-color: #ffffff;
        --text-color: #1a1a1a;
        --secondary-bg: #f8f9fa;
        --border-color: #e1e4e8;
    }
    
    /* Main app background with gradient */
    .stApp {
        background-color: #fff;
        background-image: 
            radial-gradient(at 21% 11%, hsl(126.83deg 57% 78% / 52%) 0, transparent 50%), 
            radial-gradient(at 85% 0, rgb(233 230 186 / 53%) 0, transparent 50%), 
            radial-gradient(at 91% 36%, rgb(212 255 194 / 68%) 0, transparent 50%), 
            radial-gradient(at 8% 40%, rgb(239 251 218 / 46%) 0, transparent 50%);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
    }
    
    /* Chat message styling */
    .stChatMessage {
        background-color: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(5px);
        border-radius: 10px;
        border: 1px solid rgba(225, 228, 232, 0.5);
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.9);
        border: 1px solid #e1e4e8;
        border-radius: 8px;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: rgba(255, 255, 255, 0.9);
        border: 1px solid #e1e4e8;
        border-radius: 8px;
        color: #1a1a1a;
    }
    
    .stButton > button:hover {
        background-color: rgba(248, 249, 250, 0.9);
        border-color: #d1d5da;
    }
    
    /* Metrics and info boxes */
    .metric-container {
        background-color: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(5px);
        border-radius: 10px;
        border: 1px solid rgba(225, 228, 232, 0.5);
        padding: 1rem;
    }
    
    /* Force light theme for code blocks */
    .stCodeBlock {
        background-color: rgba(248, 249, 250, 0.9) !important;
    }
    
    /* Custom header styling */
    .chat-header {
        background: linear-gradient(90deg, #28a745, #20c997);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Constrain main content to 80% width */
    .block-container {
        max-width: 60% !important;
        margin: 0 auto !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    
    /* Alternative selector for content width constraint */
    [data-testid="stAppViewContainer"] > .main > .block-container {
        max-width: 60% !important;
        margin: 0 auto !important;
    }
    
    /* Make chat input full width like header */
    [data-testid="stChatInput"] {
        max-width: 60% !important;
        width: 60% !important;
        left: 20% !important;
        transform: none !important;
    }
    
    /* Chat input container full width */
    .stChatInput > div {
        max-width: 100% !important;
        width: 100% !important;
    }
    
    /* Alternative chat input selectors */
    [data-testid="stBottom"] > div {
        max-width: 100% !important;
        width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Init state ---
if "history" not in st.session_state:
    st.session_state.history = []

# Simple header with title, paragraph and logos - HTML only
import base64

# Load images and convert to base64
with open("public/headerv2.jpg", "rb") as f:
    header_img = base64.b64encode(f.read()).decode()
with open("public/logo.png", "rb") as f:
    logo_img = base64.b64encode(f.read()).decode()

st.markdown(f"""
<div style="display: flex; justify-content: space-between; align-items: center; padding: 20px 0; margin-bottom: 2rem;">
    <div style="flex: 0.7;">
        <h1 style="color: #28a745; font-size: 1.0rem; font-weight: bold; margin: 0;">
            TROPICAL FORAGES CHAT
        </h1>
        <p style="color: #6c757d; font-size: 0.85rem; margin: 0 0 0 0; line-height: 1.3;">
            This information is generated using a large language model (LLM) and may contain errors or biases. While we strive for accuracy, it's important to verify information and consult professionals for specific advice. You are responsible for how you use this content. <b>Please do not enter any personal or sensitive information.</b>
        </p>
    </div>
    <div style="display: flex; gap: 15px; align-items: center; flex-shrink: 0;">
        <a href="https://tropicalforages.info/text/intro/index.html" target="_blank" style="text-decoration: none;">
            <img src="data:image/jpeg;base64,{header_img}" style="height: 80px; border-radius: 8px; cursor: pointer; transition: opacity 0.3s ease;" onmouseover="this.style.opacity='0.8'" onmouseout="this.style.opacity='1'">
        </a>
        <img src="data:image/png;base64,{logo_img}" style="height: 200px;">
    </div>
</div>
""", unsafe_allow_html=True)