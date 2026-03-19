import streamlit as st

st.set_page_config(page_title="OT GUI Launcher", layout="wide")

# ======================================================
# ✅ GLOBAL STYLES
# ======================================================
st.markdown("""
<style>

h1 {
    text-align: center !important;
    margin-bottom: 40px !important;
}

/* CARD */
.card {
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    cursor: pointer;
    margin-bottom: 22px;
    transition: 0.2s ease;
    font-weight: 600;
}

/* LIGHT MODE */
body[data-theme="light"] .card {
    background-color: #ffffff;
    border: 1px solid #d1d5db;
    color: #1f2937;
}
body[data-theme="light"] .card:hover {
    background-color: #f3f4f6;
}
body[data-theme="light"] .action-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
}

/* DARK MODE */
body[data-theme="dark"] .card {
    background-color: #1e293b;
    border: 1px solid #334155;
    color: #e2e8f0;
}
body[data-theme="dark"] .card:hover {
    background-color: #334155;
}
body[data-theme="dark"] .action-box {
    background: #1e293b;
    border: 1px solid #475569;
}

/* ACTION BOX */
.action-box {
    display: none;
    margin-top: 10px;
    padding: 12px;
    border-radius: 10px;
}

/* REMOVE STREAMLIT CHAT BAR */
.stChatInputContainer { display: none !important; }

/* COPILOT BUTTON */
.copilot-button {
    position: fixed;
    bottom: 28px;
    right: 28px;
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
    box-shadow: 0 5px 14px rgba(0,0,0,0.25);
}

/* COPILOT PANEL */
#copilot-panel {
    display: none;
    position: fixed;
    bottom: 100px;
    right: 30px;
    width: 360px;
    height: 500px;
    border-radius: 12px;
    padding: 18px;
    background-color: white;
    border: 1px solid #d1d5db;
    box-shadow: 0px 10px 22px rgba(0,0,0,0.25);
    z-index: 2000;
    overflow-y: auto;
}
body[data-theme="dark"] #copilot-panel {
    background-color: #1e293b;
    color: white;
    border: 1px solid #475569;
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# ✅ TITLE
# ======================================================
st.markdown("<h1>OT GUI Launcher</h1>", unsafe_allow_html=True)

# ======================================================
# ✅ DATA (sections + actions)
# ======================================================
SECTIONS = {
    "Opening": ["Open Project", "Open Folder", "Load PLC File"],
    "Versioning": ["Git Pull", "Git Diff", "Git Status"],
    "Backup": ["Backup Now", "Restore Backup", "Export Logs"],
    "Project Creation": ["New Project", "New Template", "Init Structure"],
    "Compilation": ["Build Project", "View Logs", "Diagnostics"],
    "Simulation": ["Start Simulation", "Stop Simulation", "Simulation Logs"],
    "Export / Push": ["Export Package", "Push to Git", "Generate Report"]
}

# ======================================================
# ✅ GRID LAYOUT (4 + 3)
# ======================================================
# Row 1
cols1 = st.columns(4)
for i, (title, actions) in enumerate(list(SECTIONS.items())[:4]):
    with cols1[i]:
        st.markdown(f"<div class='card' onclick=\"toggle('{title}')\">{title}</div>", unsafe_allow_html=True)
        st.markdown(f"<div id='{title}' class='action-box'></div>", unsafe_allow_html=True)

# Row 2
cols2 = st.columns(3)
for i, (title, actions) in enumerate(list(SECTIONS.items())[4:]):
    with cols2[i]:
        st.markdown(f"<div class='card' onclick=\"toggle('{title}')\">{title}</div>", unsafe_allow_html=True)
        st.markdown(f"<div id='{title}' class='action-box'></div>", unsafe_allow_html=True)

# ======================================================
# ✅ JAVASCRIPT FOR OPEN/CLOSE + INSERT ACTION BUTTONS
# ======================================================
actions_js = ""
for title, actions in SECTIONS.items():
    html_buttons = "".join(
        [f"<button style='margin:4px;padding:6px 12px;border-radius:6px;'>{a}</button>" 
         for a in actions]
    )
    actions_js += f"actions['{title}'] = `{html_buttons}`;\n"

st.markdown(f"""
<script>
let actions = {{}};
{actions_js}

function toggle(id) {{
    let box = document.getElementById(id);
    if (box.style.display === "none" || box.style.display === "") {{
        box.style.display = "block";
        box.innerHTML = actions[id];
    }} else {{
        box.style.display = "none";
    }}
}}
</script>
""", unsafe_allow_html=True)

# ======================================================
# ✅ FLOATING COPILOT BUTTON
# ======================================================
st.markdown("""
<div class="copilot-button" onclick="document.getElementById('copilot-panel').style.display='block'">
🤖
</div>
""", unsafe_allow_html=True)

# ======================================================
# ✅ COPILOT PANEL (empty for now)
# ======================================================
st.markdown("""
<div id="copilot-panel">
    <h3>OT Copilot</h3>
    <p style="opacity:0.6;font-size:13px;">Pose une question…</p>
    <div id="copilot-chat"></div>
</div>
""", unsafe_allow_html=True)
