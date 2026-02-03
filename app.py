import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Python Streamlit Starter",
    page_icon="🚀",
    layout="wide"
)

# Main header
st.title("🚀 Python Streamlit Starter")
st.write("A simple starter template for building web applications with Streamlit.")

# Sidebar
with st.sidebar:
    st.header("Settings")
    user_name = st.text_input("Enter your name:", "Developer")
    st.divider()
    st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Welcome message
st.header(f"Hello, {user_name}! 👋")
st.write("Welcome to your Streamlit app. This is a simple starting point for your project.")

# Simple demo sections
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Text Input")
    text_input = st.text_input("Enter some text:")
    if text_input:
        st.write(f"You entered: **{text_input}**")
    
    st.subheader("🔢 Number Input")
    number = st.number_input("Pick a number:", min_value=0, max_value=100, value=42)
    st.write(f"Your number: **{number}**")

with col2:
    st.subheader("🎚️ Slider")
    slider_value = st.slider("Select a value:", 0, 100, 50)
    st.write(f"Selected value: **{slider_value}**")
    
    st.subheader("✅ Checkbox")
    checkbox = st.checkbox("Check me!")
    if checkbox:
        st.success("Checkbox is checked! ✓")

st.divider()

# Button demo
st.subheader("🔘 Button Example")
if st.button("Click me!"):
    st.balloons()
    st.success("Button clicked! 🎉")

# Select box demo
st.subheader("📋 Select Options")
option = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: **{option}**")

# Text area
st.subheader("📄 Text Area")
text_area = st.text_area("Write something longer:", "Type your text here...")
if text_area:
    st.info(f"Character count: {len(text_area)}")

st.divider()

# About section
with st.expander("ℹ️ About This App"):
    st.markdown("""
    ### 🚀 Python Streamlit Starter
    
    This is a simple starter template for building web applications with Streamlit.
    
    **Features:**
    - 🎨 Simple and clean interface
    - 🔧 Basic interactive components
    - 📱 Responsive layout
    
    **Tech Stack:**
    - Python 3.x
    - Streamlit
    
    **Getting Started:**
    1. Clone the repository
    2. Install dependencies: `pip install -r requirements.txt`
    3. Run the app: `streamlit run app.py`
    
    **Resources:**
    - [Streamlit Documentation](https://docs.streamlit.io)
    - [Streamlit Gallery](https://streamlit.io/gallery)
    - [Streamlit Community](https://discuss.streamlit.io)
    
    ---
    
    Made with ❤️ using Streamlit
    """)

# Footer
st.divider()
st.caption("© 2024 Python Streamlit Starter | Built with Streamlit")
