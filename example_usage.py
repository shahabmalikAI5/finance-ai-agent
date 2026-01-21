#!/usr/bin/env python3
"""
Example usage and test scenarios for the Finance Agent
"""

import asyncio
import json
from finance_agent import run_finance_agent


async def demonstrate_capabilities():
    """Demonstrate various capabilities of the finance agent."""

    print("🚀 Finance Agent - Capability Demonstration")
    print("=" * 60)

    # Example 1: Stock Analysis
    print("\n📊 1. STOCK ANALYSIS")
    print("-" * 30)
    stock_queries = [
        "What's the current price of Apple stock (AAPL)?",
        "Get stock price for Tesla (TSLA)",
        "Analyze Google stock performance (GOOGL)"
    ]

    for query in stock_queries:
        print(f"\n❓ Question: {query}")
        response = await run_finance_agent(query)
        print(f"📝 Answer: {response}")

    # Example 2: Portfolio Analysis
    print("\n💼 2. PORTFOLIO ANALYSIS")
    print("-" * 30)

    portfolio_query = """
    Analyze my investment portfolio with these holdings:
    - 100 shares of AAPL bought at $150
    - 50 shares of MSFT bought at $300
    - 25 shares of GOOGL bought at $2800
    """
    print(f"\n❓ Question: {portfolio_query}")
    response = await run_finance_agent(portfolio_query)
    print(f"📝 Answer: {response}")

    # Example 3: Investment Returns
    print("\n📈 3. INVESTMENT RETURNS")
    print("-" * 30)

    returns_queries = [
        "Calculate my returns: invested $10000, now worth $15000 over 3 years",
        "What's the CAGR if I turned $5000 into $8000 in 2 years?"
    ]

    for query in returns_queries:
        print(f"\n❓ Question: {query}")
        response = await run_finance_agent(query)
        print(f"📝 Answer: {response}")

    # Example 4: Market Intelligence
    print("\n📰 4. MARKET INTELLIGENCE")
    print("-" * 30)

    market_queries = [
        "What's the latest market news?",
        "Give me recent tech sector updates",
        "Latest cryptocurrency news and trends"
    ]

    for query in market_queries:
        print(f"\n❓ Question: {query}")
        response = await run_finance_agent(query)
        print(f"📝 Answer: {response}")

    # Example 5: Currency & International Markets
    print("\n💱 5. CURRENCY & INTERNATIONAL")
    print("-" * 30)

    currency_queries = [
        "Convert 1000 USD to EUR",
        "How much is 500 GBP in JPY?",
        "Currency conversion for international investment analysis"
    ]

    for query in currency_queries:
        print(f"\n❓ Question: {query}")
        response = await run_finance_agent(query)
        print(f"📝 Answer: {response}")

    # Example 6: Risk Assessment
    print("\n⚠️ 6. RISK ASSESSMENT")
    print("-" * 30)

    risk_queries = [
        "Assess my portfolio risk: beta 1.2, volatility 20%, diversification score 6",
        "Evaluate risk for high-beta portfolio with 25% volatility",
        "Risk analysis for conservative portfolio"
    ]

    for query in risk_queries:
        print(f"\n❓ Question: {query}")
        response = await run_finance_agent(query)
        print(f"📝 Answer: {response}")

    # Example 7: Complex Multi-Part Queries
    print("\n🧩 7. COMPLEX MULTI-PART QUERIES")
    print("-" * 30)

    complex_queries = [
        """
        I have a portfolio with AAPL (100 shares at $150) and MSFT (50 shares at $300).
        First analyze the portfolio performance, then assess the risk level,
        and suggest improvements.
        """,
        """
        Get current prices for Apple, Google, and Microsoft stocks.
        Then explain which looks most attractive for investment.
        """
    ]

    for query in complex_queries:
        print(f"\n❓ Complex Question: {query.strip()}")
        response = await run_finance_agent(query)
        print(f"📝 Answer: {response}")


async def quick_test():
    """Quick test to verify basic functionality."""
    print("\n🧪 Quick Functionality Test")
    print("=" * 40)

    test_cases = [
        "Stock price for AAPL",
        "Analyze portfolio with 50 MSFT at $300",
        "Latest market news",
        "Convert 100 USD to EUR",
        "Assess risk with beta 1.1, volatility 15%, diversification 8"
    ]

    for i, query in enumerate(test_cases, 1):
        print(f"\nTest {i}/{len(test_cases)}: {query}")
        try:
            response = await run_finance_agent(query)
            if response and len(str(response)) > 0:
                print(f"✅ Success: {str(response)[:100]}...")
            else:
                print(f"❌ No response")
        except Exception as e:
            print(f"❌ Error: {str(e)}")


async def financial_planning_scenario():
    """Complete financial planning scenario."""
    print("\n💰 COMPLETE FINANCIAL PLANNING SCENARIO")
    print("=" * 50)

    scenario = """
    Imagine you're a financial advisor helping a client. The client has:
    - Current portfolio value: $75,000
    - Initial investment: $50,000 (3 years ago)
    - Holdings: 150 AAPL @ $180, 80 MSFT @ $320, 30 NVDA @ $450
    - Risk tolerance: Medium (beta 1.1, volatility 18%)

    Tasks:
    1. Analyze current portfolio performance
    2. Calculate overall returns and CAGR
    3. Assess risk level and provide recommendations
    4. Get latest market news that might affect the portfolio
    5. Suggest potential improvements

    Provide a comprehensive financial analysis report.
    """

    print(f"\n📋 Scenario: {scenario}")
    print("\n🤖 Agent Analysis:")
    response = await run_finance_agent(scenario)
    print(f"\n📊 Comprehensive Report:\n{response}")


async def main():
    """Main demonstration function."""
    print("🤖 Finance Agent - Complete Demonstration")
    print("Powered by OpenAI Agents SDK")
    print("=" * 60)

    while True:
        print("\n\nChoose a demonstration:")
        print("1. 📊 Complete Capability Demo (All Examples)")
        print("2. 🧪 Quick Functionality Test")
        print("3. 💰 Financial Planning Scenario")
        print("4. ❓ Ask Your Own Question")
        print("5. 🚀 Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            await demonstrate_capabilities()
        elif choice == "2":
            await quick_test()
        elif choice == "3":
            await financial_planning_scenario()
        elif choice == "4":
            custom_query = input("\nEnter your financial question: ").strip()
            if custom_query:
                response = await run_finance_agent(custom_query)
                print(f"\n📝 Response:\n{response}")
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please select 1-5.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    # Run specific demonstrations
    print("Select demonstration mode:")
    print("1. Full demo with all examples")
    print("2. Quick test only")
    mode = input("Enter choice (1 or 2): ").strip()

    if mode == "2":
        asyncio.run(quick_test())
    else:
        asyncio.run(main())