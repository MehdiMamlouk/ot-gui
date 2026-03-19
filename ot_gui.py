html = """
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>

body {
    font-family: 'Inter', sans-serif;
    background: #f4f6f9;  /* ✅ fond plus pro */
    color: #1e293b;
}

/* ============================
   ✅ GRID TOP/BOTTOM
============================ */
.container, .container-2 {
    display: grid;
    gap: 26px;
    margin-top: 20px;
}
.container { grid-template-columns: repeat(4, 1fr); }
.container-2 { grid-template-columns: repeat(3, 1fr); }

/* ============================
   ✅ CARDS (Figma-style)
============================ */
.card {
    padding: 20px;
    border-radius: 14px;
    cursor: pointer;
    font-weight: 600;
    background: #ffffff;
    color: #0f172a;
    border: 1px solid #e2e8f0;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.04);
    text-align: center;
    transition: all 0.18s ease;
}

.card:hover {
    background: #eef2f7;
    border-color: #cbd5e1;
    transform: translateY(-2px);
}

/* ============================
   ✅ ACTION BOX (clean, modern)
============================ */
.action-box {
    display: none;
    padding: 16px;
    margin-top: 12px;
    border-radius: 12px;
    background: #f8fafc;
    border: 1px solid #dbe1e8;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
    animation: fadeIn 0.2s ease-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-4px); }
    to   { opacity: 1; transform: translateY(0px); }
}

/* ✅ BUTTONS */
.action-box button {
    width: 100%;
    padding: 12px 14px;
    margin: 6px 0;
    border-radius: 8px;
    border: 1px solid #cbd5e1;
    background: #ffffff;
    font-weight: 500;
    color: #0f172a;
    cursor: pointer;
    transition: 0.15s;
}

.action-box button:hover {
    background: #e2e8f0;
    border-color: #94a3b8;
}

/* ============================
   ✅ COPILOT BUTTON (keep position)
============================ */
.copilot-btn {
    position: fixed;
    bottom: 808px;    /* ✅ tu as choisi cette valeur, je la garde */
    right: 18px;
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: #0ea5e9;
    color: white;
    font-size: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0px 8px 22px rgba(0,0,0,0.22);
    transition: 0.2s;
    z-index: 900;
}

.copilot-btn:hover {
    background: #0284c7;
    transform: scale(1.08);
}

/* ============================
   ✅ COPILOT PANEL (clean card)
============================ */
#copilot-panel {
    display: none;
    position: fixed;
    top: 22vh;        /* ✅ tu l’as choisi, je garde */
    right: 135px;     /* ✅ ton positionnement */
    width: 380px;
    height: 460px;
    background: #ffffff;
    border-radius: 16px;
    border: 1px solid #e2e8f0;
    box-shadow: 0px 15px 35px rgba(0,0,0,0.18);
    padding: 22px;
    overflow-y: auto;
    animation: slideIn 0.25s ease-out;
    z-index: 999;
}

@keyframes slideIn {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: translateY(0px); }
}

/* Close button */
.close-btn {
    position:absolute;
    top:12px;
    right:12px;
    background:#e2e8f0;
    width:28px;
    height:28px;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    cursor:pointer;
    transition:0.15s;
}
.close-btn:hover { background:#cbd5e1; }

</style>

"""

components.html(html + """
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
""", height=1400, scrolling=True)
