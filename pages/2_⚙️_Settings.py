import streamlit as st
from datetime import datetime
import json

st.set_page_config(page_title="Settings", page_icon="⚙️", layout="wide")

st.title("⚙️ Settings & Configuration")
st.write("Customize your application settings and preferences.")

# Create tabs for different setting categories
tab1, tab2, tab3 = st.tabs(["🎨 Appearance", "👤 User Profile", "🔔 Notifications"])

with tab1:
    st.header("Appearance Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Theme")
        theme = st.radio(
            "Select Theme:",
            ["Light", "Dark", "Auto"],
            help="Choose your preferred theme"
        )
        
        st.subheader("Language")
        language = st.selectbox(
            "Select Language:",
            ["English", "Spanish", "French", "German", "Chinese"]
        )
        
        st.subheader("Font Size")
        font_size = st.select_slider(
            "Choose Font Size:",
            options=["Small", "Medium", "Large", "Extra Large"],
            value="Medium"
        )
    
    with col2:
        st.subheader("Color Scheme")
        primary_color = st.color_picker("Primary Color", "#FF4B4B")
        secondary_color = st.color_picker("Secondary Color", "#0068C9")
        
        st.subheader("Layout")
        layout_option = st.radio(
            "Layout Preference:",
            ["Wide", "Centered", "Fluid"]
        )
        
        sidebar_state = st.checkbox("Auto-expand Sidebar", value=True)
    
    st.divider()
    
    # Preview section
    st.subheader("Preview")
    with st.container():
        st.markdown(f"""
        <div style="background-color: {primary_color}; padding: 20px; border-radius: 10px; color: white;">
            <h3>Theme Preview</h3>
            <p>This is how your theme will look with the selected colors.</p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.header("User Profile Settings")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Personal Information")
        
        full_name = st.text_input("Full Name:", placeholder="John Doe")
        email = st.text_input("Email:", placeholder="john.doe@example.com")
        
        col_a, col_b = st.columns(2)
        with col_a:
            phone = st.text_input("Phone:", placeholder="+1 (555) 123-4567")
        with col_b:
            country = st.selectbox("Country:", ["USA", "UK", "Canada", "Australia", "Other"])
        
        bio = st.text_area(
            "Bio:",
            placeholder="Tell us about yourself...",
            height=100
        )
        
        st.subheader("Professional Information")
        
        col_a, col_b = st.columns(2)
        with col_a:
            job_title = st.text_input("Job Title:", placeholder="Software Engineer")
        with col_b:
            company = st.text_input("Company:", placeholder="Tech Corp")
        
        skills = st.multiselect(
            "Skills:",
            ["Python", "JavaScript", "Java", "C++", "SQL", "React", "Node.js", "Django", "Flask"],
            default=["Python"]
        )
    
    with col2:
        st.subheader("Profile Picture")
        st.write("Upload a profile picture")
        uploaded_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])
        
        if uploaded_file is not None:
            st.image(uploaded_file, caption="Profile Picture", width=200)
        else:
            st.info("No image uploaded")
        
        st.subheader("Quick Stats")
        st.metric("Days Active", "42")
        st.metric("Projects", "7")
        st.metric("Tasks Completed", "156")
    
    st.divider()
    
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("💾 Save Profile", type="primary", use_container_width=True):
            st.success("✅ Profile saved successfully!")
    with col2:
        if st.button("🔄 Reset", use_container_width=True):
            st.warning("⚠️ Profile reset to defaults")

with tab3:
    st.header("Notification Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Email Notifications")
        
        email_notifications = st.checkbox("Enable Email Notifications", value=True)
        
        if email_notifications:
            st.write("**Notification Types:**")
            notify_updates = st.checkbox("Product Updates", value=True)
            notify_messages = st.checkbox("New Messages", value=True)
            notify_comments = st.checkbox("Comments & Mentions", value=True)
            notify_reports = st.checkbox("Weekly Reports", value=False)
        
        st.subheader("Email Frequency")
        email_freq = st.radio(
            "How often would you like to receive emails?",
            ["Immediately", "Daily Digest", "Weekly Digest", "Never"]
        )
    
    with col2:
        st.subheader("Push Notifications")
        
        push_notifications = st.checkbox("Enable Push Notifications", value=True)
        
        if push_notifications:
            st.write("**Push Notification Types:**")
            push_messages = st.checkbox("New Messages (Push)", value=True)
            push_alerts = st.checkbox("Important Alerts", value=True)
            push_reminders = st.checkbox("Reminders", value=True)
        
        st.subheader("Notification Sound")
        notification_sound = st.selectbox(
            "Choose Notification Sound:",
            ["Default", "Chime", "Bell", "Ping", "None"]
        )
    
    st.divider()
    
    st.subheader("Quiet Hours")
    st.write("Set hours when you don't want to receive notifications")
    
    col1, col2 = st.columns(2)
    with col1:
        quiet_start = st.time_input("Start Time:", value=None)
    with col2:
        quiet_end = st.time_input("End Time:", value=None)
    
    quiet_days = st.multiselect(
        "Quiet Days:",
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        default=["Saturday", "Sunday"]
    )
    
    st.divider()
    
    if st.button("💾 Save Notification Settings", type="primary"):
        st.success("✅ Notification settings saved!")

# Settings summary
st.divider()
st.header("📋 Settings Summary")

with st.expander("View Current Settings"):
    settings = {
        "Appearance": {
            "Theme": theme if 'theme' in locals() else "Light",
            "Language": language if 'language' in locals() else "English",
            "Font Size": font_size if 'font_size' in locals() else "Medium",
            "Primary Color": primary_color if 'primary_color' in locals() else "#FF4B4B"
        },
        "Notifications": {
            "Email Notifications": email_notifications if 'email_notifications' in locals() else True,
            "Push Notifications": push_notifications if 'push_notifications' in locals() else True,
            "Email Frequency": email_freq if 'email_freq' in locals() else "Immediately"
        },
        "Last Updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    st.json(settings)

# Export/Import settings
st.subheader("Backup & Restore")

col1, col2 = st.columns(2)

with col1:
    st.write("**Export Settings**")
    settings_json = json.dumps(settings, indent=2)
    st.download_button(
        label="📥 Download Settings",
        data=settings_json,
        file_name="app_settings.json",
        mime="application/json"
    )

with col2:
    st.write("**Import Settings**")
    uploaded_settings = st.file_uploader("Upload Settings File", type=['json'])
    if uploaded_settings is not None:
        try:
            imported_settings = json.load(uploaded_settings)
            st.success("✅ Settings imported successfully!")
            with st.expander("Preview Imported Settings"):
                st.json(imported_settings)
        except Exception as e:
            st.error(f"❌ Error importing settings: {e}")
