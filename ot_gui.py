import streamlit as st

# ===============================================
# CONFIGURATION PAGE
# ===============================================
st.set_page_config(page_title="OT GUI Launcher", layout="wide")

# ===============================================
# GLOBAL STYLE
# ===============================================
st.markdown("""
<style>

h1 { text-align: center !important; }

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

/* COPILOT BUTTON */
.copilot-fab {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background-color: #0ea5e9;
    width: 62px; height: 62px;
    border-radius: 50%;
    color: white;
    font-size: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 999;
    box-shadow: 0 4px 14px rgba(0,0,0,0.28);
}

/* COPILOT PANEL */
#copilot-panel {
    display: none;
    position: fixed;
    bottom: 100px;
    right: 30px;
    width: 370px;
    height: 500px;
    background-color: white;
    border-radius: 12px;
    padding: 18px;
    border: 1px solid #d1d5db;
    box-shadow: 0 8px 18px rgba(0,0,0,0.22);
    z-index: 1500;
    overflow-y: auto;
}

body[data-theme="dark"] #copilot-panel {
    background-color: #1e293b;
    border: 1px solid #334155;
    color: #e2e8f0;
}

</style>
""", unsafe_allow_html=True)


# ===============================================
# TITLE
# ===============================================
st.markdown("<h1>OT GUI Launcher</h1>", unsafe_allow_html=True)
st.write("")


# ===============================================
# CARD SECTION FUNCTION
# ===============================================
def card_section(title, actions):
    st.markdown(f"<div class='card'><div class='card-title'>{title}</div>", unsafe_allow_html=True)
    with st.expander("Afficher les actions", expanded=False):
        cols = st.columns(3)
        for i, action in enumerate(actions):
            cols[i % 3].button(action)
    st.markdown("</div>", unsafe_allow_html=True)


# ===============================================
# SECTIONS
# ===============================================
card_section("Opening", ["Open Project", "Open Folder", "Load PLC File"])
card_section("Versioning", ["Git Pull", "Git Diff", "Git Status"])
card_section("Backup", ["Backup Now", "Restore Backup", "Export Logs"])
card_section("Project Creation", ["New Project", "New Template", "Init Structure"])
card_section("Compilation", ["Build Project", "View Logs", "Diagnostics"])
card_section("Simulation", ["Start Simulation", "Stop Simulation", "Simulation Logs"])
card_section("Export / Push", ["Export Package", "Push to Git", "Generate Report"])


# ===============================================
# COPILOT FLOATING BUTTON (RIGHT BOTTOM)
# ===============================================
st.markdown("""
<div class="copilot-fab" onclick="document.getElementById('copilot-panel').style.display='block'">
🤖
</div>
""", unsafe_allow_html=True)


# ===============================================
# COPILOT CHAT PANEL
# ===============================================
st.markdown("""
<div id="copilot-panel">
    <h3>OT Copilot</h3>
    <p style="font-size: 13px; opacity: 0.7;">Pose-moi des questions sur l’OT, le PLC, Git, DevOps...</p>
</div>
""", unsafe_allow_html=True)


# ===============================================
# STREAMLIT CHAT BACKEND (MOCK)
# ===============================================
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Pose une question au Copilot OT…")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({
        "role": "assistant",
        "content": f"Tu as demandé : **{user_input}**.\n\n👉 Le backend OT arrivera ensuite."
    })

# Display inside panel
with st.container():
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).markdown(msg["content"])
``
