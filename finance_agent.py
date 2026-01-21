"""
Finance Agent using OpenAI Agents SDK with Google AI via OpenRouter (FREE!)
A comprehensive multi-agent system for financial analysis, portfolio management, and market insights.

Configuration: Uses Google Gemini 2.0 Flash via OpenRouter (FREE models)
Provider: OpenRouter (https://openrouter.ai/)
Model: google/gemini-2.0-flash-exp:free
"""

import asyncio
import json
import os
import random
from datetime import datetime, timedelta
from typing import Annotated, List, Dict, Any, Optional
from pydantic import BaseModel, Field

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

from agents import Agent, Runner, function_tool, Handoff, SQLiteSession
from agents.extensions.handoff_prompt import prompt_with_handoff_instructions


# ==================== OPENROUTER + GOOGLE AI CONFIGURATION ====================

# OpenRouter Configuration
# Read from OPENAI_API_KEY since that's what's configured in .env
OPENROUTER_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENROUTER_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")

# Using Google Gemini 2.0 Flash via OpenRouter (FREE model!)
# More info: https://openrouter.ai/models?free=true
DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "google/gemini-2.0-flash-exp:free")

def get_openai_client():
    """Create an OpenAI client configured for OpenRouter with Google AI models"""
    from openai import OpenAI

    return OpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL
    )


# ==================== FINANCIAL DATA MODELS ====================

class StockPrice(BaseModel):
    """Stock price information"""
    symbol: str = Field(description="Stock ticker symbol")
    price: float = Field(description="Current price")
    change: float = Field(description="Price change from previous close")
    change_percent: float = Field(description="Percentage change")
    timestamp: str = Field(description="Timestamp of the data")


class PortfolioSummary(BaseModel):
    """Portfolio performance summary"""
    total_value: float = Field(description="Total portfolio value")
    total_gain_loss: float = Field(description="Total gain/loss amount")
    gain_loss_percent: float = Field(description="Percentage gain/loss")
    num_positions: int = Field(description="Number of positions")


class MarketNews(BaseModel):
    """Market news item"""
    headline: str = Field(description="News headline")
    source: str = Field(description="News source")
    timestamp: str = Field(description="Publication time")
    summary: str = Field(description="Brief summary of the news")


class FinancialAnalysis(BaseModel):
    """Financial analysis result"""
    metric: str = Field(description="Metric being analyzed")
    value: float = Field(description="Metric value")
    interpretation: str = Field(description="Interpretation of the metric")
    recommendation: str = Field(description="Recommendation based on analysis")


class PortfolioHolding(BaseModel):
    """Individual portfolio holding"""
    symbol: str = Field(description="Stock ticker symbol")
    shares: float = Field(description="Number of shares")
    average_cost: float = Field(description="Average cost per share")


# ==================== FINANCIAL TOOLS ====================

@function_tool
def get_stock_price(symbol: Annotated[str, "Stock ticker symbol (e.g., AAPL, GOOGL)"]) -> StockPrice:
    """Get current stock price and recent performance for any stock symbol."""
    # Simulate fetching stock data (in production, use a real API like Alpha Vantage, Yahoo Finance)
    base_price = random.uniform(50, 500)
    change = random.uniform(-10, 10)
    change_percent = (change / base_price) * 100

    return StockPrice(
        symbol=symbol.upper(),
        price=round(base_price, 2),
        change=round(change, 2),
        change_percent=round(change_percent, 2),
        timestamp=datetime.now().isoformat()
    )


