import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="OT GUI Launcher", layout="wide")

# TITLE
st.markdown("<h1 style='text-align:center;'>OT GUI Launcher</h1>", unsafe_allow_html=True)

# ============================
# ✅ HTML + CSS + JS
# ============================

html_code = """
<style>

body {
    font-family: sans-serif;
}

/* GRID */
.container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 22px;
    margin-top: 40px;
}

.container-2 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
    margin-top: 40px;
}

/* CARDS */
.card {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    cursor: pointer;
    font-weight: 600;
    border: 1px solid #ccc;
    background: white;
    transition: 0.2s;
}
.card:hover {
    background: #f1f1f1;
}

/* ACTIONS BOX */
.action-box {
    display: none;
    padding: 15px;
    margin-top: 10px;
    border-radius: 10px;
    border: 1px solid #ddd;
    background: #fafafa;
}
.action-box button {
    width: 100%;
    padding: 8px;
    margin: 6px 0;
    border-radius: 6px;
    border: 1px solid #ccc;
    background: white;
    cursor: pointer;
}
.action-box button:hover {
    background: #e5e5e5;
}

/* ✅ COPILOT BUTTON — stays bottom right */
.copilot-btn {
    position: fixed;
    bottom: 1300px;
    right: 28px;
    width: 62px;
    height: 62px;
    border-radius: 50%;
    background: #0ea5e9;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    color: white;
    cursor: pointer;
    box-shadow: 0 5px 12px rgba(0,0,0,0.25);
    z-index: 999;
}

/* ✅ COPILOT PANEL — FIXED AT SCREEN MIDDLE (NO SCROLL NEEDED) */
#copilot-panel {
    display: none;
    position: fixed;
    top: 25vh;          /* ✅ MIDDLE OF THE SCREEN */
    right: 40px;
    width: 360px;
    height: 420px;
    background: white;
    border-radius: 12px;
    border: 1px solid #ccc;
    padding: 20px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.25);
    overflow-y: auto;
    z-index: 2000;
}

</style>

<!-- ✅ SECTIONS GRID -->
<div class="container">

    <div>
        <div class="card" onclick="toggle('Opening')">Opening</div>
        <div id="Opening" class="action-box">
            <button>Open Project</button>
            <button>Open Folder</button>
            <button>Load PLC File</button>
        </div>
    </div>

    <div>
        <div class="card" onclick="toggle('Versioning')">Versioning</div>
        <div id="Versioning" class="action-box">
            <button>Git Pull</button>
            <button>Git Diff</button>
            <button>Git Status</button>
        </div>
    </div>

    <div>
        <div class="card" onclick="toggle('Backup')">Backup</div>
        <div id="Backup" class="action-box">
            <button>Backup Now</button>
            <button>Restore Backup</button>
            <button>Export Logs</button>
        </div>
    </div>

    <div>
        <div class="card" onclick="toggle('Project')">Project Creation</div>
        <div id="Project" class="action-box">
            <button>New Project</button>
            <button>New Template</button>
            <button>Init Structure</button>
        </div>
    </div>

</div>

<div class="container-2">

    <div>
        <div class="card" onclick="toggle('Compilation')">Compilation</div>
        <div id="Compilation" class="action-box">
            <button>Build Project</button>
            <button>View Logs</button>
            <button>Diagnostics</button>
        </div>
    </div>

    <div>
        <div class="card" onclick="toggle('Simulation')">Simulation</div>
        <div id="Simulation" class="action-box">
            <button>Start Simulation</button>
            <button>Stop Simulation</button>
            <button>Simulation Logs</button>
        </div>
    </div>

    <div>
        <div class="card" onclick="toggle('Export')">Export / Push</div>
        <div id="Export" class="action-box">
            <button>Export Package</button>
            <button>Push to Git</button>
            <button>Generate Report</button>
        </div>
    </div>

</div>

<!-- ✅ FLOATING ROBOT -->
<div class="copilot-btn" onclick="toggleCopilot()">🤖</div>

<!-- ✅ COPILOT PANEL (MID-SCREEN) -->
<div id="copilot-panel">
    <h3>OT Copilot</h3>
    <p style='opacity:0.6'>(Backend incoming…)</p>
</div>

<script>
function toggle(id) {
    let box = document.getElementById(id);
    box.style.display = (box.style.display === "block") ? "none" : "block";
}

function toggleCopilot() {
    let panel = document.getElementById("copilot-panel");
    panel.style.display = (panel.style.display === "block") ? "none" : "block";
}
</script>
"""

components.html(html_code, height=1200, scrolling=True)
