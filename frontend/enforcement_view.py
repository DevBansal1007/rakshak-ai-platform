"""Enforcement command-center view for the Rakshak AI dashboard.

This module renders a mock intelligence console for law-enforcement users,
including filters, KPI cards, a map placeholder, a graph placeholder, and an
intercept log table.
"""

import streamlit as st
import pandas as pd
import numpy as np

st.markdown("""
    <style>
    .stApp {
        background-color: #0B0F19;
        color: #E2E8F0;
        font-family: 'Inter', sans-serif;
    }
    .top-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #1E293B;
        padding-bottom: 15px;
        margin-bottom: 25px;
    }
    .kpi-container {
        background-color: #121826;
        border: 1px solid #1E293B;
        border-left: 4px solid #38BDF8;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    .kpi-title {
        color: #94A3B8;
        font-size: 0.85em;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
        margin-bottom: 5px;
    }
    .kpi-value {
        color: #FFFFFF;
        font-size: 2.2em;
        font-weight: 800;
        letter-spacing: -1px;
    }
    .kpi-trend-up {
        color: #EF4444;
        font-size: 0.9em;
        font-weight: 700;
        background: rgba(239, 68, 68, 0.1);
        padding: 2px 8px;
        border-radius: 12px;
    }
    .map-placeholder {
        background: radial-gradient(circle at center, #1E293B 0%, #0B0F19 100%);
        border: 1px solid #334155;
        border-radius: 16px;
        height: 450px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }
    .map-overlay-text {
        color: #38BDF8;
        font-size: 1.2em;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        z-index: 10;
    }
    .graph-placeholder {
        background: radial-gradient(circle at center, #1E293B 0%, #0B0F19 100%);
        border: 1px solid #334155;
        border-radius: 16px;
        height: 450px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .section-title {
        color: #FFFFFF;
        font-size: 1.1em;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .status-badge {
        background-color: rgba(239, 68, 68, 0.15);
        color: #EF4444;
        padding: 4px 12px;
        border-radius: 50px;
        font-size: 0.75em;
        font-weight: 800;
        border: 1px solid rgba(239, 68, 68, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# Define the jurisdiction hierarchy used by the sidebar controls.
jurisdiction_map = {
    "Rajasthan": ["Statewide Overview", "Jaipur", "Jodhpur", "Udaipur", "Kota", "Bikaner"],
    "Maharashtra": ["Statewide Overview", "Mumbai", "Pune", "Nagpur", "Thane", "Solapur"],
    "Delhi NCT": ["Statewide Overview", "New Delhi", "North Delhi", "South Delhi", "East Delhi"],
    "Karnataka": ["Statewide Overview", "Bengaluru", "Mysuru", "Mangaluru", "Hubballi"]
}

# Build the sidebar filters that allow the operator to narrow the view by region.
with st.sidebar:
    st.markdown("### 🛡️ RAKSHAK Command")
    st.markdown("---")
    
    selected_state = st.selectbox("Select State Jurisdiction", list(jurisdiction_map.keys()))
    selected_district = st.selectbox("Select District Level", jurisdiction_map[selected_state])
    
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
    
    st.selectbox("Time Intel Window", ["Live (Last 24H)", "Trailing 7 Days", "Trailing 30 Days"])
    st.multiselect("Threat Vector Filter", ["Digital Arrest", "UPI Phishing", "Job Fraud", "Investment Scam"], default=["Digital Arrest"])
    
    st.markdown("---")
    st.button("Export NCRP Master File", use_container_width=True)

# Format the selected jurisdiction for the dashboard header banner.
header_jurisdiction = f"{selected_state.upper()}" if selected_district == "Statewide Overview" else f"{selected_district.upper()}, {selected_state.upper()}"

# Render the primary header and status banner for the command center.
st.markdown(f"""
    <div class="top-nav">
        <div>
            <h2 style="margin: 0; color: #F8FAFC; font-weight: 800; letter-spacing: -1px;">Geospatial Intelligence Dashboard</h2>
            <span style="color: #64748B; font-size: 0.9em; font-weight: 600; letter-spacing: 0.5px;">GRID: {header_jurisdiction} | SYSTEM STATUS: SECURE</span>
        </div>
        <div>
            <span class="status-badge">● 14 CRITICAL ALERTS</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Show the core operational metrics as KPI tiles.
kpi_1, kpi_2, kpi_3, kpi_4 = st.columns(4)

with kpi_1:
    st.markdown("""
        <div class="kpi-container" style="border-left-color: #EF4444;">
            <div class="kpi-title">Active Threat Nodes</div>
            <div class="kpi-value">1,204</div>
            <div style="margin-top: 5px;"><span class="kpi-trend-up">↑ +12% today</span></div>
        </div>
    """, unsafe_allow_html=True)

with kpi_2:
    st.markdown("""
        <div class="kpi-container" style="border-left-color: #F59E0B;">
            <div class="kpi-title">Identified Syndicates</div>
            <div class="kpi-value">42</div>
            <div style="margin-top: 5px; color: #94A3B8; font-size: 0.85em;">Cross-district operations</div>
        </div>
    """, unsafe_allow_html=True)

with kpi_3:
    st.markdown("""
        <div class="kpi-container" style="border-left-color: #10B981;">
            <div class="kpi-title">Total Capital At Risk</div>
            <div class="kpi-value">₹8.4Cr</div>
            <div style="margin-top: 5px; color: #94A3B8; font-size: 0.85em;">Intercepted & Flagged</div>
        </div>
    """, unsafe_allow_html=True)

with kpi_4:
    st.markdown("""
        <div class="kpi-container" style="border-left-color: #8B5CF6;">
            <div class="kpi-title">NCRP Auto-Complaints</div>
            <div class="kpi-value">845</div>
            <div style="margin-top: 5px; color: #94A3B8; font-size: 0.85em;">Pending review queues</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)

# Display the geospatial and network visualisation panels side by side.
col_map, col_graph = st.columns([1.5, 1], gap="large")

with col_map:
    st.markdown('<div class="section-title">📍 Live Geospatial Heatmap</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="map-placeholder">
            <div class="map-overlay-text">[ FOLIUM HEATMAP MOUNT POINT ]</div>
            <p style="color: #64748B; font-size: 0.9em; margin-top: 10px;">Awaiting st_folium geospatial stream integration</p>
        </div>
    """, unsafe_allow_html=True)

with col_graph:
    st.markdown('<div class="section-title">🕸️ Entity Linkage Network</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="graph-placeholder">
            <div class="map-overlay-text" style="color: #A855F7;">[ NETWORKX GRAPH MOUNT POINT ]</div>
            <p style="color: #64748B; font-size: 0.9em; margin-top: 10px;">Awaiting pyvis/plotly relation graph</p>
        </div>
    """, unsafe_allow_html=True)

# Show the live intercept table beneath the visual panels.
st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
st.markdown('<div class="section-title">⚡ Live Intercept Log</div>', unsafe_allow_html=True)

# Build a mock incident dataset for the log table until live backend data is wired in.
mock_data = {
    "Timestamp": ["19:42:11", "19:38:04", "19:15:22", "18:50:41", "18:42:09"],
    "Threat Class": ["Digital Arrest", "UPI Fraud", "Digital Arrest", "Job Scam", "Investment Scam"],
    "Risk": ["98%", "85%", "96%", "72%", "88%"],
    "Target District": ["Jaipur", "Jodhpur", "Jaipur", "Udaipur", "Kota"],
    "Extracted Entities": ["+91-9876543210, 'ACP Sharma'", "UPI: scammer@ybl", "+91-9876543210, ₹2.4L", "t.me/joboffer2026", "Fake Trading App APK"],
    "NCRP Status": ["Ready for Dispatch", "Processing", "Dispatched", "Archived", "Ready for Dispatch"]
}
df = pd.DataFrame(mock_data)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Risk": st.column_config.ProgressColumn("Risk Score", help="Threat probability", format="%s", min_value=0, max_value=100)
    }
)