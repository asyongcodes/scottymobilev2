from datetime import datetime
import time
import pytz
import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="SCOTTY", 
    page_icon="🤖",
    layout="centered"
)

# --- SIDEBAR CONTROL PANEL & LIVE CLOCK ---
with st.sidebar:
    st.markdown("### ⏱️ System Time (PHT)")
    clock_placeholder = st.empty()
    st.divider()
    
    st.markdown("### 🟢 System Status")
    st.success("SCOTTY v2.0 Online")

# --- MAIN INTERFACE HEADER ---
st.title("SCOTTY")
st.markdown("#### **Virtual Assistance Program**")
st.caption("Developed by TSTOC")
st.divider()

# --- INITIALIZE SESSION STATE ---
if "menu" not in st.session_state:
    st.session_state.menu = "main"

# --- APPLICATION ROUTING LOGIC ---

# 1. MAIN MENU
if st.session_state.menu == "main":
    st.markdown("##### **Select a service category:**")
    
    # Grid layout for professional service cards
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🖥️ 1. Technical Assistance", use_container_width=True):
            st.session_state.menu = "assistance"
            st.rerun()
        if st.button("📼 2. Dubout Operations", use_container_width=True):
            st.session_state.menu = "dubout"
            st.rerun()
            
    with col2:
        if st.button("🎬 3. Cinema Room Support", use_container_width=True):
            st.session_state.menu = "cinema"
            st.rerun()
        if st.button("❓ 4. Other Concerns", use_container_width=True):
            st.session_state.menu = "other"
            st.rerun()

# 2. TECHNICAL ASSISTANCE MENU
elif st.session_state.menu == "assistance":
    st.markdown("### 🖥️ Technical Assistance Diagnostics")
    st.write("Select the issue you are currently experiencing:")
    
    if st.button("Computer not responding", use_container_width=True):
        st.info("📞 **Action Required:** Call **Local 2630** for an immediate system restart and profile re-login.")
        
    if st.button("No audio or video output", use_container_width=True):
        st.info("📞 **Action Required:** Call **Local 2630** for system configuration and driver checks.")
        
    if st.button("No hardware power", use_container_width=True):
        st.info("📞 **Action Required:** Call **Local 2630** for an on-site hardware and power supply inspection.")
        
    st.divider()
    if st.button("⬅️ Return to Main Menu", use_container_width=True):
        st.session_state.menu = "main"
        st.rerun()

# 3. DUBOUT OPERATIONS MENU
elif st.session_state.menu == "dubout":
    st.markdown("### 📼 Dubout Operations Portal")
    
    # Standardized input container
    with st.container(border=True):
        st.markdown("**For PATCHING**")
        dnb = st.text_input("Enter Deck and Bay Designation:")
        if dnb:
            st.success(f"📱 **SMS Pipeline Ready:** Please forward the message **'{dnb}'** to **09154417194**")
            
    st.write("Troubleshooting Steps:")
    if st.button("No communications / Unclickable Record button", use_container_width=True):
        st.info("👉 **Resolution:** Reselect **Blackmagic** as your primary device control. If connection fails, dial **Local 2630** for on-site IO device powercycling.")
        
    if st.button("Dropped frames detected", use_container_width=True):
        st.info("👉 **Resolution:** Gracefully relaunch **Adobe Premiere**. If problem persist, dial **Local 2630**.")
        
    st.divider()
    if st.button("⬅️ Return to Main Menu", use_container_width=True):
        st.session_state.menu = "main"
        st.rerun()

# 4. CINEMA ROOM SUPPORT MENU
elif st.session_state.menu == "cinema":
    st.markdown("### 🎬 Cinema Room Support")
    st.write("Select the service required for your session:")
    
    if st.button("Request Media Preview Setup", use_container_width=True):
        st.info("📞 **Action Required:** Contact **Local 2630** for specialized projector, audio and video array preparation.")
        
    if st.button("Request Meeting Set Up", use_container_width=True):
        st.info("📞 **Action Required:** Contact **Local 2630** for facility arrangement (tables and chairs).")
        
    st.divider()
    if st.button("⬅️ Return to Main Menu", use_container_width=True):
        st.session_state.menu = "main"
        st.rerun()

# 5. OTHER CONCERNS MENU
elif st.session_state.menu == "other":
    st.markdown("### ❓ Escalate Concerns")
    st.warning("📍 **In-Person Assistance:** Please visit the **4th Floor TOC** for hands-on support from the TSTOC team.")
    
    st.divider()
    if st.button("⬅️ Return to Main Menu", use_container_width=True):
        st.session_state.menu = "main"
        st.rerun()

# --- ISOLATED, SMOOTH LIVE CLOCK LOOP ---
# This updates ONLY the clock element every second without triggering global loading spinners
@st.fragment(run_every=1.0)
def update_clock():
    ph_tz = pytz.timezone('Asia/Manila')
    date_str = datetime.now(ph_tz).strftime("%A, %B %d, %Y")
    time_str = datetime.now(ph_tz).strftime("%I:%M:%S %p")
    clock_placeholder.markdown(f"**{date_str}**\n\n**{time_str}**")

# Start the quiet isolated clock loop
update_clock()
