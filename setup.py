#!/usr/bin/env python3
"""
Setup script for Finance Agent - helps users get started quickly
"""

import os
import sys
import subprocess
import platform


def print_banner():
    """Print a welcome banner."""
    print("""
    🤖 Finance Agent Setup
    ======================
    Powered by OpenAI Agents SDK

    A multi-agent financial assistant for:
    📊 Stock Analysis
    💼 Portfolio Management
    📈 Market Intelligence
    💱 Currency Conversion
    ⚠️  Risk Assessment

    Let's get you started! 🚀
    """)


def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Error: Python 3.8+ required. You have {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True


def install_dependencies():
    """Install required dependencies."""
    print("\n📦 Installing dependencies...")

    try:
        # Try to use pip from the same Python interpreter
        pip_cmd = [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]

        result = subprocess.run(pip_cmd, capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ Dependencies installed successfully!")
            return True
        else:
            print(f"❌ Installation failed: {result.stderr}")
            return False

    except Exception as e:
        print(f"❌ Error during installation: {e}")
        return False


def setup_openai_key():
    """Guide user to set up OpenAI API key (optional for testing)."""
    print("\n🔑 OpenAI API Key Setup")
    print("-" * 30)

    print("The finance agent can run without an API key using simulated data.")
    print("For production use with real financial data, you'll need:")
    print("1. An OpenAI account at https://platform.openai.com")
    print("2. API key from https://platform.openai.com/api-keys")
    print("3. Add funds to your account")

    choice = input("\nWould you like to set up your OpenAI API key now? (y/n): ").strip().lower()

    if choice in ['y', 'yes']:
        api_key = input("Enter your OpenAI API key (sk-...): ").strip()

        if api_key.startswith("sk-") and len(api_key) > 20:
            # Set environment variable (temporary - for current session)
            os.environ["OPENAI_API_KEY"] = api_key

            # Offer to save to .env file
            save_choice = input("Save to .env file for future use? (y/n): ").strip().lower()

            if save_choice in ['y', 'yes']:
                try:
                    with open(".env", "a") as f:
                        f.write(f"\nOPENAI_API_KEY={api_key}\n")
                    print("✅ API key saved to .env file")
                except Exception as e:
                    print(f"⚠️  Could not save to .env: {e}")

            print("✅ OpenAI API key set for this session!")
            return True
        else:
            print("❌ Invalid API key format. Should start with 'sk-'")
            return False
    else:
        print("ℹ️  You can set up the API key later by:")
        print("   - Setting OPENAI_API_KEY environment variable")
        print("   - Creating a .env file with: OPENAI_API_KEY=your_key")
        return True


def create_test_script():
    """Create a simple test script for quick verification."""
    test_content = '''#!/usr/bin/env python3
"""
Quick test script to verify the Finance Agent is working
"""

import asyncio
from finance_agent import run_finance_agent

async def quick_test():
    print("🧪 Quick Finance Agent Test")
    print("=" * 30)

    # Test 1: Simple stock query
    print("\\nTest 1: Stock price check...")
    result1 = await run_finance_agent("What's the current price of AAPL?")
    print(f"Result: {str(result1)[:80]}...")

    # Test 2: Portfolio analysis
    print("\\nTest 2: Portfolio analysis...")
    result2 = await run_finance_agent("Analyze portfolio with 50 MSFT at $300")
    print(f"Result: {str(result2)[:80]}...")

    print("\\n✅ Tests completed!")

if __name__ == "__main__":
    asyncio.run(quick_test())
'''

    try:
        with open("quick_test.py", "w") as f:
            f.write(test_content)
        print("✅ Created quick_test.py")
    except Exception as e:
        print(f"⚠️  Could not create quick_test.py: {e}")


def create_bash_script():
    """Create a bash script for easy execution on Linux/Mac."""
    bash_content = '''#!/bin/bash
# Finance Agent Launcher

echo "🤖 Finance Agent - Starting..."
echo "=============================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 not found"
    exit 1
fi

# Run the main application
python3 finance_agent.py
'''

    try:
        with open("run_finance_agent.sh", "w") as f:
            f.write(bash_content)

        # Make executable
        os.chmod("run_finance_agent.sh", 0o755)
        print("✅ Created run_finance_agent.sh (executable)")

    except Exception as e:
        print(f"⚠️  Could not create bash script: {e}")


def create_windows_batch():
    """Create a Windows batch file."""
    batch_content = '''@echo off
REM Finance Agent Launcher for Windows

echo ==============================
echo    Finance Agent - Starting
echo ==============================

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python not found
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

REM Run the main application
python finance_agent.py

pause
'''

    try:
        with open("run_finance_agent.bat", "w") as f:
            f.write(batch_content)
        print("✅ Created run_finance_agent.bat")
    except Exception as e:
        print(f"⚠️  Could not create batch file: {e}")


def display_next_steps():
    """Display what to do next."""
    print("\n🎉 Setup Complete!")
    print("=" * 40)

    print("\nNext steps:")
    print("1. 🧪 Test the installation:")
    print("   python finance_agent.py")
    print("   (or: python quick_test.py for a quick test)")

    print("\n2. 📊 Try some examples:")
    print("   - 'What's the current price of AAPL?'")
    print("   - 'Analyze my portfolio with 100 AAPL at $150'")
    print("   - 'What's the latest market news?'")

    print("\n3. 📖 Explore the examples:")
    print("   python example_usage.py")

    print("\n4. 🔧 Advanced usage:")
    print("   - Check out README.md for full documentation")
    print("   - Run test suite: python test_finance_agent.py")
    print("   - Customize finance_agent.py for your needs")

    print("\n5. 🚀 Need more features?")
    print("   - Add real financial APIs in finance_agent.py")
    print("   - Extend with new tools and agents")
    print("   - Integrate with your existing systems")

    print("\n📁 Project structure:")
    print("   finance_agent.py    - Main agent implementation")
    print("   example_usage.py    - Usage examples")
    print("   test_finance_agent.py - Test suite")
    print("   quick_test.py       - Quick verification")
    print("   requirements.txt    - Dependencies")
    print("   README.md          - Full documentation")


def main():
    """Main setup function."""
    print_banner()

    if not check_python_version():
        return

    # Check if files already exist
    existing_files = []
    required_files = ["finance_agent.py", "requirements.txt", "README.md"]

    for file in required_files:
        if os.path.exists(file):
            existing_files.append(file)

    if existing_files:
        print(f"\n⚠️  Found existing files: {', '.join(existing_files)}")
        overwrite = input("Continue setup? (y/n): ").strip().lower()
        if overwrite not in ['y', 'yes']:
            print("Setup cancelled.")
            return

    print("\n" + "=" * 50)
    print("SETUP PROCESS")
    print("=" * 50)

    # Install dependencies
    deps_success = install_dependencies()

    if not deps_success:
        print("\n❌ Dependency installation failed.")
        print("You can try manually: pip install -r requirements.txt")
        return

    # Setup API key
    api_success = setup_openai_key()

    # Create helper scripts
    print("\n🔧 Creating helper scripts...")
    create_test_script()
    create_bash_script()
    create_windows_batch()

    # Display next steps
    display_next_steps()

    print("\n" + "=" * 50)
    print("✅ Setup completed successfully!")
    print("Happy financial analyzing! 📊💰")
    print("=" * 50)


if __name__ == "__main__":
    main()