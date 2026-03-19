import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="OT GUI Launcher", layout="wide")

# Title
st.markdown("""
<h1 style="
    text-align:center;
    font-family: 'Inter', sans-serif;
    font-weight:700;
    margin-top:10px;
    margin-bottom:40px;
">
OT GUI Launcher
</h1>
""", unsafe_allow_html=True)

# ===============================================================
# ✅ HTML / CSS / JS VERSION PRO (Figma-like)
# ===============================================================

html = """
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>

body {
    font-family: 'Inter', sans-serif;
    background: #f7f9fb;
}

/* -------------------- GRID -------------------- */
.container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 26px;
    margin-top: 20px;
}

.container-2 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 26px;
    margin-top: 30px;
}

/* -------------------- CARDS -------------------- */
.card {
    padding: 22px;
    border-radius: 14px;
    text-align: center;
    cursor: pointer;
    font-weight: 600;
    background: white;
    border: 1px solid #e5e7eb;
    color: #111827;
    transition: all 0.18s;
    box-shadow: 0px 1px 3px rgba(0,0,0,0.04);
}

.card:hover {
    background: #f0f4f8;
    border-color: #cbd5e1;
    transform: translateY(-2px);
}

/* -------------------- ACTION BOX -------------------- */
.action-box {
    display: none;
    padding: 14px;
    margin-top: 12px;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
    background: #f9fafb;
    box-shadow: 0px 1px 3px rgba(0,0,0,0.05);
    animation: fadein 0.2s ease-out;
}

@keyframes fadein {
