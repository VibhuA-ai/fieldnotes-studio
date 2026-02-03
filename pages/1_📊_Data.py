import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Data Analysis", page_icon="📊", layout="wide")

st.title("📊 Data Analysis Dashboard")
st.write("Explore and analyze your data with interactive visualizations.")

# Sidebar for data configuration
with st.sidebar:
    st.header("Data Configuration")
    data_points = st.slider("Number of data points:", 10, 500, 100)
    chart_type = st.selectbox("Chart Type:", ["Line", "Bar", "Area", "Scatter"])
    show_statistics = st.checkbox("Show Statistics", value=True)

# Generate sample data
st.subheader("Generated Dataset")

# Create sample dataframe
dates = pd.date_range(start='2024-01-01', periods=data_points, freq='D')
data = pd.DataFrame({
    'Date': dates,
    'Value_A': np.random.randn(data_points).cumsum() + 100,
    'Value_B': np.random.randn(data_points).cumsum() + 50,
    'Category': np.random.choice(['Category 1', 'Category 2', 'Category 3', 'Category 4'], data_points)
})

# Display data
with st.expander("View Raw Data"):
    st.dataframe(data, use_container_width=True)

# Statistics
if show_statistics:
    st.subheader("Statistical Summary")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Mean Value A", f"{data['Value_A'].mean():.2f}")
    with col2:
        st.metric("Mean Value B", f"{data['Value_B'].mean():.2f}")
    with col3:
        st.metric("Std Dev A", f"{data['Value_A'].std():.2f}")
    with col4:
        st.metric("Std Dev B", f"{data['Value_B'].std():.2f}")

# Visualization
st.subheader("Data Visualization")

col1, col2 = st.columns(2)

with col1:
    st.write("**Time Series Analysis**")
    if chart_type == "Line":
        fig1 = px.line(data, x='Date', y=['Value_A', 'Value_B'], 
                       title='Time Series - Line Chart')
    elif chart_type == "Bar":
        fig1 = px.bar(data, x='Date', y=['Value_A', 'Value_B'], 
                      title='Time Series - Bar Chart')
    elif chart_type == "Area":
        fig1 = px.area(data, x='Date', y=['Value_A', 'Value_B'], 
                       title='Time Series - Area Chart')
    else:
        fig1 = px.scatter(data, x='Date', y='Value_A', size='Value_B',
                         title='Time Series - Scatter Plot')
    
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.write("**Distribution Analysis**")
    fig2 = go.Figure()
    fig2.add_trace(go.Histogram(x=data['Value_A'], name='Value A', opacity=0.7))
    fig2.add_trace(go.Histogram(x=data['Value_B'], name='Value B', opacity=0.7))
    fig2.update_layout(title='Value Distribution', barmode='overlay')
    st.plotly_chart(fig2, use_container_width=True)

# Category analysis
st.subheader("Category Analysis")

category_summary = data.groupby('Category').agg({
    'Value_A': ['mean', 'sum', 'count'],
    'Value_B': ['mean', 'sum']
}).round(2)

col1, col2 = st.columns([2, 1])

with col1:
    fig3 = px.box(data, x='Category', y=['Value_A', 'Value_B'], 
                  title='Value Distribution by Category')
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.write("**Summary by Category**")
    st.dataframe(category_summary, use_container_width=True)

# Correlation heatmap
st.subheader("Correlation Analysis")
numeric_data = data[['Value_A', 'Value_B']]
corr_matrix = numeric_data.corr()

fig4 = px.imshow(corr_matrix, 
                 labels=dict(color="Correlation"),
                 x=['Value A', 'Value B'],
                 y=['Value A', 'Value B'],
                 color_continuous_scale='RdBu',
                 title='Correlation Heatmap')
fig4.update_layout(width=500, height=400)
st.plotly_chart(fig4, use_container_width=False)

# Data export
st.divider()
st.subheader("Export Data")

col1, col2, col3 = st.columns(3)

with col1:
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name='analysis_data.csv',
        mime='text/csv'
    )

with col2:
    json_data = data.to_json(orient='records', date_format='iso')
    st.download_button(
        label="📥 Download JSON",
        data=json_data,
        file_name='analysis_data.json',
        mime='application/json'
    )

with col3:
    if st.button("🔄 Refresh Data"):
        st.rerun()
