import streamlit as st

st.set_page_config(
    page_title="FlowSense AI",
    layout="wide"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

[data-testid="stSidebar"]{
display:none;
}

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

.main{
background-color:#050816;
color:white;
}

.block-container{
padding-top:1rem;
max-width:1200px;
}

.hero{
text-align:center;
padding-top:40px;
padding-bottom:40px;
}

.hero-title{
font-size:64px;
font-weight:700;
color:white;
}

.hero-subtitle{
font-size:22px;
color:#9ba3b4;
margin-top:10px;
}

.card{
background:rgba(255,255,255,0.04);
backdrop-filter: blur(16px);
border:1px solid rgba(255,255,255,0.08);
padding:35px;
border-radius:24px;
height:260px;
transition:0.3s;
}

.card:hover{
border:1px solid #4f7cff;
box-shadow:0px 0px 25px rgba(79,124,255,0.4);
}

.card-title{
font-size:28px;
font-weight:700;
color:white;
margin-bottom:20px;
}

.card-text{
font-size:16px;
line-height:2;
color:#b7c0d0;
}

.stButton>button{
background:#4f7cff;
color:white;
border-radius:12px;
height:50px;
border:none;
font-size:16px;
font-weight:600;
}

.stButton>button:hover{
background:#6b8dff;
color:white;
}

</style>
""",unsafe_allow_html=True)

# ---------------- HERO ----------------

st.markdown("""
<div class='hero'>

<div class='hero-title'>
FlowSense AI
</div>

<div class='hero-subtitle'>
Event-Driven Congestion Intelligence Platform
</div>

</div>
""",unsafe_allow_html=True)

st.markdown("---")

# ================= ROW 1 =================

col1,col2=st.columns(2)

with col1:

    st.markdown("""
<div class='card'>

<div class='card-title'>
Overview
</div>

<div class='card-text'>

Historical Traffic Analytics

• Event Trends

• Peak Hours

</div>

</div>
""",unsafe_allow_html=True)

    if st.button(
        "Open Overview",
        use_container_width=True
    ):
        st.switch_page("pages/1_Overview.py")



with col2:

    st.markdown("""
<div class='card'>

<div class='card-title'>
Real Time Response
</div>

<div class='card-text'>

Live Event Operations

• Event Inputs

• Impact Forecast

</div>

</div>
""",unsafe_allow_html=True)

    if st.button(
        "Open Real Time Response",
        use_container_width=True
    ):
        st.switch_page("pages/2_Real_Time_Response.py")



st.write("")
st.write("")

# ================= ROW 2 =================

col3,col4=st.columns(2)

with col3:

    st.markdown("""
<div class='card'>

<div class='card-title'>
Deployment Intelligence
</div>

<div class='card-text'>

Resource Optimization

• Officer Allocation

• Barricade Planning

</div>

</div>
""",unsafe_allow_html=True)

    if st.button(
        "Open Deployment Intelligence",
        use_container_width=True
    ):
        st.switch_page("pages/3_Deployment_Intelligence.py")



with col4:

    st.markdown("""
<div class='card'>

<div class='card-title'>
Past Event Learning
</div>

<div class='card-text'>

Institutional Memory

• Event Debriefs

• Officer Notes

</div>

</div>
""",unsafe_allow_html=True)

    if st.button(
        "Open Past Event Learning",
        use_container_width=True
    ):
        st.switch_page("pages/4_Event_Learning.py")



st.write("")
st.write("")
st.markdown("---")

st.markdown(
"""
<center>

<h4 style='color:white'>
Predict → Deploy → Learn → Improve
</h4>

<p style='color:#9ba3b4'>
Historical Intelligence + Real-Time Response + Institutional Memory
</p>

</center>
""",
unsafe_allow_html=True
)