@function_tool
def get_market_news(
    category: Annotated[str, "Market category (stocks, crypto, economy, tech)"] = "stocks",
    limit: Annotated[int, "Number of news items to return"] = 5
) -> List[MarketNews]:
    """Get latest market news and financial updates."""
    categories = {
        "stocks": ["Stock Market", "Equities", "Wall Street"],
        "crypto": ["Cryptocurrency", "Bitcoin", "DeFi"],
        "economy": ["Economy", "Inflation", "Federal Reserve"],
        "tech": ["Technology", "AI", "Semiconductors"]
    }

    sources = ["Bloomberg", "Reuters", "CNBC", "Financial Times", "MarketWatch"]

    news_items = []
    for i in range(limit):
        category_name = random.choice(categories.get(category, ["Market"]))
        source = random.choice(sources)

        news_items.append(MarketNews(
            headline=f"{category_name} Update: Market analysis and insights {i+1}",
            source=source,
            timestamp=(datetime.now() - timedelta(hours=random.randint(0, 24))).isoformat(),
            summary=f"Analysis of {category_name.lower()} trends and market movements. Expert opinions on future direction."
        ))

    return news_items


@function_tool
def analyze_portfolio(
    holdings: Annotated[List[PortfolioHolding], "List of portfolio holdings"]
) -> PortfolioSummary:
    """Analyze portfolio performance and calculate metrics."""
    total_value = 0
    total_cost = 0

    for holding in holdings:
        symbol = holding.symbol.upper()
        shares = holding.shares
        avg_cost = holding.average_cost

        # Get current price (in production, would fetch real data)
        current_price = get_stock_price(symbol).price

        total_cost += shares * avg_cost
        total_value += shares * current_price

    total_gain_loss = total_value - total_cost
    gain_loss_percent = (total_gain_loss / total_cost * 100) if total_cost > 0 else 0

    return PortfolioSummary(
        total_value=round(total_value, 2),
        total_gain_loss=round(total_gain_loss, 2),
        gain_loss_percent=round(gain_loss_percent, 2),
        num_positions=len(holdings)
    )


@function_tool
def calculate_returns(
    initial_investment: Annotated[float, "Initial investment amount"],
    final_value: Annotated[float, "Final portfolio value"],
    period_years: Annotated[float, "Investment period in years"]
) -> FinancialAnalysis:
    """Calculate investment returns and performance metrics."""
    total_return = final_value - initial_investment
    total_return_percent = (total_return / initial_investment) * 100

    # Calculate CAGR (Compound Annual Growth Rate)
    cagr = ((final_value / initial_investment) ** (1 / period_years) - 1) * 100

    interpretation = f"Your investment grew by {total_return_percent:.2f}% over {period_years} years. "

    if cagr > 10:
        recommendation = "Excellent performance! Consider maintaining your strategy."
    elif cagr > 5:
        recommendation = "Good performance. Continue monitoring and diversifying."
    else:
        recommendation = "Review investment strategy for better returns."

    return FinancialAnalysis(
        metric="CAGR",
        value=round(cagr, 2),
        interpretation=interpretation + f"Annualized return: {cagr:.2f}%",
        recommendation=recommendation
    )


@function_tool
def currency_converter(
    amount: Annotated[float, "Amount to convert"],
    from_currency: Annotated[str, "Source currency (USD, EUR, GBP, JPY, PKR, etc.)"],
    to_currency: Annotated[str, "Target currency (USD, EUR, GBP, JPY, PKR, etc.)"]
) -> FinancialAnalysis:
    """Convert between different currencies with current exchange rates."""
    # Simulate exchange rates (in production, use real exchange rate API)
    # Rates as of January 2025
    exchange_rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.79,
        "JPY": 149.50,
        "CAD": 1.35,
        "AUD": 1.52,
        "CHF": 0.88,
        "PKR": 278.50,  # Pakistani Rupee
        "INR": 83.12,   # Indian Rupee
        "CNY": 7.24,    # Chinese Yuan
        "AED": 3.67,    # UAE Dirham
        "SAR": 3.75     # Saudi Riyal
    }

    from_rate = exchange_rates.get(from_currency.upper(), 1.0)
    to_rate = exchange_rates.get(to_currency.upper(), 1.0)

    converted_amount = (amount / from_rate) * to_rate

    return FinancialAnalysis(
        metric="Currency Conversion",
        value=round(converted_amount, 2),
        interpretation=f"{amount} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}",
        recommendation=f"Conversion rate: {1/from_rate:.4f} {from_currency}/USD, {to_rate:.4f} {to_currency}/USD"
    )


