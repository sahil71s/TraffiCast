import streamlit as st

st.set_page_config(
    page_title="FlowSense AI",
    layout="wide"
)

# ================= CSS =================

st.markdown("""
<style>

.stApp{
background:
radial-gradient(circle at 20% 20%, rgba(59,130,246,0.15), transparent 30%),
radial-gradient(circle at 80% 70%, rgba(37,99,235,0.12), transparent 25%),
linear-gradient(180deg,#020617,#081225,#0B1630);
}

/* Grid */
.stApp::before{
content:"";
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
background-image:
linear-gradient(rgba(91,140,255,0.05) 1px, transparent 1px),
linear-gradient(90deg, rgba(91,140,255,0.05) 1px, transparent 1px);
background-size:40px 40px;
pointer-events:none;
z-index:-1;
}

/* Hide sidebar */
[data-testid="stSidebar"]{
display:none;
}

/* Title */
.title{
text-align:center;
font-size:72px;
font-weight:700;
color:white;
margin-top:20px;
letter-spacing:2px;
text-shadow:
0 0 20px rgba(91,140,255,0.5),
0 0 40px rgba(91,140,255,0.3);
}

.subtitle{
text-align:center;
font-size:22px;
color:#94a3b8;
margin-bottom:40px;
}

/* Cards */
.card{
background:rgba(10,20,40,0.75);
backdrop-filter:blur(20px);
border:1px solid rgba(91,140,255,0.15);
border-radius:20px;
padding:20px;
margin-bottom:20px;
box-shadow:0 0 20px rgba(59,130,246,0.15);
}

.card-title{
font-size:30px;
font-weight:700;
color:white;
margin-bottom:10px;
}

.card-text{
font-size:16px;
line-height:1.8;
color:#cbd5e1;
}

/* Buttons */
.stButton>button{
height:48px;
background:linear-gradient(90deg,#2563eb,#3b82f6);
border:none;
border-radius:12px;
font-size:16px;
font-weight:600;
color:white;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================

st.markdown("""
<div class='title'>
FlowSense AI
</div>

<div class='subtitle'>
Event-Driven Congestion Intelligence Platform
</div>
""", unsafe_allow_html=True)

# ================= OVERVIEW =================

st.markdown("""
<div class='card'>

<div class='card-title'>
Overview
</div>

<div class='card-text'>

Historical analytics and city-wide traffic intelligence.

• Event trends

• Peak hours

• Corridor risk analysis

• Event causes

• Duration statistics

</div>

</div>
""", unsafe_allow_html=True)

if st.button("Open Overview", use_container_width=True):
    st.switch_page("pages/1_Overview.py")

# ================= OPERATIONS CENTER =================

st.markdown("""
<div class='card'>

<div class='card-title'>
Operations Center
</div>

<div class='card-text'>

Real-time forecasting and deployment planning.

• Historical intelligence

• Duration prediction

• Officers recommendation

• Barricades recommendation

• Diversion planning

• Command summary

</div>

</div>
""", unsafe_allow_html=True)

if st.button("Open Operations Center", use_container_width=True):
    st.switch_page("pages/2_Operations_Center.py")

# ================= POST EVENT LEARNING =================

st.markdown("""
<div class='card'>

<div class='card-title'>
Post Event Learning
</div>

<div class='card-text'>

Institutional memory and continuous improvement.

• Actual outcomes

• Officer observations

• Lessons learned

• Recommendations

• Knowledge repository

</div>

</div>
""", unsafe_allow_html=True)

if st.button("Open Post Event Learning", use_container_width=True):
    st.switch_page("pages/3_Post_Event_Learning.py")