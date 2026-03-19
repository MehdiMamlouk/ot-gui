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
    from { opacity: 0; transform: translateY(-3px); }
    to   { opacity: 1; transform: translateY(0px); }
}

/* Buttons inside */
.action-box button {
    width: 100%;
    padding: 10px 14px;
    margin: 6px 0;
    border-radius: 8px;
    border: 1px solid #d1d5db;
    background: white;
    cursor: pointer;
    font-size: 14px;
    font-weight: 500;
    transition: 0.15s;
}

.action-box button:hover {
    background: #e2e8f0;
    border-color: #cbd5e1;
}

/* -------------------- COPILOT BUTTON -------------------- */
.copilot-btn {
    position: fixed;
    bottom: 708px;
    right: 18px;
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: #0284c7;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    color: white;
    cursor: pointer;
    box-shadow: 0px 7px 18px rgba(0,0,0,0.22);
    transition: 0.2s;
    z-index: 998;
}

.copilot-btn:hover {
    background: #0369a1;
    transform: translateY(-3px);
}

/* -------------------- COPILOT PANEL -------------------- */
#copilot-panel {
    display: none;
    position: fixed;
    top: 22vh;                 /* ✅ REMONTÉ TRÈS HAUT */
    right: 35px;
    width: 380px;
    height: 460px;
    background: white;
    border-radius: 14px;
    border: 1px solid #e2e8f0;
    padding: 20px;
    box-shadow: 0px 12px 30px rgba(0,0,0,0.20);
    overflow-y: auto;
    animation: slidein 0.25s ease-out;
    z-index: 999;
}

@keyframes slidein {
    from { opacity:0; transform:translateY(15px); }
    to   { opacity:1; transform:translateY(0px); }
}

/* Close button */
.close-btn {
    position:absolute;
    top:12px;
    right:12px;
    background:#e5e7eb;
    width:30px;
    height:30px;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    cursor:pointer;
    transition:0.2s;
}
.close-btn:hover { background:#cbd5e1; }

</style>


<!-- ===================================================== -->
<!-- ✅ SECTIONS GRID (Clickable) -->
<!-- ===================================================== -->

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

<!-- ===================================================== -->
<!-- ✅ COPILOT BUTTON (Floating) -->
<!-- ===================================================== -->
<div class="copilot-btn" onclick="toggleCopilot()">🤖</div>

<!-- ===================================================== -->
<!-- ✅ COPILOT PANEL -->
<!-- ===================================================== -->
<div id="copilot-panel">
    <div class="close-btn" onclick="toggleCopilot()">✕</div>
    <h3 style="margin-top:0;">OT Copilot</h3>
    <p style='opacity:0.65;font-size:14px;'>Pose une question…</p>
</div>

<script>
function toggle(section) {
    let box = document.getElementById(section);
    box.style.display = (box.style.display === "block") ? "none" : "block";
}

function toggleCopilot() {
    let panel = document.getElementById("copilot-panel");
    panel.style.display = (panel.style.display === "block") ? "none" : "block";
}
</script>
"""

components.html(html, height=1400, scrolling=True)
