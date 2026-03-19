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
    color:#0f172a;
">
OT GUI Launcher
</h1>
""", unsafe_allow_html=True)

html = """
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>

body {
    font-family: 'Inter', sans-serif;
    background: #f5f7fa;
    color: #1e293b;
    margin: 0;
}

/* ---------------- GRID ---------------- */
.container, .container-2 {
    display: grid;
    gap: 26px;
}
.container  { grid-template-columns: repeat(4, 1fr); margin-top: 25px; }
.container-2 { grid-template-columns: repeat(3, 1fr); margin-top: 30px; }

/* ---------------- CARDS ---------------- */
.card {
    padding: 18px;
    border-radius: 14px;
    background: white;
    border: 1px solid #e2e8f0;
    color: #0f172a;
    font-weight: 600;
    text-align:center;
    cursor:pointer;
    box-shadow: 0px 1px 4px rgba(0,0,0,0.05);
    transition: all 0.15s ease;
}

.card:hover {
    background: #eef2f7;
    border-color:#cbd5e1;
    transform: translateY(-2px);
}

/* ---------------- ACTION BOX ---------------- */
.action-box {
    display:none;
    padding: 16px;
    margin-top: 12px;
    border-radius: 12px;
    border: 1px solid #d5dbe3;
    background: #f8fafc;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.06);
    animation: fadeIn 0.2s ease-out;
}

@keyframes fadeIn {
    from { opacity:0; transform:translateY(-4px); }
    to   { opacity:1; transform:translateY(0); }
}

.action-box button {
    width:100%;
    padding:12px 14px;
    margin:6px 0;
    border-radius:8px;
    background:white;
    border:1px solid #cbd5e1;
    font-weight:500;
    cursor:pointer;
    font-size:14px;
    transition:0.15s ease;
}
.action-box button:hover {
    background:#e2e8f0;
    border-color:#94a3b8;
}

/* ---------------- COPILOT BUTTON (KEEP YOUR POSITION) ---------------- */
.copilot-btn {
    position: fixed;
    bottom: 808px;   /* ✅ EXACTLY YOUR VALUE */
    right: 18px;     /* ✅ EXACTLY YOUR VALUE */
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: #0ea5e9;
    color:white;
    font-size:32px;
    display:flex;
    align-items:center;
    justify-content:center;
    cursor:pointer;
    box-shadow:0px 8px 22px rgba(0,0,0,0.22);
    transition:0.2s;
    z-index:900;
}

.copilot-btn:hover {
    background:#0284c7;
    transform:scale(1.07);
}

/* ---------------- COPILOT PANEL (KEEP YOUR POSITION) ---------------- */
#copilot-panel {
    display:none;
    position: fixed;
    top:22vh;        /* ✅ EXACTLY YOUR VALUE */
    right:135px;     /* ✅ EXACTLY YOUR VALUE */
    width:380px;
    height:460px;
    background:white;
    border-radius:16px;
    border:1px solid #e2e8f0;
    padding:22px;
    box-shadow:0px 14px 34px rgba(0,0,0,0.18);
    overflow-y:auto;
    animation: slideIn 0.25s ease-out;
    z-index:999;
}

@keyframes slideIn {
    from { opacity:0; transform:translateY(18px); }
    to   { opacity:1; transform:translateY(0); }
}

/* Close button */
.close-btn {
    position:absolute;
    top:12px;
    right:12px;
    width:28px;
    height:28px;
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
    <h3 style="margin-top:0;">OT Copilot</h3>
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

components.html(html, height=1400, scrolling=True)