@function_tool
def risk_assessment(
    portfolio_beta: Annotated[float, "Portfolio beta (systematic risk)"],
    volatility: Annotated[float, "Portfolio volatility percentage"],
    diversification_score: Annotated[int, "Diversification score 1-10"]
) -> FinancialAnalysis:
    """Assess portfolio risk and provide recommendations."""
    risk_level = "Low"
    if portfolio_beta > 1.2 or volatility > 25:
        risk_level = "High"
    elif portfolio_beta > 0.8 or volatility > 15:
        risk_level = "Medium"

    recommendations = []

    if risk_level == "High":
        recommendations.append("Consider reducing high-beta positions")
        recommendations.append("Add defensive stocks and bonds")
        recommendations.append("Increase cash position")
    elif risk_level == "Medium":
        recommendations.append("Maintain current allocation")
        recommendations.append("Consider gradual rebalancing")
    else:
        recommendations.append("Your portfolio is well-positioned")
        recommendations.append("Consider growth opportunities")

    if diversification_score < 6:
        recommendations.append("Improve diversification across sectors")

    return FinancialAnalysis(
        metric="Risk Level",
        value=portfolio_beta,
        interpretation=f"Portfolio risk level: {risk_level}. Beta: {portfolio_beta}, Volatility: {volatility}%",
        recommendation="; ".join(recommendations)
    )


# ==================== SPECIALIZED AGENTS ====================

# Create model settings for OpenRouter with Google AI
def create_model_settings():
    """Create ModelSettings for OpenRouter with FREE tier compatibility"""
    from agents import ModelSettings
    return ModelSettings(
        model=DEFAULT_MODEL,
        base_url=OPENROUTER_BASE_URL,
        api_key=OPENROUTER_API_KEY,
        max_tokens=2000  # Reduced for stability with free tier
    )

# Stock Analysis Agent
stock_agent = Agent(
    name="Stock Analyst",
    handoff_description="Specialist for stock analysis and equity research",
    instructions=(
        "You are a professional stock analyst. Provide detailed analysis of individual stocks, "
        "including price trends, fundamental metrics, and investment recommendations. "
        "Always use the get_stock_price tool for current data and provide thoughtful analysis.\n\n"
        "IMPORTANT: Always provide calculations clearly. If user mentions previous calculations "
        "or wants to convert values to other currencies, explicitly acknowledge the amount and "
        "suggest using the currency specialist if needed."
    ),
    tools=[get_stock_price],
    model_settings=create_model_settings()
)

# Portfolio Management Agent
portfolio_agent = Agent(
    name="Portfolio Manager",
    handoff_description="Specialist for portfolio analysis and management",
    instructions=prompt_with_handoff_instructions(
        "You are a skilled portfolio manager. Analyze investment portfolios, calculate returns, "
        "assess risk, and provide optimization recommendations. Use analyze_portfolio and "
        "calculate_returns tools for comprehensive analysis."
    ),
    tools=[analyze_portfolio, calculate_returns, risk_assessment],
    model_settings=create_model_settings()
)

# Market Intelligence Agent
market_agent = Agent(
    name="Market Intelligence Analyst",
    handoff_description="Specialist for market news and trends",
    instructions=prompt_with_handoff_instructions(
        "You are a market intelligence expert. Provide latest market news, trends, and insights. "
        "Use get_market_news tool to fetch current information and provide context-rich analysis."
    ),
    tools=[get_market_news],
    model_settings=create_model_settings()
)

