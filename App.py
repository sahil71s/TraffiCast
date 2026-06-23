import streamlit as st
import base64

st.set_page_config(
    page_title="TraffiCast",
    layout="wide"
)

# ================= BACKGROUND IMAGE INJECTION =================

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    st.markdown(
    f"""
    <style>
    .stApp {{
        /* Adding a dark 85% opacity overlay on top of your image */
        background-image: 
            linear-gradient(rgba(2, 6, 23, 0.75), rgba(2, 6, 23, 0.75)), 
            url(data:image/jpeg;base64,{encoded_string});
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

# Call the function with your image file name
# IMPORTANT: Ensure 'bg.jpg' is saved in the exact same folder as this Python script
add_bg_from_local('bg.jpg')

# ================= CSS =================

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<style>

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* Hide Sidebar */
section[data-testid="stSidebar"] {
    display: none;
}

/* Hero Text */
.title {
    margin-top: 150px;
    text-align: center;
    font-size: 105px;
    font-weight: 800;
    color: white;
    line-height: 1.1;
}

.subtitle {
    text-align: center;
    font-size: 34px;
    color: #60a5fa;
    margin-top: 20px;
    font-weight: 500;
}
            
.description {
    text-align:center;
    font-size:24px;
    max-width:1000px;
    margin:auto;
    margin-top:25px;
    color:#cbd5e1;
    line-height:1.8;
}

/* ================= Buttons ================= */

/* Force the Streamlit button container to flex and center across the full screen */
div.stButton{
    width:100%;
}
                     
div.stButton > button {
    height: 82px;
    width: 340px;
    font-size: 28px;
    font-weight: 800;
    letter-spacing: 0.5px;
    border-radius: 50px;
    background: linear-gradient(90deg,#f3c8cb,#b66d6d);
    color: white;
    border: none;
    box-shadow: 0px 0px 35px rgba(255,180,180,.35);
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #60a5fa, #2563eb);
}

</style>
""", unsafe_allow_html=True)

# ================= NAVBAR =================

c1, c2, c3, c4 = st.columns([7,1.2,1.2,1.6])

with c1:
    st.markdown(
    "<h3 style='color:white;'>Flipkart Gridlock 2.0 Hackathon</h3>",
    unsafe_allow_html=True)

with c2:
    st.markdown("""
    <a href="/Overview" style="
    color:white;
    font-size:21px;
    text-decoration:none;
    font-weight:600;
    ">
    Overview
    </a>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <a href="/Command_Desk" style="
    color:white;
    font-size:21px;
    text-decoration:none;
    font-weight:600;
    ">
    Command Desk
    </a>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <a href="/Post_Action_Analytics" style="
    color:white;
    font-size:21px;
    text-decoration:none;
    font-weight:600;
    ">
    Post-Action Analytics
    </a>
    """, unsafe_allow_html=True)

# ================= HERO =================

st.markdown("""
<div class='title'>
TraffiCast
</div>

<div class='subtitle'>
Event-Driven Congestion Intelligence Platform
</div>

<div class='description'>
Transforming traffic operations from reactive response to predictive and continuously learning intelligence.
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1.4,1,1.6])

with c2:
    launch = st.button(
        "Launch Platform",
        use_container_width=True
    )

if launch:
    st.switch_page("pages/1_Overview.py")