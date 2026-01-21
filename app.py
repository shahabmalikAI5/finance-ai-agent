"""
Finance Agent Web Interface - Streamlit
A beautiful chat interface for the Finance Agent using Streamlit
"""

import streamlit as st
import asyncio
import os
import sys
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import finance agent AFTER setting up path
from finance_agent import run_finance_agent, SQLiteSession

# Ensure .env is loaded
from dotenv import load_dotenv
load_dotenv()

# ==================== PAGE CONFIGURATION ====================

st.set_page_config(
    page_title="Finance Agent | AI-Powered Financial Assistant",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS ====================

st.markdown("""
<style>
    /* ============================================
       Finance Agent UI Styles - High Contrast Dark Theme
       Creator: SHAHAB MALIK
       ============================================ */

    /* ==================== PAGE BACKGROUND ====================
       'e8eaed' - Light gray color for the overall page background
       Yeh poore page ka background color hai (chat area ke bahar wala hissa)
    */
    .main {
        background-color: #e8eaed !important;
    }

    .main .block-container {
        background-color: #e8eaed !important;
        padding: 20px !important;
    }

    /* ==================== CHAT MESSAGES ====================
       User aur assistant ke messages ka styling
    */

    .stChatMessage {
        background-color: transparent !important;
        border-radius: 12px;
        padding: 12px 16px;
        margin-bottom: 16px;
    }

    /* USER MESSAGES (Right side) -
       '4a5568' - Dark gray/slate color for user message background
       'ffffff' - White text color for readability
       Messages right side mein appear hote hain
    */
    .stChatMessage[data-testid="user-message"] {
        background-color: #4a5568 !important;
        color: #ffffff !important;
        border-radius: 12px;
        margin-left: auto;
        max-width: 70%;
        float: right;
        clear: both;
    }

    /* ASSISTANT MESSAGES (Left side) -
       'ffffff' - Pure white background for AI responses
       '1a202c' - Very dark text color for contrast
       'cbd5e0' - Light gray border around messages
       Messages left side mein appear hote hain
    */
    .stChatMessage[data-testid="assistant-message"] {
        background-color: #ffffff !important;
        color: #1a202c !important;
        border: 1px solid #cbd5e0 !important;
        border-radius: 12px;
        margin-right: auto;
        max-width: 85%;
        float: left;
        clear: both;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    /* ==================== HEADER SECTION ====================
       '2d3748' - Dark slate gray background for header
       'ffffff' - White text for main heading
       'e2e8f0' - Light gray text for subtext
       Top heading area "🤖 Finance Agent" wali jagah
    */
    .main-header {
        text-align: center;
        padding: 24px 20px;
        background: #2d3748;
        color: #ffffff;
        border-radius: 12px;
        margin-bottom: 24px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        position: relative;
    }

    .main-header h1 {
        color: #ffffff !important;
        font-size: 28px !important;
        font-weight: 600 !important;
        margin-bottom: 8px !important;
    }

    .main-header p {
        color: #e2e8f0 !important;
    }

    /* Creator credit - "Created By: SHAHAB MALIK"
       'a0aec0' - Muted gray color for creator name
       Bottom right corner mein appear hota hai
       Font weight increased to 700 (Bold)
    */
    .creator-credit {
        position: absolute;
        bottom: 8px;
        right: 15px;
        font-size: 13px;
        color: #ffffff !important;
        font-weight: 700;
        text-shadow: 0 1px 2px rgba(0,0,0,0.3);
    }

    /* ==================== SIDEBAR ====================
       'ffffff' - White background for sidebar panels
       '1a202c' - Dark text color
       'e2e8f0' - Light gray border
       Left side mein buttons aur settings wali jagah
    */
    .sidebar-info {
        background-color: #ffffff;
        color: #1a202c;
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 16px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border: 1px solid #e2e8f0;
    }

    /* ==================== CHAT INPUT BOX ====================
       BLACK THEME - Highly visible input area at bottom
       "Ask your finance question..." wali jagah
    */

    /* CONTAINER (Bahar ka box) -
       '1a1a1a' - Almost black color for outer container
       '000000' - Pure black border (3px thick)
       Yeh textarea ke bahar ka wrapper box hai
    */
    .stChatInputContainer {
        background-color: #1a1a1a !important;
        border: 3px solid #000000 !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4) !important;
        margin: 16px 0 !important;
    }

    /* TEXTAREA (Andar jahan hum type karte hain) -
       '000000' - Pure black background for typing area
       'ffffff' - White text color for maximum contrast
       '333333' - Dark gray border around typing area
       '15px' - Font size for text
       Yeh actual input field hai jahan user type karta hai
    */
    .stChatInputContainer textarea {
        background-color: #000000 !important;
        color: #ffffff !important;
        border: 2px solid #333333 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        padding: 10px 12px !important;
        line-height: 1.5 !important;
        border-radius: 8px !important;
    }

    /* FOCUS STATE (Jab user click karta hai) -
       '0a0a0a' - Even darker black when focused
       '666666' - Medium gray border when typing
       White glow effect around input
    */
    .stChatInputContainer textarea:focus {
        background-color: #0a0a0a !important;
        border-color: #666666 !important;
        box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.1) !important;
        outline: none !important;
    }

    /* PLACEHOLDER TEXT ("Ask your finance question...") -
       '000000' - Medium gray color for placeholder
       Placeholder wo text hai jo type se pehle dikhta hai
    */
    .stChatInputContainer textarea::placeholder {
        color: grey !important;
        font-weight: 600 !important;
    }

    /* ==================== APP BASE ====================
       Overall application background
    */
    .stApp {
        background-color: #e8eaed !important;
    }

    /* ==================== TEXT COLOR FIX ====================
       Ensure proper text colors in messages
    */
    .stChatMessage p {
        color: inherit !important;
    }

    /* User message text - White color */
    .stChatMessage[data-testid="user-message"] p {
        color: #ffffff !important;
    }

    /* Assistant message text - Dark color */
    .stChatMessage[data-testid="assistant-message"] p {
        color: #1a202c !important;
    }

    /* ==================== FORCE CSS - MORE SPECIFIC SELECTORS ====================
       Streamlit ke liye more specific selectors for better CSS application
    */

    /* Target the input container using data-testid attribute */
    div[data-testid="stChatInputContainer"] {
        background-color: #1a1a1a !important;
        border: 3px solid #000000 !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4) !important;
        margin: 16px 0 !important;
    }

    div[data-testid="stChatInputContainer"] textarea {
        background-color: #000000 !important;
        color: #ffffff !important;
        border: 2px solid #333333 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        padding: 10px 12px !important;
        line-height: 1.5 !important;
        border-radius: 8px !important;
    }

    div[data-testid="stChatInputContainer"] textarea:focus {
        background-color: #0a0a0a !important;
        border-color: #666666 !important;
        box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.1) !important;
        outline: none !important;
    }

    div[data-testid="stChatInputContainer"] textarea::placeholder {
        color: #a0a0a0 !important;
        font-weight: 600 !important;
    }

    /* ==================== TARGET STREAMLIT CSS CLASSES ====================
       Streamlit uses internal CSS classes like .st-c5 for textarea background
       Yeh classes ko directly target kar rahe hain
    */

    /* .st-c5 is the textarea background class */
    .st-c5 {
        background-color: #d3d3d3 !important;
        background: #d3d3d3 !important;
    }

    /* Force light gray on all textarea elements */
    textarea.st-c5,
    .stChatInputContainer textarea,
    div[data-testid="stChatInputContainer"] textarea {
        background-color: #d3d3d3 !important;
        background: #d3d3d3 !important;
    }

    /* Target the specific Streamlit input element classes */
    .st-cj.st-c5 {
        background-color: #d3d3d3 !important;
    }

    /* More specific - using combined classes */
    textarea[data-testid="stChatInputTextArea"] {
        background-color: #d3d3d3 !important;
        color: #1a202c !important;
        border: 2px solid #a0a0a0 !important;
    }
</style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================

with st.sidebar:
    st.image("https://img.icons8.com/color/96/finance.png", width=100)

    st.title("⚙️ Settings")

    # Session info
    st.markdown("### 📊 Session Info")
    if "session" not in st.session_state:
        st.session_state.session = SQLiteSession(f"web_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
    st.success("✅ Session Active")
    st.info(f"🆔 Session: finance_agent_web")

    st.markdown("---")

    # Features
    st.markdown("### ✨ Features")
    st.markdown("""
    - 📈 Stock Prices
    - 💱 Currency Conversion
    - 💼 Portfolio Analysis
    - 📰 Market News
    - 🧠 Memory Enabled
    """)

    st.markdown("---")

    # Example questions
    st.markdown("### 💡 Example Questions")
    examples = [
        "What's Apple's stock price?",
        "Convert 100 USD to PKR",
        "Show me Tesla stock",
        "Latest market news",
        "Investment calculator"
    ]

    for example in examples:
        if st.button(example, key=example, use_container_width=True):
            st.session_state.example_question = example

    st.markdown("---")

    # Clear chat button
    if st.button("🗑️ Clear Chat History", use_container_width=True, type="secondary"):
        st.session_state.messages = []
        st.rerun()

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; font-size: 12px; color: #666;'>
    Made with ❤️ using<br>
    OpenAI Agents SDK + Streamlit<br>
    Powered by Google Gemini via OpenRouter
    </div>
    """, unsafe_allow_html=True)

# ==================== MAIN AREA ====================

# Debug info (collapsible)
with st.expander("🔧 Debug Info"):
    st.write(f"**Model:** {os.getenv('OPENAI_MODEL', 'Not set')}")
    st.write(f"**Base URL:** {os.getenv('OPENAI_BASE_URL', 'Not set')}")
    st.write(f"**API Key:** {'✅ Set' if os.getenv('OPENAI_API_KEY') else '❌ Missing'}")
    st.write(f"**Max Tokens:** 2000")

# Header
st.markdown("""
<div class="main-header">
    <h1>🤖 Finance Agent</h1>
    <p style='font-size: 14px; margin: 8px 0 0 0;'>Your AI-Powered Financial Assistant</p>
    <p style='font-size: 13px; margin: 4px 0 0 0; opacity: 0.7;'>
    Ask about stocks, currency, investments, market news & more!
    </p>
    <div class="creator-credit">Created By: SHAHAB MALIK</div>
</div>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display welcome message if no messages
if len(st.session_state.messages) == 0:
    st.markdown("""
    <div style='text-align: center; padding: 40px; background-color: #f8f9fa; border-radius: 10px; margin-bottom: 20px;'>
        <h2>👋 Welcome to Finance Agent!</h2>
        <p style='font-size: 16px; color: #666;'>
            I can help you with stock prices, currency conversion, portfolio analysis, and market news.<br>
            Just ask your question below!
        </p>
    </div>
    """, unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input - ALWAYS show at the bottom
user_input = st.chat_input(
    "💬 Ask your finance question...",
    accept_file=False,
    key="chat_input"
)

# Handle example question from sidebar (if any)
# This processes example questions immediately
if "example_question" in st.session_state and st.session_state.example_question:
    example_q = st.session_state.example_question
    del st.session_state.example_question

    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": example_q})

    # Display user message
    with st.chat_message("user"):
        st.markdown(example_q)

    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            try:
                # Disable tracing for web interface
                os.environ['OPENAI_AGENTS_DISABLE_TRACING'] = '1'

                # Get response from finance agent
                response = asyncio.run(
                    run_finance_agent(example_q, session=st.session_state.session)
                )

                # Check if response is an error message
                if "⚠️" in response and ("Token Limit" in response or "API Error" in response):
                    st.warning(response)
                else:
                    # Display response
                    st.markdown(response)

                # Add to message history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })

                # Rerun to show updated chat with input still visible
                st.rerun()

            except Exception as e:
                error_msg = str(e)

                # Provide helpful error messages
                if "402" in error_msg or "token" in error_msg.lower():
                    error_msg = "⚠️ **Token Limit Error**: The request was too large. Please try a shorter query."

                elif "401" in error_msg or "authentication" in error_msg.lower():
                    error_msg = "⚠️ **Authentication Error**: Please check your API key in the .env file."

                elif "429" in error_msg or "rate limit" in error_msg.lower():
                    error_msg = "⚠️ **Rate Limit**: Too many requests. Please wait a moment and try again."

                else:
                    error_msg = f"❌ **Error**: {error_msg}"

                st.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg
                })
                st.rerun()

# Process manual user input (if we have one and not from example)
if user_input:
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            try:
                # Disable tracing for web interface
                os.environ['OPENAI_AGENTS_DISABLE_TRACING'] = '1'

                # Get response from finance agent
                response = asyncio.run(
                    run_finance_agent(user_input, session=st.session_state.session)
                )

                # Check if response is an error message
                if "⚠️" in response and ("Token Limit" in response or "API Error" in response):
                    st.warning(response)
                else:
                    # Display response
                    st.markdown(response)

                # Add to message history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })

            except Exception as e:
                error_msg = str(e)

                # Provide helpful error messages
                if "402" in error_msg or "token" in error_msg.lower():
                    error_msg = "⚠️ **Token Limit Error**: The request was too large. Please try a shorter query."

                elif "401" in error_msg or "authentication" in error_msg.lower():
                    error_msg = "⚠️ **Authentication Error**: Please check your API key in the .env file."

                elif "429" in error_msg or "rate limit" in error_msg.lower():
                    error_msg = "⚠️ **Rate Limit**: Too many requests. Please wait a moment and try again."

                else:
                    error_msg = f"❌ **Error**: {error_msg}"

                st.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg
                })

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; font-size: 12px; color: #999;'>
    <p>💡 Tip: I remember our conversation! Ask follow-up questions like "convert that to PKR"</p>
    <p style='margin-top: 5px;'>Powered by <strong>Google Gemini 2.0 Flash</strong> via OpenRouter (FREE)</p>
</div>
""", unsafe_allow_html=True)
