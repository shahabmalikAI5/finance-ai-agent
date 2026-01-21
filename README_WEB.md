# 🌐 Finance Agent Web Interface

Beautiful web interface for the Finance Agent using Streamlit.

## 🚀 Quick Start

### Local Development

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the app:**
```bash
streamlit run app.py
```

3. **Open in browser:**
```
http://localhost:8501
```

## 🌐 Deploy Online

### Option 1: Streamlit Cloud (Recommended - Free & Easy)

1. **Push code to GitHub:**
```bash
git init
git add .
git commit -m "Add Finance Agent Web Interface"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/finance-agent.git
git push -u origin main
```

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub repository
   - Select `app.py` as main file
   - Click "Deploy" ✨

3. **Add Environment Variables:**
   - In Streamlit Cloud, go to your app settings
   - Add secret: `OPENAI_API_KEY` = `your-openrouter-key-here`
   - Add secret: `OPENAI_BASE_URL` = `https://openrouter.ai/api/v1`

### Option 2: Hugging Face Spaces (Also Free)

1. **Create new Space at [huggingface.co/spaces](https://huggingface.co/spaces)**

2. **Choose "Streamlit" as SDK**

3. **Upload files:**
   - `app.py`
   - `requirements.txt`
   - `finance_agent.py`
   - All other Python files

4. **Add secrets in Settings:**
   - `OPENAI_API_KEY`
   - `OPENAI_BASE_URL`

5. **Auto-deploys!** 🎉

### Option 3: Railway.app / Render.com

1. **Create `web_app.py`:**
```python
import subprocess
import sys

subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py", "--server.port=8501"])
```

2. **Deploy on Railway.app or Render.com**

## 🎨 Features

- ✅ Beautiful chat interface
- ✅ Conversation memory (remembers context!)
- ✅ Real-time stock prices
- ✅ Currency conversion (PKR, INR, EUR, etc.)
- ✅ Portfolio analysis
- ✅ Market news
- ✅ Example questions sidebar
- ✅ Mobile responsive
- ✅ Dark/light theme support

## 📸 Screenshots

- **Chat Interface**: Modern, clean UI with message history
- **Sidebar**: Example questions, settings, session info
- **Responsive**: Works on desktop, tablet, mobile

## 🔧 Configuration

### Environment Variables (.env)

```bash
OPENAI_API_KEY=sk-or-v1-your-key-here
OPENAI_BASE_URL=https://openrouter.ai/api/v1
```

### Streamlit Config (.streamlit/config.toml)

```toml
[browser]
gatherUsageStats = false

[theme]
primaryColor = "#667eea"
backgroundColor = "#ffffff"
```

## 💡 Usage Tips

1. **Start with simple questions:**
   - "What's Apple's stock price?"
   - "Convert 100 USD to PKR"

2. **Follow-up questions work perfectly:**
   - "Convert **that** to PKR" ✨ (Agent remembers!)
   - "Now subtract 10% from **it**"

3. **Try investment scenarios:**
   - "If I invested $1000 in Tesla 5 years ago..."
   - "What's my portfolio worth: 10 AAPL, 5 GOOGL?"

## 🛠️ Troubleshooting

### Port already in use
```bash
# Use different port
streamlit run app.py --server.port 8502
```

### ModuleNotFoundError
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### API Key errors
- Check `.env` file has correct OpenRouter key
- On Streamlit Cloud, add secrets in app settings

## 📚 Tech Stack

- **Backend**: Python 3.10+
- **Framework**: Streamlit
- **AI**: OpenAI Agents SDK
- **Model**: Google Gemini 2.0 Flash (via OpenRouter)
- **Database**: SQLite (conversation memory)

## 🌟 Credits

Built with:
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python)
- [Streamlit](https://streamlit.io)
- [OpenRouter](https://openrouter.ai)
- [Google Gemini](https://ai.google.dev)

---

**Made with ❤️ | Powered by Google Gemini (FREE via OpenRouter)**
