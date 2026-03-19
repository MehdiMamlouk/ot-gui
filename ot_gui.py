import streamlit as st

st.set_page_config(page_title="OT GUI Launcher", layout="wide")

# -------------------------------------------------------------
# ✅ GLOBAL STYLE (Light/Dark + Cards + Clickable Sections)
# -------------------------------------------------------------
st.markdown("""
<style>

h1 {
    text-align: center !important;
    margin-bottom: 40px !important;
}

/* CARDS (titles only) */
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

/* DARK MODE */
body[data-theme="dark"] .card {
    background-color: #1e293b;
    border: 1px solid #334155;
    color: #e2e8f0;
}
body[data-theme="dark"] .card:hover {
    background-color: #334155;
}

/* ACTION BOX (hidden by default) */
.action-box {
    display: none;
    margin-top: 10px;
    padding: 12px;
    border-radius: 10px;
}

/* LIGHT */
body[data-theme="light"] .action-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
}

/* DARK */
body[data-theme="dark"] .action-box {
    background: #1e293b;
    border: 1px solid #475569;
}

/* ---------------------------------------------------
   ✅ COPILOT FLOATING BUTTON
--------------------------------------------------- */
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
    box-shadow: 0px 5px 14px rgba(0,0,0,0.25);
    z-index: 999;
}

/* ---------------------------------------------------
   ✅ COPILOT PANEL POPUP
--------------------------------------------------- */
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
    background: #1e293b;
    color: white;
    border: 1px solid #475569;
}

/* ---------------------------------------------------
✅ REMOVE STREAMLIT CHAT BAR
--------------------------------------------------- */
.stChatInputContainer { display: none !important; }

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# ✅ TITLE
# -------------------------------------------------------------
st.markdown("<h1>OT GUI Launcher</h1>", unsafe_allow_html=True)

# -------------------------------------------------------------
# ✅ DATA MODEL (titles + actions)
# -------------------------------------------------------------
SECTIONS = {
    "Opening": ["Open Project", "Open Folder", "Load PLC File"],
    "Versioning": ["Git Pull", "Git Diff", "Git Status"],
    "Backup": ["Backup Now", "Restore Backup", "Export Logs"],
    "Project Creation": ["New Project", "New Template", "Init Structure"],
    "Compilation": ["Build Project", "View Logs", "Diagnostics"],
    "Simulation": ["Start Simulation", "Stop Simulation", "Simulation Logs"],
    "Export / Push": ["Export Package", "Push to Git", "Generate Report"]
}

# -------------------------------------------------------------
# ✅ GRID LAYOUT : 4 cards on row 1, 3 cards on row 2
# -------------------------------------------------------------

# Row 1
r1 = st.columns(4)
for i, title in enumerate(list(SECTIONS.keys())[:4]):
    with r1[i]:
        st.markdown(f"<div class='card' onclick=\"toggle('{title}')\">{title}</div>", unsafe_allow_html=True)
        st.markdown(f"<div id='{title}' class='action-box'></div>", unsafe_allow_html=True)

# Row 2
r2 = st.columns(3)
for i, title in enumerate(list(SECTIONS.keys())[4:]):
    with r2[i]:
        st.markdown(f"<div class='card' onclick=\"toggle('{title}')\">{title}</div>", unsafe_allow_html=True)
        st.markdown(f"<div id='{title}' class='action-box'></div>", unsafe_allow_html=True)

# -------------------------------------------------------------
# ✅ JS TOGGLE FOR ACTIONS
# -------------------------------------------------------------
actions_js = ""
for title, actions in SECTIONS.items():
    html_actions = "".join([f"<button style='margin:4px;padding:6px 12px;border-radius:6px;'>{a}</button>" 
                            for a in actions])
    actions_js += f"actions['{title}'] = `{html_actions}`;\n"

st.markdown(f"""
<script>
let actions = {{}};
{actions_js}

function toggle(id) {{
    let box = document.getElementById(id);
    box.style.display = (box.style.display === "none" || box.style.display === "") 
                        ? "block" : "none";
    box.innerHTML = actions[id];
}}
</script>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# ✅ FLOATING COPILOT BUTTON
# -------------------------------------------------------------
st.markdown("""
<div class="copilot-button" onclick="document.getElementById('copilot-panel').style.display='block'">
🤖
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# ✅ POPUP COPILOT PANEL
# -------------------------------------------------------------
st.markdown("""
<div id="copilot-panel">
    <h3>OT Copilot</h3>
    <p style="opacity:0.6;font-size:13px;">Pose une question…</p>
    <div id="copilot-chat"></div>
</div>
""", unsafe_allow_html=True)
