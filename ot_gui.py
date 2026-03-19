import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(page_title="OT GUI Launcher", layout="wide")


# =========================================================
# GLOBAL CSS FIXES (light/dark mode, cards, expanders)
# =========================================================
st.markdown("""
<style>

h1 {
    text-align: center !important;
    margin-bottom: 40px !important;
}

/* CARD STYLE */
.card {
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
}

/* LIGHT MODE */
body[data-theme="light"] .card {
    background-color: #ffffff;
    border: 1px solid #d1d5db;
    color: #1f2937;
}

/* DARK MODE */
body[data-theme="dark"] .card {
    background-color: #1e293b;
    border: 1px solid #334155;
    color: #e2e8f0;
}

/* EXPANDERS CLEAN */
.streamlit-expanderHeader {
    font-size: 15px !important;
    font-weight: 500 !important;
}

/* COPILOT BUTTON */
.copilot-button {
    position: fixed;
    bottom: 28px;
    right: 28px;
    background-color: #0ea5e9;
    width: 62px; height: 62px;
    border-radius: 50%;
    color: white;
    font-size: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0px 5px 14px rgba(0,0,0,0.25);
    z-index: 999;
}

/* COPILOT PANEL */
#copilot-panel {
    display: none;
    position: fixed;
    bottom: 100px;
    right: 30px;
    width: 360px;
    height: 480px;
    border-radius: 12px;
    padding: 18px;
    background-color: white;
    border: 1px solid #d1d5db;
    box-shadow: 0px 10px 20px rgba(0,0,0,0.25);
    z-index: 2000;
    overflow-y: auto;
}

body[data-theme="dark"] #copilot-panel {
    background-color: #1e293b;
    color: #e2e8f0;
    border: 1px solid #334155;
}

/* REMOVE STREAMLIT DEFAULT CHAT BAR */
.stChatInputContainer {
    display: none !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TITLE
# =========================================================
st.markdown("<h1>OT GUI Launcher</h1>", unsafe_allow_html=True)


# =========================================================
# CARD FUNCTION
# =========================================================
def card(title, actions):
    st.markdown(f"<div class='card'><h3 style='margin-top:0;'>{title}</h3>", unsafe_allow_html=True)
    with st.expander("Afficher les actions", expanded=False):
        cols = st.columns(3)
        for i, action in enumerate(actions):
            cols[i % 3].button(action)
    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# GRID LAYOUT — LIKE YOUR ORIGINAL VERSION
# =========================================================

# Row 1 — 4 categories
c1, c2, c3, c4 = st.columns(4)
with c1: card("Opening",        ["Open Project", "Open Folder", "Load PLC File"])
with c2: card("Versioning",     ["Git Pull", "Git Diff", "Git Status"])
with c3: card("Backup",         ["Backup Now", "Restore Backup", "Export Logs"])
with c4: card("Project Creation", ["New Project", "New Template", "Init Structure"])

# Row 2 — 3 categories
c5, c6, c7 = st.columns(3)
with c5: card("Compilation", ["Build Project", "View Logs", "Diagnostics"])
with c6: card("Simulation",  ["Start Simulation", "Stop Simulation", "Simulation Logs"])
with c7: card("Export / Push", ["Export Package", "Push to Git", "Generate Report"])


# =========================================================
# FLOATING COPILOT BUTTON
# =========================================================
st.markdown("""
<div class="copilot-button" onclick="document.getElementById('copilot-panel').style.display='block'">
🤖
</div>
""", unsafe_allow_html=True)


# =========================================================
# COPILOT PANEL (POPUP)
# =========================================================
st.markdown("""
<div id="copilot-panel">
    <h3>OT Copilot</h3>
    <p style="opacity:0.6;font-size:13px;">Pose une question…</p>
    <div id="copilot-chat"></div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# COPILOT BACKEND (messages)
# =========================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# Custom input instead of Streamlit bottom bar
user_input = st.text_input("Pose une question…", key="manual_input")

if st.button("Envoyer"):
    if user_input.strip() != "":
        st.session_state.messages.append(("user", user_input))
        st.session_state.messages.append(("assistant", f"Demande reçue : {user_input}"))
        st.session_state.manual_input = ""


# Inject messages inside copilot panel
for role, content in st.session_state.messages:
    st.markdown(f"""
    <script>
        var panel = document.getElementById('copilot-chat');
        panel.innerHTML += "<p><b>{role}:</b> {content}</p>";
    </script>
    """, unsafe_allow_html=True)
