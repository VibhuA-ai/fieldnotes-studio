# Fieldnotes Studio

A personal build desk by **VibhuA-ai**. Shape a small project, track its momentum, and keep the thoughts worth returning to.

## Run it

```bash
git clone https://github.com/VibhuA-ai/fieldnotes-studio.git
cd fieldnotes-studio
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

On Windows, create the environment with `python -m venv venv` and activate it with `venv\\Scripts\\activate`.

The app runs at `http://localhost:8501`. In Codespaces, open port `8501` in the **Ports** panel if the browser notification does not appear. If that port is busy, run `streamlit run app.py --server.port 8502` and open port `8502`.

## Inside the studio

- **The desk:** set a working title, intention, and progress for your current idea.
- **Fieldnotes:** capture and revisit thoughts during the session.
- **About:** the principles behind this small workspace.

Project details and notes live in the current Streamlit session and reset when that session ends.

## Stack

Python 3.12 · Streamlit · PyArrow

## License

MIT. See [LICENSE](LICENSE).
