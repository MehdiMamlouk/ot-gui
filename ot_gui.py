import streamlit as st

st.set_page_config(page_title="OT GUI", layout="wide")

st.title("OT GUI")

# ---------- STYLES ----------
st.markdown("""
<style>
.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
    border: 1px solid #2c3e50;
}
.card-title {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)


# ---------- REUSABLE BLOCK ----------
def card_section(title, actions):
    with st.container():
        st.markdown(f'<div class="card"><div class="card-title">{title}</div>', unsafe_allow_html=True)

        with st.expander("Afficher les actions", expanded=False):
            cols = st.columns(3)
            for i, action in enumerate(actions):
                cols[i % 3].button(action)

        st.markdown("</div>", unsafe_allow_html=True)


# ---------- SECTIONS ----------
card_section("Opening", ["Open Project", "Open Folder", "Load PLC File"])

card_section("Versioning", ["Git Pull", "Git Diff", "Git Status"])

card_section("Backup", ["Backup Now", "Restore Backup", "Export Logs"])

card_section("Project Creation", ["New Project", "New Template", "Init Structure"])

card_section("Compilation", ["Build Project", "View Logs", "Diagnostics"])

card_section("Simulation", ["Start Simulation", "Stop Simulation", "Simulation Logs"])

card_section("Export / Push", ["Export Package", "Push to Git", "Generate Report"])


# ============================
# COPILOT SECTION (Chat UI)
# ============================

st.markdown("---")
st.subheader("🤖 OT Copilot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Input
user_input = st.chat_input("Pose une question sur l’OT, Git, PLC, DevOps...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Réponse simple (mock)
    response = f"Tu as demandé : **{user_input}**\n\n➡️ Cette feature viendra avec ton futur backend 🙂"
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)
``
