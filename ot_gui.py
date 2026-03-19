import streamlit as st

st.set_page_config(page_title="OT GUI", layout="wide")

st.title("🟦 OT GUI — Professional Prototype")

st.markdown(
    """
    ### 💠 Sélectionne une étape ci‑dessous  
    Les actions apparaîtront **uniquement après le clic**, pour une UI plus propre.
    """
)

# --- STYLE (pour l'aspect plus pro) ---
st.markdown("""
<style>
.step-button {
    background-color: #1f2937;
    color: white;
    padding: 12px 20px;
    border-radius: 8px;
    width: 100%;
    text-align: left;
    font-size: 18px;
    border: none;
    margin-bottom: 10px;
}
.action-button {
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# --- FONCTION POUR CRÉER UNE SECTION À CLiQUER ---
def step(title, actions):
    with st.expander(f"▶ {title}", expanded=False):
        cols = st.columns(3)
        i = 0
        for action in actions:
            with cols[i % 3]:
                st.button(action, key=f"{title}_{action}", help=f"Run: {action}")
            i += 1

# --- SECTIONS (ta pipeline OT) ---
step("Opening", [
    "Open Project", "Open Folder", "Load PLC File"
])

step("Versioning", [
    "Git Pull", "Git Diff", "Git Status"
])

step("Backup", [
    "Backup Now", "Restore Backup", "Export Logs"
])

step("Project Creation", [
    "New Project", "New Template", "Init Structure"
])

step("Compilation", [
    "Build Project", "View Logs", "Diagnostics"
])

step("Simulation", [
    "Start Simulation", "Stop Simulation", "Simulation Logs"
])

step("Export / Push", [
    "Export Package", "Push to Git", "Generate Report"
])

