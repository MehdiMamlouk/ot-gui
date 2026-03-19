import streamlit as st

st.set_page_config(page_title="OT GUI Launcher", layout="wide")

# ============================================================================
# ✅ NAVBAR (Design PRO)
# ============================================================================
st.markdown("""
<style>
.navbar {
    position: fixed;
    top: 0; 
    left: 0;
    right: 0;
    height: 60px;
    background-color: #0f172a;
    display: flex;
    align-items: center;
    padding-left: 25px;
    gap: 25px;
    z-index: 999;
    border-bottom: 1px solid #1e293b;
}
.navbar-item {
    color: #e2e8f0;
    text-decoration: none;
    font-size: 17px;
}
.navbar-item:hover {
    color: #93c5fd;
}
body { padding-top: 70px; }
</style>

<div class="navbar">
    <a class="navbar-item" href="#">OT GUI Launcher</a>
    <a class="navbar-item" href="#opening">Opening</a>
    <a class="navbar-item" href="#versioning">Versioning</a>
    <a class="navbar-item" href="#backup">Backup</a>
    <a class="navbar-item" href="#creation">Creation</a>
    <a class="navbar-item" href="#compilation">Compilation</a>
    <a class="navbar-item" href="#simulation">Simulation</a>
    <a class="navbar-item" href="#export">Export</a>
</div>
""", unsafe_allow_html=True)

st.title("OT GUI Launcher")
st.write("")  # spacing


# ============================================================================
# ✅ AUTO DARK/LIGHT MODE — CARDS CLEAN
# ============================================================================
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
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================================
# ✅ CARD SECTION FUNCTION
# ============================================================================
def card_section(anchor, title, actions):
    st.markdown(f"<div id='{anchor}'></div>", unsafe_allow_html=True)

    st.markdown(f"""
        <div class="card">
            <div class="card-title">{title}</div>
        """, unsafe_allow_html=True)

    with st.expander("Afficher les actions", expanded=False):
        cols = st.columns(3)
        for i, action in enumerate(actions):
            cols[i % 3].button(action)

    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================================
# ✅ SECTIONS
# ============================================================================
card_section("opening", "Opening",
             ["Open Project", "Open Folder", "Load PLC File"])

card_section("versioning", "Versioning",
             ["Git Pull", "Git Diff", "Git Status"])

card_section("backup", "Backup",
             ["Backup Now", "Restore Backup", "Export Logs"])

card_section("creation", "Project Creation",
             ["New Project", "New Template", "Init Structure"])

card_section("compilation", "Compilation",
             ["Build Project", "View Logs", "Diagnostics"])

card_section("simulation", "Simulation",
             ["Start Simulation", "Stop Simulation", "Simulation Logs"])

card_section("export", "Export / Push",
             ["Export Package", "Push to Git", "Generate Report"])



# ============================================================================
# ✅ FLOATING COPILOT BUTTON (BOTTOM RIGHT)
# ============================================================================
st.markdown("""
<style>
.copilot-fab {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background-color: #0ea5e9;
    width: 60px; height: 60px;
    border-radius: 50%;
    color: white;
    font-size: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 999;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
}
</style>

<div class="copilot-fab" onclick="document.getElementById('copilot-panel').style.display='block'">
🤖
</div>
""", unsafe_allow_html=True)


# ============================================================================
# ✅ COPILOT POPUP PANEL — MODERN UI
# ============================================================================
st.markdown("""
<style>
#copilot-panel {
    display:none;
    position: fixed;
    bottom: 100px;
    right: 25px;
    width: 360px;
    height: 480px;
    background-color: white;
    border-radius: 12px;
    padding: 15px;
    border: 1px solid #d1d5db;
    box-shadow: 0 8px 18px rgba(0,0,0,0.25);
    z-index: 2000;
}

body[data-theme="dark"] #copilot-panel {
    background-color: #1e293b;
    color: white;
    border: 1px solid #334155;
}
</style>

<div id="copilot-panel">
    <h4>OT Copilot</h4>
</div>
""", unsafe_allow_html=True)


# ============================================================================
# ✅ STREAMLIT CHAT LOGIC (backend mock)
# ============================================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("#### ")
user_input = st.chat_input("Pose une question au Copilot OT…")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({
        "role": "assistant",
        "content": f"Tu as demandé : **{user_input}**.\n\n👉 Le backend OT arrivera ensuite."
    })
    st.chat_message("assistant").markdown(
        f"✅ Reçu : **{user_input}**\n\nJe suis ton futur Copilot OT 🤖"
    )
