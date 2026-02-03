# 🚀 Python Streamlit Starter

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Takeoff-Techworks/python-starter)

A comprehensive starter template for building web applications with Streamlit, featuring data visualization, interactive components, and a multi-page app structure.

## ✨ Features

- 📊 **Data Visualization**: Interactive charts and graphs using Plotly
- 🎨 **Modern UI**: Clean, responsive design with custom styling
- 📱 **Multi-Page App**: Organized structure with multiple pages
- 🔧 **Rich Components**: Wide variety of Streamlit widgets and components
- 📈 **Data Analysis**: Built-in data analysis and statistics tools
- ⚙️ **Settings Page**: Customizable user preferences and configuration
- 📥 **Data Export**: Download data in CSV and JSON formats
- 🎯 **Best Practices**: Follows Streamlit best practices and conventions

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** - Web app framework
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Plotly** - Interactive visualizations
- **python-dotenv** - Environment variable management

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🚀 Getting Started

### Quick Start with GitHub Codespaces (Recommended) ⚡

The fastest way to get started is using GitHub Codespaces:

1. Click the **Code** button on the repository
2. Select the **Codespaces** tab
3. Click **Create codespace on main**
4. Wait for the environment to build (dependencies install automatically)
5. Once ready, run:
   ```bash
   streamlit run app.py
   ```
6. Click the pop-up notification to open the app in your browser

That's it! No local setup required. 🎉

### Local Development Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/Takeoff-Techworks/python-starter.git
cd python-starter
```

#### 2. Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Configure Environment Variables (Optional)

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your configuration
```

#### 5. Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your default browser at `http://localhost:8501`

## 📁 Project Structure

```
python-starter/
│
├── app.py                      # Main application file
├── pages/                      # Additional pages
│   ├── 1_📊_Data.py           # Data analysis page
│   └── 2_⚙️_Settings.py       # Settings page
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore file
└── README.md                  # Project documentation
```

## 📖 Usage

### Main Page (app.py)

The main page includes:
- Welcome section with user input
- Data visualization demos
- Interactive charts with Plotly
- Various Streamlit components showcase
- About section with documentation

### Data Analysis Page

Navigate to the "📊 Data" page to:
- Generate and visualize sample datasets
- Analyze data with interactive charts
- View statistical summaries
- Export data in multiple formats

### Settings Page

Navigate to the "⚙️ Settings" page to:
- Customize appearance and theme
- Manage user profile
- Configure notifications
- Export/import settings

## 🎨 Customization

### Adding New Pages

To add a new page to your Streamlit app:

1. Create a new Python file in the `pages/` directory
2. Name it with a number prefix and emoji: `3_🎯_YourPage.py`
3. Add your Streamlit code to the file

Example:

```python
import streamlit as st

st.set_page_config(page_title="Your Page", page_icon="🎯")

st.title("🎯 Your New Page")
st.write("Your content here...")
```

### Modifying Styles

Custom CSS can be added in any page using:

```python
st.markdown("""
    <style>
    .your-custom-class {
        /* Your styles here */
    }
    </style>
    """, unsafe_allow_html=True)
```

### Environment Variables

Edit the `.env` file to configure:
- App name and version
- Database connections
- API keys
- Debug mode
- Server settings

## 📊 Example Data Visualizations

The starter includes examples of:
- Line charts
- Bar charts
- Scatter plots
- Pie charts
- Heatmaps
- Box plots
- Histograms

## 🔧 Development

### Development Environments

#### GitHub Codespaces (Cloud-Based)
- **Zero Setup**: Click the badge at the top of this README
- **Pre-configured**: Python 3.12, all extensions, and dependencies
- **Instant**: Start coding in seconds
- **Free Tier**: 60 hours/month for GitHub Free users

#### VS Code Dev Containers (Local)
- **Consistent**: Same environment as Codespaces
- **Offline**: Work without internet after initial setup
- **Requirement**: Docker Desktop installed
- **Setup**: Open in VS Code and select "Reopen in Container"

#### Traditional Local Setup
- **Manual**: Follow the local development setup above
- **Flexible**: Use any editor or IDE
- **Requirement**: Python 3.8+ installed locally

### Running in Development Mode

```bash
# Run with file watcher for auto-reload
streamlit run app.py --server.runOnSave true
```

### Installing Additional Dependencies

```bash
pip install <package-name>
pip freeze > requirements.txt
```

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Streamlit Community Forum](https://discuss.streamlit.io)
- [Plotly Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💡 Tips

- Use `st.cache_data` for caching data computations
- Use `st.cache_resource` for caching resource-heavy operations
- Organize complex apps into multiple pages
- Use columns and containers for better layouts
- Add custom CSS for enhanced styling
- Use session state for maintaining data across reruns

## 🐛 Troubleshooting

### Port Already in Use

If port 8501 is already in use:

```bash
streamlit run app.py --server.port 8502
```

### Module Not Found Error

Make sure all dependencies are installed:

```bash
pip install -r requirements.txt
```

### Virtual Environment Issues

Deactivate and reactivate your virtual environment:

```bash
deactivate
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
```

## 📧 Support

For questions or issues, please open an issue on GitHub or contact the maintainers.

---

**Made with ❤️ using Streamlit**