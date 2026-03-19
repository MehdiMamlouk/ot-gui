import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="OT GUI Launcher", layout="wide")

st.markdown("""
<h1 style="
    text-align:center;
    font-family:'Segoe UI', sans-serif;
    font-weight:700;
    margin-top:10px;
    margin-bottom:35px;
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
    background: #eef1f6;
    margin: 0;
}

/* ---------------- SECTION WRAPPER ---------------- */
.section {
    background:white;
    padding:30px;
    border-radius:18px;
    box-shadow:0 8px 24px rgba(0,0,0,0.08);
    margin-bottom:40px;
    border:1px solid #dce3ec;
}

/* Section Title */
.section-title {
    font-size:20px;
    font-weight:700;
    color:#1e293b;
    margin-bottom:20px;
    padding-bottom:8px;
    border-bottom:2px solid #e2e8f0;
}

/* ---------------- GRID ---------------- */
.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap:22px;
}

/* ---------------- PANEL ---------------- */
.panel {
    background:#f8fafc;
    border:1px solid #d4dbe5;
    padding:18px;
    border-radius:14px;
    box-shadow:0 4px 12px rgba(0,0,0,0.05);
    transition:0.2s;
    cursor:pointer;
}

.panel:hover {
    background:white;
    border-color:#b9c4d3;
    transform: translateY(-4px);
    box-shadow:0 8px 24px rgba(0,0,0,0.10);
}

/* Panel label */
.panel-title {
    font-weight:700;
    margin-bottom:12px;
    color:#1e293b;
}

/* ---------------- ACTION BOX ---------------- */
.action-box {
    display:none;
    margin-top:14px;
}

.action-btn {
    display:block;
    width:100%;
    text-align:left;
    padding:10px 14px;
    margin-bottom:8px;
    background:white;
    border-radius:10px;
    border:1px solid #cfd6e1;
    font-size:14px;
    font-weight:500;
    cursor:pointer;
    transition:0.18s;
}

.action-btn:hover {
    background:#e2e8f0;
    transform:translateX(4px);
}

/* ---------------- COPILOT BUTTON EXACT POSITION ---------------- */
.copilot-btn {
    position: fixed;
    bottom: 808px;   /* ✅ AVEC EXACTITUDE */
    right: 18px;     /* ✅ NE BOUGE PAS */
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
    box-shadow:0px 10px 28px rgba(0,0,0,0.25);
    transition:0.25s;
    z-index:900;
}

.copilot-btn:hover {
    background:#1d4ed8;
    transform:scale(1.08);
}

/* ---------------- COPILOT PANEL ---------------- */
#copilot-panel {
    display:none;
    position: fixed;
    top:22vh;
    right:135px;
    width:400px;
    height:500px;
    background:white;
    border-radius:20px;
    border:1px solid #dde3ed;
    padding:26px;
    box-shadow:0 18px 46px rgba(0,0,0,0.20);
    overflow-y:auto;
    z-index:999;
}

/* Close button */
.close-btn {
    position:absolute;
    top:12px;
    right:12px;
    width:30px;
    height:30px;
    border-radius:50%;
    background:#e2e8f0;
    display:flex;
    align-items:center;
    justify-content:center;
    cursor:pointer;
}
.close-btn:hover { background:#cbd5e1; }
</style>


<!-- ---------------- CONTENT ---------------- -->

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


<!-- ---------------- COPILOT BUTTON ---------------- -->
<div class="copilot-btn" onclick="toggleCopilot()">🤖</div>

<!-- ---------------- COPILOT PANEL ---------------- -->
<div id="copilot-panel">
    <div class="close-btn" onclick="toggleCopilot()">✕</div>
    <h3 style="margin-top:0;">OT Copilot</h3>
    <p style="opacity:0.65;">Pose une question…</p>
</div>

<script>
function toggle(id) {
    const box = document.getElementById(id);
    box.style.display = box.style.display === "block" ? "none" : "block";
}
function toggleCopilot() {
    const p = document.getElementById("copilot-panel");
    p.style.display = p.style.display === "block" ? "none" : "block";
}
</script>
"""

components.html(html, height=1800, scrolling=True)
