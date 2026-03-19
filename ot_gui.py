import streamlit as st

st.set_page_config(page_title="OT GUI", layout="wide")

# =========================================================
# ✅ NAVBAR (simple, pro, sticky)
# =========================================================
st.markdown("""
<style>
/* NAVBAR */
.navbar {
    position: fixed;
    top: 0; left: 0;
    width: 100%;
    background-color: #0f172a;
    padding: 12px 25px;
    z-index: 999;
    display: flex;
    align-items: center;
    border-bottom: 1px solid #1e293b;
}
.navbar a {
    color: #e2e8f0;
    margin-right: 25px;
    font-size: 16px;
    text-decoration: none;
}
.navbar a:hover {
    color: #93c5fd;
}
body { padding-top: 70px; }
</style>

<div class="navbar">
    <a href="#">OT GUI</a>
    <a href="#opening">Opening</a>
    <a href="#versioning">Versioning</a>
    <a href="#backup">Backup</a>
    <a href="#creation">Creation</a>
    <a href="#compilation">Compilation</a>
    <a href="#simulation">Simulation</a>
    <a href="#export">Export</a>
</div>
""", unsafe_allow_html=True)


# =========================================================
# ✅ AUTO LIGHT/DARK THEME SUPPORT
# =========================================================
st.markdown("""
<style>

/* LIGHT MODE */
body[data-theme="light"] .card {
    background-color: #ffffff;
    border: 1px solid #d1d5db;
    color: #1f2937;
}
body[data-theme="light"] .card-title {
    color: #1f2937 !important;
}

/* DARK MODE */
body[data-theme="dark"] .card {
    background-color: #1e293b;
    border: 1px solid #334155;
    color: #e2e8f0;
}
body[data-theme="dark"] .card-title {
    color: #e2e8f0 !important;
}

/* CARD STYLE */
.card {
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 18px;
}

/* COPILOT FLOATING BUTTON */
.copilot-button {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background-color: #0ea5e9;
    width: 60px; height: 60px;
    border-radius: 50%;
    color: white;
    font-size: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 1000;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# ✅ REUSABLE CARD SECTION
# =========================================================
def card_section(anchor, title, actions):
    st.markdown(f"<div id='{anchor}'></div>", unsafe_allow_html=True)
    with st.container():
        st.markdown(f"<div class='card'><div class='card-title'>{title}</div>", unsafe_allow_html=True)

        with st.expander("Afficher les actions", expanded=False):
            cols = st.columns(3)
            for i, action in enumerate(actions):
                cols[i % 3].button(action)

        st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# ✅ SECTIONS
# =========================================================
card_section("opening", "Opening", ["Open Project", "Open Folder", "Load PLC File"])
card_section("versioning", "Versioning", ["Git Pull", "Git Diff", "Git Status"])
card_section("backup", "Backup", ["Backup Now", "Restore Backup", "Export Logs"])
card_section("creation", "Project Creation", ["New Project", "New Template", "Init Structure"])
card_section("compilation", "Compilation", ["Build Project", "View Logs", "Diagnostics"])
card_section("simulation", "Simulation", ["Start Simulation", "Stop Simulation", "Simulation Logs"])
card_section("export", "Export / Push", ["Export Package", "Push to Git", "Generate Report"])


# =========================================================
# ✅ COPILOT (floating icon → opens chat)
# =========================================================

# Floating Chat Button
st.markdown("""
<div class="copilot-button" onclick="document.getElementById('copilot-box').style.display='block'">
🤖
</div>
""", unsafe_allow_html=True)

# Hidden Chat Box
with st.container():
    st.markdown("""
    <div id="copilot-box" style="
        display:none;
        position:fixed;
        bottom:100px;
        right:30px;
        width:350px;
        height:420px;
        background-color:white;
        border-radius:12px;
        padding:15px;
        box-shadow:0px 0px 12px rgba(0,0,0,0.25);
        z-index:1100;
    ">
        <h4>OT Copilot</h4>
    </div>
    """, unsafe_allow_html=True)

# Streamlit Chat Logic
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.write("### 🤖 OT Copilot (Debug Panel)")
    for msg in st.session_state.messages:
        st.write(msg)

user_input = st.chat_input("Pose une question au Copilot OT…")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({
        "role": "assistant",
        "content": f"Tu as demandé : **{user_input}**.\n\n👉 Le vrai backend arrive bientôt !"
    })
    st.chat_message("assistant").markdown(
        f"✅ Commande reçue : **{user_input}**\n\nJe suis ton futur Copilot OT 🤖"
    )
