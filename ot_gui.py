import streamlit as st

st.set_page_config(layout="wide", page_title="OT Launcher Mockup")

st.title("🟦 OT GUI — Mockup Prototype")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Opening")
    st.button("Open Project")
    st.button("Open Folder")
    st.button("Load PLC File")

with col2:
    st.subheader("Versioning")
    st.button("Git Pull")
    st.button("Git Diff")
    st.button("Git Status")

with col3:
    st.subheader("Backup")
    st.button("Backup Now")
    st.button("Restore Backup")
    st.button("Export Logs")

with col4:
    st.subheader("Project Creation")
    st.button("New Project")
    st.button("New Template")
    st.button("Init Structure")

st.markdown("---")

col5, col6, col7 = st.columns(3)

with col5:
    st.subheader("Compilation")
    st.button("Build Project")
    st.button("View Logs")
    st.button("Diagnostics")

with col6:
    st.subheader("Simulation")
    st.button("Start Simulation")
    st.button("Stop Simulation")
    st.button("Simulation Logs")

with col7:
    st.subheader("Export / Push")
    st.button("Export Package")
    st.button("Push to Git")
    st.button("Generate Report")
