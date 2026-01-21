# Finance Agent - OpenAI Agents SDK

A sophisticated multi-agent financial assistant built using the OpenAI Agents SDK. This agent provides comprehensive financial analysis, portfolio management, market intelligence, and currency services through specialized agents working together.

## 🚀 Features

### 🏢 Multi-Agent Architecture
- **Finance Assistant Triage**: Intelligent routing to specialized agents
- **Stock Analyst**: Individual stock analysis and equity research
- **Portfolio Manager**: Portfolio performance analysis and risk assessment
- **Market Intelligence**: Real-time market news and trends
- **Currency Specialist**: International markets and forex conversion

### 💰 Financial Capabilities
- **Stock Price Analysis**: Get current prices and performance metrics
- **Portfolio Analysis**: Calculate returns, gains/losses, and portfolio metrics
- **Market News**: Latest financial news and market updates
- **Currency Conversion**: Real-time exchange rates and conversion
- **Risk Assessment**: Evaluate portfolio risk and get recommendations
- **Investment Returns**: Calculate CAGR and performance metrics

### 🔧 Advanced Features
- **Structured Output**: Type-safe responses using Pydantic models
- **Async Architecture**: Non-blocking operations for better performance
- **Context-Aware Routing**: Smart agent selection based on query analysis
- **Error Handling**: Robust exception handling and graceful failures
- **Interactive CLI**: User-friendly command-line interface

## 📦 Installation

### Prerequisites
- Python 3.8+
- OpenAI API key (for production use)

### Setup Steps

1. **Clone and navigate to project:**
```bash
cd "/mnt/d/Data all/claude-code-router-setup/"
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables (optional for production):**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## 🎯 Usage Examples

### Basic Usage

Run the interactive CLI:
```bash
python finance_agent.py
```

### Example Queries

#### Stock Analysis
```
"What's the current price of Apple stock (AAPL)?"
"Analyze Tesla stock performance"
"Get price updates for Microsoft and Google"
```

#### Portfolio Management
```
"Analyze my portfolio: 100 shares of AAPL at $150, 50 shares of MSFT at $300"
"What are my returns if I invested $10000 and now have $12500 over 2 years?"
"Assess my portfolio risk with beta 1.2 and 20% volatility"
```

#### Market Intelligence
```
"What's the latest market news?"
"Give me recent tech sector updates"
"Latest cryptocurrency news"
```

#### Currency & International
```
"Convert 1000 USD to EUR"
"How much is 500 GBP in JPY?"
"Currency exchange analysis for international investment"
```

### Programmatic Usage

```python
import asyncio
from finance_agent import run_finance_agent

async def main():
    # Simple query
    response = await run_finance_agent("What's the current price of AAPL?")
    print(response)

    # Portfolio analysis
    portfolio = [
        {"symbol": "AAPL", "shares": 100, "average_cost": 150},
        {"symbol": "MSFT", "shares": 50, "average_cost": 300}
    ]
    response = await run_finance_agent(f"Analyze my portfolio: {portfolio}")
    print(response)

asyncio.run(main())
```

## 🏗️ Architecture

### Agent Hierarchy
```
Finance Assistant Triage (Main Entry Point)
├── Stock Analyst (Equities & Stocks)
├── Portfolio Manager (Performance & Risk)
├── Market Intelligence (News & Trends)
└── Currency Specialist (Forex & International)
```

### Tools Overview
- `get_stock_price()`: Fetch stock data
- `analyze_portfolio()`: Portfolio performance analysis
- `calculate_returns()`: Investment return calculations
- `risk_assessment()`: Portfolio risk evaluation
- `get_market_news()`: Latest market updates
- `currency_converter()`: Exchange rate conversion

## 🔧 Customization

### Adding Real Financial APIs

Replace mock data with real APIs:

```python
@function_tool
def get_stock_price(symbol: str) -> StockPrice:
    # Use real API like Alpha Vantage, Yahoo Finance, or Polygon.io
    import requests
    response = requests.get(f"https://api.polygon.io/v2/stocks/{symbol}/quotes")
    data = response.json()
    # Parse and return StockPrice...
```

### Adding New Tools

```python
@function_tool
def analyze_technical_indicators(
    symbol: Annotated[str, "Stock symbol"]
) -> TechnicalAnalysis:
    """Analyze technical indicators for a stock."""
    # Your implementation here
    pass

# Add to agents
stock_agent = Agent(
    name="Stock Analyst",
    tools=[get_stock_price, analyze_technical_indicators]  # Add new tool
)
```

## 📊 Sample Output

```
🤖 Finance Agent - Powered by OpenAI Agents SDK
==================================================
I can help you with:
📊 Stock analysis and prices
💼 Portfolio management and performance
📈 Market news and trends
💱 Currency conversion
⚠️ Risk assessment

💬 Your question: What's the current price of AAPL?

🤔 Processing your request...

📝 Answer:
The current price of Apple Inc. (AAPL) is $178.52, with a change of +2.34 (+1.33%).
This represents positive momentum in today's trading session. The stock has shown
strength with over 1% gains, which could indicate positive sentiment surrounding
the company's latest announcements or overall market conditions.
```

## 🔒 Security & Best Practices

### API Keys
- Never hardcode API keys in the code
- Use environment variables or secure key management
- In production, use services like AWS Secrets Manager or Azure Key Vault

### Error Handling
- All tools include proper error handling
- Graceful degradation if external APIs fail
- Clear error messages for troubleshooting

### Rate Limiting
- Implement rate limiting for external API calls
- Use appropriate delays between requests
- Respect API terms of service

## 🧪 Testing

Run basic tests to verify functionality:

```python
import asyncio
from finance_agent import run_finance_agent

async def test_agents():
    test_queries = [
        "Get stock price for AAPL",
        "Analyze a simple portfolio",
        "What's the latest market news?",
        "Convert 100 USD to EUR"
    ]

    for query in test_queries:
        print(f"\nTesting: {query}")
        response = await run_finance_agent(query)
        print(f"Response: {response[:200]}...")  # Print first 200 chars

asyncio.run(test_agents())
```

## 🚧 Future Enhancements

- [ ] **Real-time Data**: Integrate with live financial data providers
- [ ] **Technical Analysis**: Add technical indicators (RSI, MACD, Moving Averages)
- [ ] **Chart Generation**: Generate price charts and visualizations
- [ ] **Sentiment Analysis**: News sentiment scoring
- [ ] **Machine Learning**: Predictive analytics and trend forecasting
- [ ] **Web Interface**: Streamlit or FastAPI web dashboard
- [ ] **Portfolio Optimization**: Modern portfolio theory implementation
- [ ] **Risk Models**: Value at Risk (VaR) calculations

## 📝 Project Structure

```
claude-code-router-setup/
├── finance_agent.py           # Main agent implementation
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── .claude/                   # Claude configuration (existing)
```

## 🔗 OpenAI Agents SDK Documentation

- [Official Documentation](https://github.com/openai/openai-agents-python)
- [API Reference](https://github.com/openai/openai-agents-python/blob/main/docs)
- [Examples & Patterns](https://github.com/openai/openai-agents-python/tree/main/examples)

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional financial tools and data sources
- Advanced analytics and metrics
- Multi-currency portfolio support
- Real-time market data integration

## 📄 License

This project is for educational and demonstration purposes.

---

**Built with OpenAI Agents SDK** | **Multi-Agent Architecture** | **Financial Intelligence**