import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="OT GUI Launcher", layout="wide")

st.markdown("""
<h1 style="
    text-align:center;
    font-family:'IBM Plex Sans', sans-serif;
    font-weight:700;
    margin-top:20px;
    margin-bottom:35px;
    color:#0D1B2A;
">
OT GUI Launcher
</h1>
""", unsafe_allow_html=True)

html = """
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>

body {
    font-family:'IBM Plex Sans', sans-serif;
    background:#E0E1DD;
    margin:0;
}

/* -------- SECTION TITLE -------- */
.section {
    background:#1B263B;
    color:#E0E1DD;
    padding:30px;
    margin-bottom:40px;
    border-radius:18px;
    box-shadow:0 8px 24px rgba(0,0,0,0.25);
}

.section-title {
    font-size:22px;
    font-weight:700;
    margin-bottom:25px;
    border-left:5px solid #4CC9F0;
    padding-left:15px;
}

/* -------- GRID -------- */
.grid {
    display:grid;
    grid-template-columns:repeat(3, 1fr);
    gap:26px;
}

/* -------- PANELS -------- */
.panel {
    background:#415A77;
    border:1px solid #778DA9;
    padding:20px;
    border-radius:14px;
    color:#E0E1DD;
    box-shadow:0 6px 16px rgba(0,0,0,0.2);
    transition:0.25s ease;
    cursor:pointer;
}

.panel:hover {
    background:#4C6788;
    border-color:#AFC3D6;
    transform:translateY(-5px);
    box-shadow:0 12px 28px rgba(0,0,0,0.28);
}

/* Panel title */
.panel-title {
    font-size:17px;
    font-weight:700;
    margin-bottom:14px;
}

/* -------- ACTION BOX -------- */
.action-box {
    display:none;
    margin-top:12px;
}

.action-btn {
    width:100%;
    background:#E0E1DD;
    border:1px solid #B8C0CC;
    padding:10px 14px;
    border-radius:10px;
    margin-bottom:8px;
    text-align:left;
    font-weight:600;
    color:#1B263B;
    cursor:pointer;
    transition:0.20s;
}

.action-btn:hover {
    background:#4CC9F0;
    color:#0D1B2A;
    transform:translateX(6px);
}

/* -------- COPILOT BUTTON (POSITION STRICTE) -------- */
.copilot-btn {
    position: fixed;
    bottom: 808px;  /* ✅ NE PAS TOUCHER */
    right: 18px;    /* ✅ NE PAS TOUCHER */
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background:#4CC9F0;
    color:#0D1B2A;
    font-size:30px;
    display:flex;
    align-items:center;
    justify-content:center;
    cursor:pointer;
    box-shadow:0px 10px 28px rgba(0,0,0,0.35);
    transition:0.25s;
    z-index:900;
}

.copilot-btn:hover {
    transform:scale(1.10);
    background:#72D8FF;
}

/* -------- COPILOT PANEL -------- */
#copilot-panel {
    display:none;
    position:fixed;
    top:22vh;
    right:135px;
    width:400px;
    height:500px;
    background:#1B263B;
    border-radius:20px;
    border:1px solid #4CC9F0;
    padding:26px;
    color:#E0E1DD;
    box-shadow:0 18px 46px rgba(0,0,0,0.35);
    overflow-y:auto;
    z-index:999;
}

.close-btn {
    position:absolute;
    top:12px;
    right:12px;
    width:30px;
    height:30px;
    border-radius:50%;
    background:#778DA9;
    color:#0D1B2A;
    display:flex;
    align-items:center;
    justify-content:center;
    cursor:pointer;
    font-weight:700;
}
.close-btn:hover {
    background:#4CC9F0;
    color:#0D1B2A;
}

</style>

<!-- UI -->

<div class="section">
    <div class="section-title">Project Operations</div>

    <div class="grid">

        <div class="panel" onclick="toggle('open')">
            <div class="panel-title">Opening</div>
            <div id="open" class="action-box">
                <button class="action-btn">Open Project</button>
                <button class="action-btn">Open Folder</button>
                <button class="action-btn">Load PLC File</button>
            </div>
        </div>

        <div class="panel" onclick="toggle('version')">
            <div class="panel-title">Versioning</div>
            <div id="version" class="action-box">
                <button class="action-btn">Git Pull</button>
                <button class="action-btn">Git Diff</button>
                <button class="action-btn">Git Status</button>
            </div>
        </div>

        <div class="panel" onclick="toggle('backup')">
            <div class="panel-title">Backup</div>
            <div id="backup" class="action-box">
                <button class="action-btn">Backup Now</button>
                <button class="action-btn">Restore Backup</button>
                <button class="action-btn">Export Logs</button>
            </div>
        </div>

    </div>
</div>


<div class="section">
    <div class="section-title">Build & Deployment</div>

    <div class="grid">

        <div class="panel" onclick="toggle('comp')">
            <div class="panel-title">Compilation</div>
            <div id="comp" class="action-box">
                <button class="action-btn">Build Project</button>
                <button class="action-btn">View Logs</button>
                <button class="action-btn">Diagnostics</button>
            </div>
        </div>

        <div class="panel" onclick="toggle('sim')">
            <div class="panel-title">Simulation</div>
            <div id="sim" class="action-box">
                <button class="action-btn">Start Simulation</button>
                <button class="action-btn">Stop Simulation</button>
                <button class="action-btn">Simulation Logs</button>
            </div>
        </div>

        <div class="panel" onclick="toggle('export')">
            <div class="panel-title">Export / Push</div>
            <div id="export" class="action-box">
                <button class="action-btn">Export Package</button>
                <button class="action-btn">Push to Git</button>
                <button class="action-btn">Generate Report</button>
            </div>
        </div>

    </div>
</div>

<div class="copilot-btn" onclick="toggleCopilot()">🤖</div>

<div id="copilot-panel">
    <div class="close-btn" onclick="toggleCopilot()">✕</div>
    <h3>OT Copilot</h3>
    <p style="opacity:0.8;">Pose une question…</p>
</div>

<script>
function toggle(id) {
    const panel = document.getElementById(id);
    panel.style.display = panel.style.display === "block" ? "none" : "block";
}
function toggleCopilot() {
    const p = document.getElementById("copilot-panel");
    p.style.display = p.style.display === "block" ? "none" : "block";
}
</script>
"""

components.html(html, height=1800, scrolling=True)
