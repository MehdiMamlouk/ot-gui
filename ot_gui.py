import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="OT Management System", layout="wide")

st.markdown("""
<h1 style="
    text-align:center;
    font-family:'Inter','Segoe UI Variable',sans-serif;
    font-weight:700;
    margin-top:10px;
    margin-bottom:40px;
    color:#1e293b;
">
OT Management System
</h1>
""", unsafe_allow_html=True)

html = """
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>
body {
    font-family: 'Inter','Segoe UI Variable', sans-serif;
    background: #f3f6fa;
    color: #1e293b;
    margin: 0;
}

/* --- GRID --- */
.container, .container-2 {
    display: grid;
    gap: 26px;
}
.container  { grid-template-columns: repeat(4, 1fr); margin-top: 25px; }
.container-2 { grid-template-columns: repeat(3, 1fr); margin-top: 40px; }

/* --- CARD STYLE --- */
.card {
    padding: 20px;
    border-radius: 16px;
    background: rgba(255,255,255,0.72);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(180, 188, 202, 0.45);
    color: #1e293b;
    font-weight: 600;
    text-align:center;
    cursor:pointer;
    transition: all 0.18s ease;
    box-shadow: 0 4px 16px rgba(0,0,0,0.06);
}
.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 14px 28px rgba(0,0,0,0.10);
    background: rgba(255,255,255,0.90);
    border-color: #d2dae6;
}

/* --- ACTION BOX --- */
.action-box {
    display:none;
    padding: 18px;
    margin-top: 12px;
    border-radius: 14px;
    border: 1px solid #d6dce5;
    background: #ffffff;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.08);
    animation: fadeIn 0.25s ease-out;
}
@keyframes fadeIn {
    from { opacity:0; transform:translateY(-6px); }
    to   { opacity:1; transform:translateY(0); }
}

/* Buttons inside action panel */
.action-box button {
    width:100%;
    padding:12px 14px;
    margin:6px 0;
    border-radius:10px;
    background:white;
    border:1px solid #cbd5e1;
    font-weight:500;
    cursor:pointer;
    font-size:14px;
    transition:0.15s ease;
    text-align:left;
}
.action-box button:hover {
    background:#e2e8f0;
    transform: translateX(4px);
}

/* ✅ COPILOT BUTTON — SAME POSITION */
.copilot-btn {
    position: fixed;
    bottom: 808px;
    right: 18px;
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: #2563eb;
    color:white;
    font-size:32px;
    display:flex;
    align-items:center;
    justify-content:center;
    cursor:pointer;
    box-shadow:0px 8px 22px rgba(0,0,0,0.28);
    transition:0.2s;
    z-index:900;
}
.copilot-btn:hover {
    background:#1d4ed8;
    transform:scale(1.07);
}

/* ✅ COPILOT PANEL */
#copilot-panel {
    display:none;
    position: fixed;
    top:22vh;
    right:135px;
    width:380px;
    height:460px;
    background:white;
    border-radius:18px;
    border:1px solid #e2e8f0;
    padding:26px;
    box-shadow:0px 18px 46px rgba(0,0,0,0.20);
    overflow-y:auto;
    animation: slideIn 0.25s ease-out;
    z-index:999;
}

@keyframes slideIn {
    from { opacity:0; transform:translateY(20px); }
    to   { opacity:1; transform:translateY(0); }
}

.close-btn {
    position:absolute;
    top:12px;
    right:12px;
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


<!-- ✅ TOP GRID (4 SECTIONS) -->
<div class="container">

    <!-- ✅ TOOLS -->
    <div>
        <div class="card" onclick="toggle('Tools')">Tools</div>
        <div id="Tools" class="action-box">
            <button>Launch TIA Portal</button>
            <button>Launch SIMIT</button>
            <button>Launch PLCSIM Advanced</button>
        </div>
    </div>

    <!-- ✅ OPENING PROJECT -->
    <div>
        <div class="card" onclick="toggle('Opening')">Opening Project</div>
        <div id="Opening" class="action-box">
            <button>Open TIA Portal Project</button>
            <button>Open SIMIT Project</button>
        </div>
    </div>

    <!-- ✅ VERSIONING -->
    <div>
        <div class="card" onclick="toggle('Versioning')">Versioning</div>
        <div id="Versioning" class="action-box">
            <button>Export Project</button>
            <button>Push to Source Code Manager</button>
            <button>Compare Versions</button>
        </div>
    </div>

    <!-- ✅ PROJECT CREATION -->
    <div>
        <div class="card" onclick="toggle('ProjectCreation')">Project Creation</div>
        <div id="ProjectCreation" class="action-box">
            <button>Type Project Name</button>
            <button>Type Device Name</button>
            <button>Select Product Family</button>
            <button>Select CPU</button>
            <button>Select Order Number</button>
            <button>Select Version</button>
        </div>
    </div>

</div>


<!-- ✅ SECOND GRID (3 SECTIONS) -->
<div class="container-2">

    <!-- ✅ BACKUP / RESTORE -->
    <div>
        <div class="card" onclick="toggle('Backup')">Backup / Restore</div>
        <div id="Backup" class="action-box">
            <button>Backup TIA Portal Project</button>
            <button>Restore TIA Portal Project</button>
        </div>
    </div>

    <!-- ✅ COMPILATION -->
    <div>
        <div class="card" onclick="toggle('Compilation')">Compilation</div>
        <div id="Compilation" class="action-box">
            <button>Select Project</button>
            <button>Compile</button>
            <button>Logs</button>
            <button>Diagnostics Report</button>
        </div>
    </div>

    <!-- ✅ SIMULATION -->
    <div>
        <div class="card" onclick="toggle('Simulation')">Simulation</div>
        <div id="Simulation" class="action-box">
            <button>Select TIA Portal Project</button>
            <button>Select SIMIT Project</button>
            <button>Setup Simulation for Virtual Commissioning</button>
        </div>
    </div>

</div>


<!-- ✅ COPILOT BUTTON -->
<div class="copilot-btn" onclick="toggleCopilot()">🤖</div>

<!-- ✅ COPILOT PANEL -->
<div id="copilot-panel">
    <div class="close-btn" onclick="toggleCopilot()">✕</div>
    <h3 style="margin-top:0;">OT Copilot</h3>
    <p style="opacity:0.60;font-size:14px;">Pose une question…</p>
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

components.html(html, height=1700, scrolling=True)
