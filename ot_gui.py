import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="OT GUI Launcher", layout="wide")

st.markdown("<h1 style='text-align:center;'>OT GUI Launcher</h1>", unsafe_allow_html=True)

html_code = """
<style>

.container {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 22px;
    margin-top: 40px;
}

.card {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    cursor: pointer;
    font-weight: 600;
    border: 1px solid #ccc;
    background: white;
}

.card:hover {
    background: #f1f1f1;
}

.action-box {
    display: none;
    padding: 15px;
    margin-top: 10px;
    border-radius: 10px;
    border: 1px solid #ddd;
    background: #fafafa;
}

/* COPILOT BUTTON */
.copilot-btn {
    position: fixed;
    bottom: 28px;
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
    box-shadow: 0px 5px 14px rgba(0,0,0,0.25);
}

/* COPILOT PANEL */
#copilot-panel {
    display: none;
    position: fixed;
    bottom: 100px;
    right: 20px;
    width: 360px;
    height: 500px;
    background: white;
    border-radius: 12px;
    border: 1px solid #ccc;
    padding: 20px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.25);
    overflow-y: auto;
}

</style>

<h2 style='margin-top:40px;'>Sections</h2>

<div class="container">

    <div class="section">
        <div class="card" onclick="toggle('Opening')">Opening</div>
        <div id="Opening" class="action-box">
            <button>Open Project</button><br><br>
            <button>Open Folder</button><br><br>
            <button>Load PLC File</button>
        </div>
    </div>

    <div class="section">
        <div class="card" onclick="toggle('Versioning')">Versioning</div>
        <div id="Versioning" class="action-box">
            <button>Git Pull</button><br><br>
            <button>Git Diff</button><br><br>
            <button>Git Status</button>
        </div>
    </div>

    <div class="section">
        <div class="card" onclick="toggle('Backup')">Backup</div>
        <div id="Backup" class="action-box">
            <button>Backup Now</button><br><br>
            <button>Restore Backup</button><br><br>
            <button>Export Logs</button>
        </div>
    </div>

    <div class="section">
        <div class="card" onclick="toggle('Project')">Project Creation</div>
        <div id="Project" class="action-box">
            <button>New Project</button><br><br>
            <button>New Template</button><br><br>
            <button>Init Structure</button>
        </div>
    </div>

</div>

<br><br>

<div class="container" style="grid-template-columns: repeat(3, 1fr);">

    <div class="section">
        <div class="card" onclick="toggle('Compilation')">Compilation</div>
        <div id="Compilation" class="action-box">
            <button>Build Project</button><br><br>
            <button>View Logs</button><br><br>
            <button>Diagnostics</button>
        </div>
    </div>

    <div class="section">
        <div class="card" onclick="toggle('Simulation')">Simulation</div>
        <div id="Simulation" class="action-box">
            <button>Start Simulation</button><br><br>
            <button>Stop Simulation</button><br><br>
            <button>Simulation Logs</button>
        </div>
    </div>

    <div class="section">
        <div class="card" onclick="toggle('Export')">Export / Push</div>
        <div id="Export" class="action-box">
            <button>Export Package</button><br><br>
            <button>Push to Git</button><br><br>
            <button>Generate Report</button>
        </div>
    </div>

</div>

<!-- COPILOT BUTTON -->
<div class="copilot-btn" onclick="openCopilot()">🤖</div>

<!-- COPILOT PANEL -->
<div id="copilot-panel">
    <h3>OT Copilot</h3>
    <p style='opacity:0.6'>Pose ta question… (backend prochainement)</p>
</div>

<script>

function toggle(id) {
    var box = document.getElementById(id);
    box.style.display = (box.style.display === "block") ? "none" : "block";
}

function openCopilot() {
    var panel = document.getElementById("copilot-panel");
    panel.style.display = (panel.style.display === "block") ? "none" : "block";
}

</script>
"""

components.html(html_code, height=1400, scrolling=True)
