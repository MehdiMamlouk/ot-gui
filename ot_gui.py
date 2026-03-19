import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="OT GUI Launcher", layout="wide")

st.markdown("""
<h1 style="
    text-align:center;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight:700;
    margin-top:10px;
    margin-bottom:40px;
    color:#1e2a47;
">
OT GUI Launcher
</h1>
""", unsafe_allow_html=True)

html = """
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>
body {
    font-family: 'Plus Jakarta Sans', sans-serif;
    background: linear-gradient(180deg, #f8fafc 0%, #eef2f7 100%);
    margin: 0;
    color: #1e2a47;
}

/* ---------------- GRID ---------------- */
.container, .container-2 {
    display: grid;
    gap: 26px;
}
.container { grid-template-columns: repeat(4, 1fr); margin-top: 25px; }
.container-2 { grid-template-columns: repeat(3, 1fr); margin-top: 30px; }

/* ---------------- CARDS (PREMIUM) ---------------- */
.card {
    padding: 18px;
    border-radius: 18px;
    background: rgba(255, 255, 255, 0.5);
    backdrop-filter: blur(11px);
    border: 1px solid rgba(255,255,255,0.35);
    color: #24375b;
    font-weight: 600;
    text-align:center;
    cursor:pointer;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.08);
    transition: all 0.20s ease;
}

.card:hover {
    background: rgba(255,255,255,0.75);
    transform: translateY(-4px) scale(1.02);
    box-shadow: 0px 10px 28px rgba(0,0,0,0.12);
}

/* ---------------- ACTION BOX ---------------- */
.action-box {
    display:none;
    padding: 18px;
    margin-top: 12px;
    border-radius: 14px;
    border: 1px solid #d8dee9;
    background: #f1f5f9;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.06);
    animation: fadeIn 0.25s ease-out;
}

@keyframes fadeIn {
    from { opacity:0; transform:translateY(-4px); }
    to   { opacity:1; transform:translateY(0); }
}

.action-box button {
    width:100%;
    padding:12px 14px;
    margin:6px 0;
    border-radius:10px;
    background:#ffffff;
    border:1px solid #cbd5e1;
    font-weight:500;
    cursor:pointer;
    font-size:14px;
    transition:0.18s ease;
}
.action-box button:hover {
    background:#e2e8f0;
    border-color:#94a3b8;
    transform: scale(1.02);
}

/* ---------------- COPILOT BUTTON ---------------- */
.copilot-btn {
    position: fixed;
    bottom: 28px;
    right: 28px;
    width: 68px;
    height: 68px;
    border-radius: 50%;
    background: #1e2a47;
    color:white;
    font-size:32px;
    display:flex;
    align-items:center;
    justify-content:center;
    cursor:pointer;
    box-shadow:0px 10px 28px rgba(0,0,0,0.22);
    transition:0.25s;
    z-index:900;
}

.copilot-btn:hover {
    background:#24375b;
    transform:scale(1.08);
}

/* ---------------- COPILOT PANEL ---------------- */
#copilot-panel {
    display:none;
    position: fixed;
    top:18vh;
    right:135px;
    width:400px;
    height:500px;
    background:white;
    border-radius:18px;
    border:1px solid #e2e8f0;
    padding:26px;
    box-shadow:0px 18px 44px rgba(0,0,0,0.18);
    overflow-y:auto;
    animation: slideIn 0.28s ease-out;
    z-index:999;
    font-family:'Plus Jakarta Sans';
}

@keyframes slideIn {
    from { opacity:0; transform:translateY(22px); }
    to   { opacity:1; transform:translateY(0); }
}

/* Close button */
.close-btn {
    position:absolute;
    top:14px;
    right:14px;
    width:30px;
    height:30px;
    border-radius:50%;
    background:#e5e7eb;
    display:flex;
    align-items:center;
    justify-content:center;
    cursor:pointer;
    transition:0.15s;
}
.close-btn:hover { background:#cbd5e1; }
</style>


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

<div class="copilot-btn" onclick="toggleCopilot()">🤖</div>

<div id="copilot-panel">
    <div class="close-btn" onclick="toggleCopilot()">✕</div>
    <h3 style="margin-top:0; font-weight:700;">OT Copilot</h3>
    <p style="opacity:0.65;font-size:14px;">Pose une question…</p>
</div>

<script>
function toggle(id) {
    let box = document.getElementById(id);
    box.style.display = (box.style.display === "block") ? "none" : "block";
}
function toggleCopilot() {
    let p = document.getElementById("copilot-panel");
    p.style.display = (p.style.display === "block") ? "none" : "block";
}
</script>
"""

components.html(html, height=1500, scrolling=True)
