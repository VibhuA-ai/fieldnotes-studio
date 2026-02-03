import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Python Streamlit Starter",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #FF4B4B;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">🚀 Python Streamlit Starter</h1>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Navigation")
    st.write("Welcome to the Streamlit starter app!")
    st.divider()
    
    # User inputs
    st.subheader("Settings")
    user_name = st.text_input("Enter your name:", "User")
    theme_color = st.selectbox("Choose a theme color:", ["Red", "Blue", "Green", "Purple"])
    
    st.divider()
    st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Welcome message
st.write(f"### Hello, {user_name}! 👋")
st.write("This is a starter template for building web applications with Streamlit.")

# Tabs for different sections
tab1, tab2, tab3, tab4 = st.tabs(["📊 Data Visualization", "📈 Interactive Charts", "🔧 Components", "ℹ️ About"])

with tab1:
    st.header("Data Visualization Demo")
    
    # Generate sample data
    st.subheader("Sample Dataset")
    data = pd.DataFrame({
        'Date': pd.date_range(start='2024-01-01', periods=30, freq='D'),
        'Sales': np.random.randint(100, 1000, 30),
        'Customers': np.random.randint(10, 100, 30),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 30)
    })
    
    st.dataframe(data, use_container_width=True)
    
    # Download button
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download data as CSV",
        data=csv,
        file_name='sample_data.csv',
        mime='text/csv',
    )

with tab2:
    st.header("Interactive Charts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sales Over Time")
        fig1 = px.line(data, x='Date', y='Sales', title='Daily Sales Trend')
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.subheader("Sales by Region")
        region_data = data.groupby('Region')['Sales'].sum().reset_index()
        fig2 = px.pie(region_data, values='Sales', names='Region', title='Sales Distribution by Region')
        st.plotly_chart(fig2, use_container_width=True)
    
    st.subheader("Customers vs Sales")
    fig3 = px.scatter(data, x='Customers', y='Sales', color='Region', 
                      title='Customer Count vs Sales', size='Sales')
    st.plotly_chart(fig3, use_container_width=True)

with tab3:
    st.header("Streamlit Components")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Total Sales", value=f"${data['Sales'].sum():,}", delta="12.5%")
    
    with col2:
        st.metric(label="Avg Customers", value=f"{data['Customers'].mean():.0f}", delta="-3.2%")
    
    with col3:
        st.metric(label="Total Days", value=len(data), delta="30 days")
    
    st.divider()
    
    # Interactive widgets
    st.subheader("Interactive Widgets")
    
    col1, col2 = st.columns(2)
    
    with col1:
        slider_value = st.slider("Select a range:", 0, 100, (25, 75))
        st.write(f"Selected range: {slider_value[0]} - {slider_value[1]}")
        
        number_input = st.number_input("Enter a number:", min_value=0, max_value=100, value=50)
        st.write(f"You entered: {number_input}")
    
    with col2:
        date = st.date_input("Select a date:")
        st.write(f"Selected date: {date}")
        
        time = st.time_input("Select a time:")
        st.write(f"Selected time: {time}")
    
    st.divider()
    
    # Checkbox and radio
    st.subheader("Selection Components")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.checkbox("Show additional info"):
            st.info("This is additional information that appears when checked!")
        
        agree = st.checkbox("I agree to the terms and conditions")
        if agree:
            st.success("Thank you for agreeing!")
    
    with col2:
        option = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
        st.write(f"You selected: {option}")
        
        multiselect = st.multiselect("Select multiple options:", 
                                     ["Python", "JavaScript", "Java", "C++", "Ruby"])
        st.write(f"Selected: {', '.join(multiselect)}")
    
    st.divider()
    
    # Progress and status
    st.subheader("Progress & Status Indicators")
    
    col1, col2 = st.columns(2)
    
    with col1:
        progress_value = st.slider("Adjust progress:", 0, 100, 50)
        st.progress(progress_value)
    
    with col2:
        with st.spinner("Loading..."):
            st.write("Content loaded!")
    
    # Alert boxes
    st.info("ℹ️ This is an info message")
    st.success("✅ This is a success message")
    st.warning("⚠️ This is a warning message")
    st.error("❌ This is an error message")

with tab4:
    st.header("About This App")
    
    st.markdown("""
    ### 🚀 Python Streamlit Starter
    
    This is a starter template for building web applications with Streamlit.
    
    **Features:**
    - 📊 Data visualization with Pandas and Plotly
    - 🎨 Custom styling with CSS
    - 📱 Responsive layout with columns and containers
    - 🔧 Interactive widgets and components
    - 📁 Multi-page app structure support
    
    **Tech Stack:**
    - Python 3.x
    - Streamlit
    - Pandas
    - NumPy
    - Plotly
    
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
    
    # Expander for more info
    with st.expander("View Source Code Structure"):
        st.code("""
project/
│
├── app.py                 # Main application file
├── pages/                 # Additional pages (for multi-page apps)
│   ├── 1_📊_Data.py
│   └── 2_⚙️_Settings.py
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore file
└── README.md             # Project documentation
        """, language="text")

# Footer
st.divider()
st.caption("© 2024 Python Streamlit Starter | Built with Streamlit")