# Currency and Global Markets Agent
currency_agent = Agent(
    name="Currency Specialist",
    handoff_description="Expert for currency conversion and international markets",
    instructions=(
        "You are a currency and international markets specialist. Handle currency conversions, "
        "analyze international market trends, and provide global investment insights. "
        "Use currency_converter tool for accurate conversions.\n\n"
        "When user provides just an amount and currency (e.g., '1000 dollars', 'convert to pkr'), "
        "understand the context and perform the conversion. Common conversions:\n"
        "- USD to PKR (Pakistani Rupees)\n"
        "- USD to INR (Indian Rupees)\n"
        "- USD to EUR, GBP, etc.\n\n"
        "Always show the calculation clearly."
    ),
    tools=[currency_converter],
    model_settings=create_model_settings()
)

# ==================== TRIAGE AGENT ====================

triage_agent = Agent(
    name="Finance Assistant",
    instructions=(
        "You are a financial assistant triage agent. Your ONLY job is to route requests to specialists.\n\n"
        "Routing rules:\n"
        "- Stock prices, stock analysis, ticker symbols (AAPL, GOOGL, TSLA, NVDA, MSFT, etc.) → Handoff to 'Stock Analyst'\n"
        "- Portfolio analysis, investment returns, risk assessment → Handoff to 'Portfolio Manager'\n"
        "- Market news, market trends, sector analysis → Handoff to 'Market Intelligence Analyst'\n"
        "- Currency conversion, forex, international markets → Handoff to 'Currency Specialist'\n\n"
        "CRITICAL: You MUST handoff to the appropriate specialist. Do NOT answer questions yourself."
    ),
    handoffs=[stock_agent, portfolio_agent, market_agent, currency_agent],
    model_settings=create_model_settings()
)


# ==================== API CONFIGURATION ====================

def get_api_key():
    """
    Get API key from environment with fallback.
    Priority: OPENAI_API_KEY (OpenRouter) > GOOGLE_API_KEY
    """
    # Check for OpenRouter key first (sk-or-v1-...)
    openrouter_key = os.getenv("OPENAI_API_KEY", "")
    google_key = os.getenv("GOOGLE_API_KEY")

    # Prioritize OpenRouter key since it works with OpenAI Agents SDK
    if openrouter_key and openrouter_key.startswith("sk-or-v1-"):
        print("✅ Using OpenRouter (Google Gemini via OpenRouter) - FREE")
        return openrouter_key, "openrouter"
    elif openai_key:
        print("✅ Using OpenAI API")
        return openai_key, "openai"
    elif google_key:
        print("✅ Using Google AI Studio (via OpenRouter)")
        # For Google keys, we need to use them through OpenRouter
        return google_key, "google"
    else:
        print("⚠️  No API key found!")
        print("   Get FREE OpenRouter key from: https://openrouter.ai/keys")
        print("   Add to .env file: OPENAI_API_KEY=your-key-here")
        return None, "none"


def configure_openai_client():
    """
    Configure OpenAI client with OpenRouter for Google Gemini compatibility.
    This allows using Google Gemini models via OpenRouter with OpenAI Agents SDK.
    """
    openrouter_key = os.getenv("OPENAI_API_KEY", "")
    base_url = os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1")

    # Only configure if we have an OpenRouter key
    if openrouter_key and openrouter_key.startswith("sk-or-v1-"):
        print(f"🔧 Configuring OpenAI SDK with OpenRouter")
        print(f"   Base URL: {base_url}")
        print(f"   Model: google/gemini-2.0-flash-exp:free")

        os.environ["OPENAI_API_KEY"] = openrouter_key
        os.environ["OPENAI_BASE_URL"] = base_url

        return True
    return False


# ==================== MAIN EXECUTION ====================

