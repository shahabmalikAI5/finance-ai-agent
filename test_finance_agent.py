#!/usr/bin/env python3
"""
Simple test script to verify the Finance Agent functionality
"""

import asyncio
import sys
from finance_agent import run_finance_agent


async def test_basic_functionality():
    """Test basic agent functionality with simple queries."""
    print("🧪 Testing Finance Agent Basic Functionality")
    print("=" * 50)

    test_cases = [
        {
            "name": "Stock Price Query",
            "query": "What's the current price of AAPL?",
            "expected_in_response": ["AAPL", "price", "dollar"]
        },
        {
            "name": "Portfolio Analysis",
            "query": "Analyze my portfolio with 50 shares of MSFT at $300",
            "expected_in_response": ["portfolio", "value", "analysis"]
        },
        {
            "name": "Market News",
            "query": "What's the latest market news?",
            "expected_in_response": ["news", "market", "headline"]
        },
        {
            "name": "Currency Conversion",
            "query": "Convert 100 USD to EUR",
            "expected_in_response": ["USD", "EUR", "conversion"]
        }
    ]

    success_count = 0
    total_tests = len(test_cases)

    for test in test_cases:
        print(f"\n📋 Test: {test['name']}")
        print(f"❓ Query: {test['query']}")

        try:
            response = await run_finance_agent(test['query'])

            if response:
                response_lower = str(response).lower()

                # Check if expected keywords are in response
                found_keywords = []
                for keyword in test['expected_in_response']:
                    if keyword.lower() in response_lower:
                        found_keywords.append(keyword)

                if found_keywords:
                    print(f"✅ PASS - Found keywords: {found_keywords}")
                    print(f"📝 Response: {str(response)[:100]}...")
                    success_count += 1
                else:
                    print(f"❌ FAIL - Missing expected keywords")
                    print(f"📝 Response: {str(response)[:100]}...")
            else:
                print(f"❌ FAIL - No response received")

        except Exception as e:
            print(f"❌ ERROR - {type(e).__name__}: {str(e)}")

    print(f"\n🎯 Results: {success_count}/{total_tests} tests passed")
    return success_count == total_tests


async def test_error_handling():
    """Test how the agent handles edge cases."""
    print("\n🧪 Testing Error Handling")
    print("=" * 30)

    edge_cases = [
        "This is a completely unrelated query about cooking recipes",
        "",
        "A" * 1000,  # Very long query
        "What is the meaning of life, the universe, and everything?",
    ]

    for i, query in enumerate(edge_cases, 1):
        print(f"\n📋 Edge Case {i}: {query[:50]}{'...' if len(query) > 50 else ''}")
        try:
            response = await run_finance_agent(query)
            print(f"✅ Handled gracefully: {str(response)[:100]}...")
        except Exception as e:
            print(f"❌ Exception: {type(e).__name__}: {str(e)}")


async def test_structured_queries():
    """Test more complex, structured queries."""
    print("\n🧪 Testing Structured Queries")
    print("=" * 35)

    complex_queries = [
        "Get current prices for Apple (AAPL) and Microsoft (MSFT)",
        "Calculate returns for a $10000 investment now worth $15000 over 3 years",
        "Assess portfolio risk with beta 1.2, volatility 20%, diversification score 7",
        "Analyze my portfolio: 100 AAPL at $150, 50 MSFT at $300",
    ]

    for i, query in enumerate(complex_queries, 1):
        print(f"\n📋 Complex Query {i}: {query}")
        try:
            response = await run_finance_agent(query)
            if response and len(str(response)) > 10:
                print(f"✅ Success: {str(response)[:150]}...")
            else:
                print(f"⚠️  Minimal response: {str(response)}")
        except Exception as e:
            print(f"❌ Error: {type(e).__name__}: {str(e)}")


async def benchmark_performance():
    """Simple performance test."""
    print("\n⏱️  Performance Test")
    print("=" * 20)

    import time

    queries = [
        "Get stock price for AAPL",
        "Analyze portfolio with 100 AAPL at $150",
        "What's the latest market news?"
    ]

    total_time = 0

    for i, query in enumerate(queries, 1):
        print(f"\nTest {i}: {query}")
        start_time = time.time()

        try:
            response = await run_finance_agent(query)
            end_time = time.time()
            elapsed = end_time - start_time
            total_time += elapsed

            print(f"✅ Completed in {elapsed:.2f}s")
            print(f"📝 Response length: {len(str(response))} chars")
        except Exception as e:
            print(f"❌ Failed: {e}")

    print(f"\n📊 Performance Summary:")
    print(f"   Total time: {total_time:.2f}s")
    print(f"   Average per query: {total_time/len(queries):.2f}s")


async def main():
    """Main test runner."""
    print("🚀 Finance Agent Test Suite")
    print("=" * 40)

    while True:
        print("\nSelect test to run:")
        print("1. Basic Functionality Test")
        print("2. Error Handling Test")
        print("3. Structured Queries Test")
        print("4. Performance Benchmark")
        print("5. Run All Tests")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ").strip()

        if choice == "1":
            await test_basic_functionality()
        elif choice == "2":
            await test_error_handling()
        elif choice == "3":
            await test_structured_queries()
        elif choice == "4":
            await benchmark_performance()
        elif choice == "5":
            print("\n" + "="*50)
            print("RUNNING COMPLETE TEST SUITE")
            print("="*50)

            all_passed = await test_basic_functionality()
            await test_error_handling()
            await test_structured_queries()
            await benchmark_performance()

            print(f"\n🎯 Overall Result: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")

        elif choice == "6":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please select 1-6.")

        if choice != "6":
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    # Check for OpenAI API key
    import os
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Warning: OPENAI_API_KEY environment variable not set.")
        print("   The agent will still work with simulated data for testing.")
        print("   For production use, set OPENAI_API_KEY with your actual key.")

    # Run tests
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\nTest suite interrupted. Goodbye! 👋")
    except Exception as e:
        print(f"\n❌ Unexpected error: {type(e).__name__}: {e}")
        sys.exit(1)