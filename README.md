# Python Streamlit Starter

<!-- Note: Update the repository path in the badge URL if you fork this template -->
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Takeoff-Techworks/python-starter)


### Quick Start with GitHub Codespaces (Recommended)

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

### Local Development Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/Takeoff-Techworks/python-starter.git
cd python-starter
```

#### 2. Create a Virtual Environment (Recommended)

1. In VSCode open command palette with Ctrl/Command + Shift + P
1. In search bar type environment
1. Select Python > Create Environment > venv > Create new
1. Open a new terminal with Ctrl/Cmd + Shift + C to verify environment is activated

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
# Run with file watcher for auto-reload
streamlit run app.py --server.runOnSave true
```

The app will open automatically in your default browser at `http://localhost:8501`

### Environment Variables

Edit the `.env` file to configure:
- App name and version
- API keys
- Debug mode
- Server settings

## Resources

- [Streamlit Documentation](https://docs.streamlit.io)


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


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
