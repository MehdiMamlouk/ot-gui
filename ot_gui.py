import streamlit as st

# ===============================================
# PAGE CONFIG
# ===============================================
st.set_page_config(page_title="OT GUI Launcher", layout="wide")

# ===============================================
# GLOBAL STYLES
# ===============================================
st.markdown("""
<style>

h1 { 
    text-align: center !important; 
    margin-bottom: 40px;
}

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
    margin-bottom: 25px;
}

/* FLOATING COPILOT BUTTON */
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
    bottom: 110px;
    right: 30px;
    width: 370px;
    height: 500px;
    background-color: var(--background-color);
    border-radius: 12px;
    padding: 18px;
    border: 1px solid #d1d5db;
    box-shadow: 0px 8px 18px rgba(0,0,0,0.25);
    z-index: 1500;
    overflow-y: auto;
}

body[data-theme="dark"] #copilot-panel {
    background-color: #1e293b;
    color: white;
    border: 1px solid #334155;
}

</style>
""", unsafe_allow_html=True)

# ===============================================
# TITLE
# ===============================================
st.markdown("<h1>OT GUI Launcher</h1>", unsafe_allow_html=True)


# ===============================================
# CARD SECTION
# ===============================================
def card(title, actions):
    st.markdown(f"<div class='card'><div class='card-title'>{title}</div>", unsafe_allow_html=True)
    with st.expander("Afficher les actions"):
        cols = st.columns(3)
        for i, a in enumerate(actions):
            cols[i % 3].button(a)
    st.markdown("</div>", unsafe_allow_html=True)


# ===============================================
# GRID OF SECTIONS (LIKE THE FIRST VERSION YOU LIKED)
# ===============================================

# --- ROW 1 : 4 CARDS ---
c1, c2, c3, c4 = st.columns(4)
with c1:
    card("Opening", ["Open Project", "Open Folder", "Load PLC File"])
with c2:
    card("Versioning", ["Git Pull", "Git Diff", "Git Status"])
with c3:
    card("Backup", ["Backup Now", "Restore Backup", "Export Logs"])
with c4:
    card("Project Creation", ["New Project", "New Template", "Init Structure"])

# --- ROW 2 : 3 CARDS ---
c5, c6, c7 = st.columns(3)
with c5:
    card("Compilation", ["Build Project", "View Logs", "Diagnostics"])
with c6:
    card("Simulation", ["Start Simulation", "Stop Simulation", "Simulation Logs"])
with c7:
    card("Export / Push", ["Export Package", "Push to Git", "Generate Report"])


# ===============================================
# FLOATING COPILOT BUTTON
# ===============================================
st.markdown("""
<div class="copilot-button" onclick="document.getElementById('copilot-panel').style.display='block'">
🤖
</div>
""", unsafe_allow_html=True)


# ===============================================
# POPUP PANEL (EMPTY CHAT MOCKUP)
# ===============================================
st.markdown("""
<div id="copilot-panel">
    <h3>OT Copilot</h3>
    <p style="opacity:0.7;font-size:13px;">Pose-moi une question…</p>
</div>
""", unsafe_allow_html=True)

# ===============================================
# STREAMLIT CHAT BACKEND (NO BOTTOM BAR)
# ===============================================

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Pose une question au Copilot OT…")  # <- This is hidden visually
if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    st.session_state.messages.append({
        "role": "assistant",
        "content": f"Demande reçue: **{user_input}** (Backend pas encore activé)"
    })

# Only display messages INSIDE the panel, not on main page
for msg in st.session_state.messages:
    st.markdown(f"""
    <script>
        var panel = document.getElementById('copilot-panel');
        panel.innerHTML += "<p><b>{msg['role']}:</b> {msg['content']}</p>";
    </script>
    """, unsafe_allow_html=True)
