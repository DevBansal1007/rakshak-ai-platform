"""Main entry point for the Rakshak AI frontend gateway.

This module serves as the landing page for the application and routes users
between the citizen safety portal and the enforcement command center.
"""

import streamlit as st

from citizen_view import render_citizen_view

# Configure the page metadata for the enterprise gateway experience.
st.set_page_config(
    page_title="Rakshak AI - Enterprise Gateway",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize the active route in session state so navigation persists across reruns.
if 'active_route' not in st.session_state:
    st.session_state.active_route = 'gateway'

# Helper function used by the portal cards to switch views without reloading the app.
def set_route(route_name):
    st.session_state.active_route = route_name

# Render the landing gateway view when the user has not selected a portal yet.
if st.session_state.active_route == 'gateway':
    st.markdown("""
        <style>
        .stApp {
            background-color: #06090E;
            background-image: radial-gradient(circle at 50% 0%, #151F32 0%, #06090E 70%);
            font-family: 'Inter', sans-serif;
        }
        .gateway-wrapper {
            max-width: 1200px;
            margin: 0 auto;
            padding-top: 80px;
        }
        .hero-logo {
            display: block;
            margin: 0 auto 30px auto;
            width: 100px;
            height: 100px;
            background: linear-gradient(135deg, #FF3333 0%, #6C5DD3 100%);
            border-radius: 24px;
            box-shadow: 0 0 40px rgba(108, 93, 211, 0.4);
        }
        .hero-title {
            text-align: center;
            font-size: 4.5em;
            font-weight: 900;
            color: #FFFFFF;
            letter-spacing: -2px;
            margin-bottom: 10px;
        }
        .hero-subtitle {
            text-align: center;
            font-size: 1.3em;
            color: #94A3B8;
            font-weight: 400;
            margin-bottom: 80px;
            letter-spacing: 0.5px;
        }
        .portal-card {
            background-color: #0F141E;
            border: 1px solid #1E293B;
            border-radius: 24px;
            padding: 40px;
            height: 100%;
            transition: transform 0.3s ease, border-color 0.3s ease;
        }
        .portal-card:hover {
            transform: translateY(-5px);
        }
        .portal-icon {
            font-size: 3em;
            margin-bottom: 20px;
        }
        .portal-title {
            font-size: 1.8em;
            font-weight: 800;
            color: #F8FAFC;
            margin-bottom: 15px;
        }
        .portal-desc {
            color: #64748B;
            line-height: 1.6;
            margin-bottom: 30px;
            font-size: 1.05em;
        }
        .citizen-accent { border-top: 4px solid #FF523D; }
        .enforcement-accent { border-top: 4px solid #6C5DD3; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="gateway-wrapper">', unsafe_allow_html=True)
    st.markdown('<div class="hero-logo"></div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">RAKSHAK AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Agentic Fraud Intelligence Platform for Digital Public Safety</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 8, 1])

    with col2:
        card_col1, card_col2 = st.columns(2, gap="large")
        
        with card_col1:
            st.markdown("""
                <div class="portal-card citizen-accent">
                    <div class="portal-icon">🛡️</div>
                    <div class="portal-title">Citizen Safety Portal</div>
                    <div class="portal-desc">
                        Access the public threat scanner. Upload suspicious messages, 
                        documents, or audio to receive instant risk analysis and 
                        automatically generate official NCRP complaint drafts.
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("ENTER CITIZEN PORTAL →", use_container_width=True, type="primary"):
                set_route('citizen')
                st.rerun()

        with card_col2:
            st.markdown("""
                <div class="portal-card enforcement-accent">
                    <div class="portal-icon">⚡</div>
                    <div class="portal-title">Command Center</div>
                    <div class="portal-desc">
                        Secure access for authorized law enforcement personnel. 
                        Monitor live geospatial threat heatmaps, track organized 
                        syndicate networks, and manage regional intelligence data.
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("AUTHORIZE ENFORCEMENT LOGIN →", use_container_width=True ):
                set_route('enforcement')
                st.rerun()
                
    st.markdown('</div>', unsafe_allow_html=True)

# Load the citizen-facing threat analysis experience when requested.
elif st.session_state.active_route == 'citizen':
    render_citizen_view()

# Load the enforcement command-center experience when requested.
elif st.session_state.active_route == 'enforcement':
    import enforcement_view