async def run_finance_agent(query: str, session: SQLiteSession = None):
    """Main function to run the finance agent with a user query."""
    try:
        # Check for API key
        api_key, provider = get_api_key()
        if not api_key:
            return "⚠️  Error: No API key configured. Please add OPENAI_API_KEY to .env file."

        # Configure client based on provider
        if provider == "openrouter":
            # Configure for OpenRouter (Google Gemini via OpenRouter)
            configure_openai_client()
        elif provider == "google":
            # Google key via OpenRouter
            configure_openai_client()
        elif provider == "openai":
            # Direct OpenAI API
            os.environ["OPENAI_API_KEY"] = api_key

        # Manual routing based on query keywords (since handoffs don't work well with OpenRouter)
        query_lower = query.lower()

        # Stock-related keywords
        stock_keywords = ['stock', 'price', 'aapl', 'googl', 'tsla', 'nvda', 'msft', 'amzn',
                         'meta', 'ticker', 'shares', 'equity', 'analysis']

        # Portfolio-related keywords
        portfolio_keywords = ['portfolio', 'investment', 'returns', 'risk', 'diversification',
                             'holdings', 'asset', 'allocation']

        # Market news keywords
        news_keywords = ['news', 'market', 'trends', 'sector', 'update', 'latest', 'breaking']

        # Currency keywords
        currency_keywords = ['currency', 'forex', 'convert', 'exchange rate', 'eur', 'gbp', 'jpy',
                           'usd', 'international', 'pkr', 'rupees', 'pakistan', 'inr', 'cny',
                           'cad', 'aud', 'chf', 'aed', 'sar', 'subtract', 'add', 'multiply']

        # Math/calculation keywords
        math_keywords = ['subtract', 'add', 'multiply', 'divide', 'percent', '%', 'calculate']

        # Route to appropriate agent
        if any(keyword in query_lower for keyword in math_keywords):
            # Math operations - use currency agent for calculations with money
            target_agent = currency_agent
        elif any(keyword in query_lower for keyword in stock_keywords):
            target_agent = stock_agent
        elif any(keyword in query_lower for keyword in portfolio_keywords):
            target_agent = portfolio_agent
        elif any(keyword in query_lower for keyword in news_keywords):
            target_agent = market_agent
        elif any(keyword in query_lower for keyword in currency_keywords):
            target_agent = currency_agent
        else:
            # Default to triage
            target_agent = triage_agent

        # Run with session if provided (for conversation memory)
        if session:
            result = await Runner.run(target_agent, query, session=session)
        else:
            result = await Runner.run(target_agent, query)

        return result.final_output

    except Exception as e:
        error_msg = str(e)
        # Handle specific errors with helpful messages
        if "401" in error_msg or "User not found" in error_msg:
            return "⚠️ API Error: Unable to connect to the service. This might be due to rate limiting on the free tier. Please wait a moment and try again."
        elif "429" in error_msg or "rate limit" in error_msg.lower():
            return "⚠️ Rate Limit: Too many requests. Please wait a moment and try again."
        elif "402" in error_msg:
            return "⚠️ Token Limit: Request too large. Please try a shorter query."
        else:
            return f"⚠️ Error: {error_msg}"


# ==================== CLI INTERFACE ====================

async def main():
    """Interactive CLI for the Finance Agent."""
    # Disable tracing to avoid API key validation errors with OpenRouter
    import sys
    if 'OPENAI_AGENTS_DISABLE_TRACING' not in os.environ:
        os.environ['OPENAI_AGENTS_DISABLE_TRACING'] = '1'

    # Create session for conversation memory
    # Each conversation session is stored in SQLite database
    session = SQLiteSession("finance_conversation")

    print("🤖 Finance Agent - Powered by OpenAI Agents SDK")
    print("=" * 50)
    print("I can help you with:")
    print("📊 Stock analysis and prices")
    print("💼 Portfolio management and performance")
    print("📈 Market news and trends")
    print("💱 Currency conversion")
    print("⚠️ Risk assessment")
    print("\n✨ Conversation memory enabled - I remember our discussion!")
    print("Type 'quit' to exit or ask your financial question!")
    print("=" * 50)

    while True:
        try:
            user_input = input("\n💬 Your question: ").strip()

            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Goodbye! 👋")
                break

            if not user_input:
                continue

            print("\n🤔 Processing your request...")
            # Pass session to maintain conversation context
            response = await run_finance_agent(user_input, session=session)
            print(f"\n📝 Answer:\n{response}")

        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    # Example usage
    asyncio.run(main())