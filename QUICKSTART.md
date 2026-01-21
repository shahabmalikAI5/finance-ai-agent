# Quick Start Guide - Finance Agent

## 🚀 Get Started in 3 Minutes

### Prerequisites
- Python 3.8 or higher
- Internet connection

### Installation Steps

1. **Navigate to the project directory:**
```bash
cd "/mnt/d/Data all/claude-code-router-setup/"
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### First Run

**Option A: Interactive CLI (Recommended)**
```bash
python finance_agent.py
```

**Option B: Quick Test**
```bash
python quick_test.py
```

**Option C: Example Demonstrations**
```bash
python example_usage.py
```

## 🎯 Try These Examples

### Basic Commands

Once the agent is running, try these queries:

**Stock Analysis:**
```
What's the current price of Apple stock (AAPL)?
```

**Portfolio Management:**
```
Analyze my portfolio with 100 shares of AAPL at $150
```

**Market Intelligence:**
```
What's the latest market news?
```

**Currency Conversion:**
```
Convert 1000 USD to EUR
```

**Risk Assessment:**
```
Assess my portfolio risk with beta 1.2 and 20% volatility
```

## 📱 Interactive Mode

The agent features an interactive chat interface:

```
🤖 Finance Agent - Powered by OpenAI Agents SDK
==================================================
I can help you with:
📊 Stock analysis and prices
💼 Portfolio management and performance
📈 Market news and trends
💱 Currency conversion
⚠️  Risk assessment

💬 Your question: What's the current price of AAPL?
```

## 🔧 Configuration Options

### OpenAI API Key (Optional)

For production use with real data, set your OpenAI API key:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Or create a `.env` file:
```bash
OPENAI_API_KEY=your-api-key-here
```

### Testing Without API Key

The agent works without an API key using simulated data for testing and demonstration purposes.

## 📊 Examples of Complex Queries

### Multi-Part Analysis
```
I have a portfolio with:
- 100 shares of AAPL at $150
- 50 shares of MSFT at $300
- 25 shares of GOOGL at $2800

First analyze the portfolio performance, then assess risk levels,
and provide recommendations for improvement.
```

### Investment Planning
```
Calculate my returns if I invested $10000 and now have $15000 over 3 years.
What does this CAGR mean for my investment strategy?
```

### Market Research
```
Get the latest tech sector news and tell me which companies
are mentioned most frequently and why.
```

## 🧪 Testing

### Run the Test Suite
```bash
python test_finance_agent.py
```

### Quick Verification
```bash
python quick_test.py
```

## 🚨 Troubleshooting

### Common Issues

**"Module not found: agents"**
```bash
pip install -r requirements.txt
```

**"OpenAI API key not found"**
- The agent works without an API key for testing
- Or set your key: `export OPENAI_API_KEY="your-key"`

**"Python not found"**
- Ensure Python 3.8+ is installed: `python --version`
- Try `python3` instead of `python`

### Get Help

Check the full documentation in `README.md` or visit:
- OpenAI Agents SDK: https://github.com/openai/openai-agents-python

## 🎓 Next Steps

1. **Master the basics** - Try simple queries first
2. **Explore advanced features** - Use `example_usage.py`
3. **Customize the agent** - Modify `finance_agent.py`
4. **Add real APIs** - Integrate with Alpha Vantage, Yahoo Finance
5. **Build a web interface** - Use Streamlit or FastAPI

## 📁 Files Overview

| File | Purpose |
|------|---------|
| `finance_agent.py` | Main agent implementation |
| `example_usage.py` | Comprehensive examples |
| `test_finance_agent.py` | Test suite |
| `quick_test.py` | Quick verification |
| `requirements.txt` | Dependencies |
| `README.md` | Full documentation |
| `setup.py` | Setup helper |

---

**Happy Analyzing! 🤖📈💰**

*Need help? Check README.md or run `python setup.py` for guided setup.*