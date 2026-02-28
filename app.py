import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime
import time
import random

# ===============================
# PAGE CONFIG & TERMINAL CSS
# ===============================
st.set_page_config(page_title="NOVA RESOURCES: ORION INTERFACE", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'JetBrains Mono', monospace; background-color: #000000; }
    .stMetric { background: rgba(0, 255, 0, 0.05); border: 1px solid #00FF00; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ===============================
# HEADER & CLOCK
# ===============================
target_date = datetime(2026, 4, 14, 16, 15)
time_left = target_date - datetime.now()
st.markdown(f"# 🎧 NOVA RESOURCES: ORION INTERFACE")
st.markdown(f"### 🌌 CEO: Daniel | T-MINUS: **{time_left.days}D {time_left.seconds//3600}H** | STATUS: **LOCKED**")

# ===============================
# TELEMETRY DASH
# ===============================
col1, col2, col3 = st.columns(3)
col1.metric("Distance to 2013 GM3", f"{29853521 + random.randint(-10,10):,}")
col2.metric("Relative Velocity", "7.41 km/s")
col3.metric("Bounty Valuation", "$1.2 Billion")

# ===============================
# 3D TACTICAL MAP (STARS + PLANETS + TARGETS)
# ===============================
fig = go.Figure()

# 1. GENERATE STARFIELD (Static Background)
np.random.seed(1)
stars_x, stars_y, stars_z = np.random.uniform(-25, 25, 600), np.random.uniform(-25, 25, 600), np.random.uniform(-25, 25, 600)
fig.add_trace(go.Scatter3d(x=stars_x, y=stars_y, z=stars_z, mode='markers',
                         marker=dict(size=1.2, color='white', opacity=0.4), name="Starfield", hoverinfo='skip'))

# 2. THE NINE PLANETS (Restored & Named)
planets = [
    {"n": "SUN", "x": -10, "y": 0, "s": 50, "c": "yellow"},
    {"n": "Mercury", "x": -7, "y": 2, "s": 6, "c": "gray"},
    {"n": "Venus", "x": -4, "y": -3, "s": 10, "c": "orange"},
    {"n": "Moon", "x": 0.5, "y": 0.5, "s": 4, "c": "white"},
    {"n": "Mars", "x": 3, "y": 4, "s": 8, "c": "red"},
    {"n": "Jupiter", "x": 7, "y": -5, "s": 25, "c": "peru"},
    {"n": "Saturn", "x": 11, "y": 6, "s": 20, "c": "khaki"},
    {"n": "Uranus", "x": 15, "y": -4, "s": 14, "c": "lightblue"},
    {"n": "Neptune", "x": 19, "y": 3, "s": 14, "c": "royalblue"},
    {"n": "Pluto", "x": 23, "y": -5, "s": 5, "c": "darkgray"}
]

for p in planets:
    fig.add_trace(go.Scatter3d(x=[p['x']], y=[p['y']], z=[0], mode='markers+text',
                             marker=dict(size=p['s'], color=p['c'], opacity=0.8),
                             text=[p['n']], name=p['n']))

# 3. EARTH (The Tecca Globe)
fig.add_trace(go.Scatter3d(x=[0], y=[0], z=[0], mode='markers+text', 
                         marker=dict(size=30, color='#0077BE', line=dict(color='cyan', width=2)), 
                         text=["TECCA GLOBE 🌍"], name="Earth"))

# 4. TARGETS (RESTORING MISSING DATA)
targets = [
    {"n": "2013 GM3 (PRIORITY)", "x": 1.5, "y": -2, "z": 1, "c": "#00FF00", "v": 1.2},
    {"n": "2007 DB61", "x": 5, "y": 8, "z": -2, "c": "#FFD700", "v": 4.8},
    {"n": "2025 YU15", "x": -2, "y": -6, "z": 3, "c": "#FFD700", "v": 12.5}
]

for t in targets:
    fig.add_trace(go.Scatter3d(x=[t['x']], y=[t['y']], z=[t['z']], mode='markers+text',
                             marker=dict(size=12, color=t['c'], symbol='diamond'),
                             text=[f"{t['n']}<br>${t['v']}B"], name="Target"))

fig.update_layout(scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False, bgcolor="black"),
                  paper_bgcolor="black", margin=dict(l=0, r=0, t=0, b=0))

st.plotly_chart(fig, use_container_width=True)

# ===============================
# SIDEBAR: DEEP SPACE SCANNER
# ===============================
st.sidebar.title("💰 LOOT LEDGER")

# SOUNDTRACK
st.sidebar.markdown("### 🎵 Station Atmosphere")
try:
    audio_file = open('soundtrack.mp3', 'rb')
    st.sidebar.audio(audio_file.read(), format='audio/mp3')
except:
    st.sidebar.warning("⚠️ soundtrack.mp3 Missing")

st.sidebar.markdown("---")

# DEEP SPACE SCANNER INTERFACE
st.sidebar.markdown("### 🛰️ DEEP SPACE SCANNER")
if st.sidebar.button("INITIATE MULTI-SPECTRAL PING"):
    progress_text = "Targeting 2013 GM3..."
    my_bar = st.sidebar.progress(0, text=progress_text)
    
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    
    st.sidebar.success("✅ SCAN SUCCESSFUL")
    st.sidebar.markdown("""
    **METALLIC SIGNATURES:**
    * 💎 **Iridium:** 18% (Extremely Rare)
    * 🟡 **Gold:** 4.2%
    * ⚪ **Platinum:** 11.5%
    * ⚙️ **Iron/Nickel:** 62%
    
    **OBJECT TYPE:** NATURAL ASTEROID (NON-PROBE)
    """)

st.sidebar.markdown("---")
st.sidebar.error(f"🚨 ALERT: 2013 GM3 @ 8,620km Perigee")