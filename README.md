# 🚀 Python Streamlit Starter

<!-- Note: Update the repository path in the badge URL if you fork this template -->
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Takeoff-Techworks/python-starter)

A simple starter template for building web applications with Streamlit. Perfect for beginners and quick prototypes!

## ✨ Features

- 🎨 **Simple & Clean**: Easy-to-understand code structure
- 🔧 **Interactive Components**: Basic Streamlit widgets and components
- 📱 **Responsive Layout**: Works on different screen sizes
- 🚀 **GitHub Copilot Ready**: Pre-configured with Copilot extension
- 🎯 **Best Practices**: Follows Streamlit best practices and conventions

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** - Web app framework
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
   # Or use the quick start script:
   ./start.sh
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
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .devcontainer/             # GitHub Codespaces configuration
├── .gitignore                 # Git ignore file
└── README.md                  # Project documentation
```

## 📖 Usage

### Main Page (app.py)

The main page includes:
- Welcome section with user input
- Basic interactive components (text input, sliders, buttons)
- Simple demonstrations of Streamlit widgets
- About section with documentation

## 🎨 Customization

### Adding Features

You can easily extend this starter by adding:
- More interactive widgets
- Custom styling with CSS
- Additional pages (create a `pages/` directory)
- Data visualization libraries (Plotly, Matplotlib)
- Database connections

Example of adding custom CSS:

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
- API keys
- Debug mode
- Server settings

## 🔧 Development

### Development Environments

#### GitHub Codespaces (Cloud-Based)
- **Zero Setup**: Click the badge at the top of this README
- **Pre-configured**: Python 3.12, all extensions including GitHub Copilot
- **Instant**: Start coding in seconds
- **Free Tier**: 60 hours/month for GitHub Free users
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