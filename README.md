# Personal-Fin-Bot

#💰Personal Finance Chatbot
An intelligent, AI-powered financial advisor built with Streamlit that provides personalized financial guidance based on your profile, goals, and life stage.
🌟 Features
Personalized Financial Advice

User Profile-Based Recommendations: Tailored advice for students, working professionals, recent graduates, entrepreneurs, and retirees
Age-Appropriate Guidance: Investment and savings strategies adjusted for your age and risk tolerance
Income-Specific Tips: Advice scaled to your monthly income level
Goal-Oriented Planning: Customized recommendations based on your selected financial goals

Comprehensive Knowledge Base

Savings Strategies: Emergency fund building, high-yield accounts, automation tips
Budgeting Techniques: 50/30/20 rule, zero-based budgeting, expense tracking
Investment Guidance: Index funds, 401(k), IRA, portfolio allocation by age
Debt Management: Debt snowball/avalanche methods, student loan strategies
Retirement Planning: Age-specific retirement savings recommendations
Credit & Tax Advice: Credit score improvement, tax-advantaged accounts

Interactive Chat Interface

Real-time Responses: Instant, contextual financial advice
Conversation Memory: Maintains chat history during your session
Quick Response System: Fast answers for common financial questions
Profile Integration: All advice automatically personalized to your profile

🚀 Getting Started
Prerequisites

Python 3.7 or higher
pip package manager

Installation

Clone the repository
bashgit clone https://github.com/yourusername/personal-finance-chatbot.git
cd personal-finance-chatbot

Install required dependencies
bashpip install streamlit python-dotenv

Set up environment variables (optional)
Create a .env file in the root directory:
HF_API_KEY=your_huggingface_api_key_here
Note: The HF_API_KEY is loaded but not currently used in the implementation
Run the application
bashstreamlit run app.py

Open your browser
The app will automatically open at http://localhost:8501

🎯 Usage
Setting Up Your Profile

Select Your Status: Choose from Student, Working Professional, Recent Graduate, Entrepreneur, or Retiree
Enter Your Age: Used for age-appropriate investment and savings advice
Add Monthly Income: Optional field that helps provide more targeted recommendations
Set Financial Goals: Select from 8 different financial objectives

Getting Financial Advice

Type any financial question in the chat interface
Ask about specific topics like "How should I start investing?" or "Help me create a budget"
Get personalized responses based on your profile
Receive actionable tips with relevant emojis and formatting

Example Questions

"How much should I save each month?"
"What's the best way to pay off my student loans?"
"Should I invest in a 401(k) or Roth IRA?"
"How do I build an emergency fund?"
"What's a good credit score and how do I improve mine?"

🏗️ Project Structure
personal-finance-chatbot/
├── app.py                 # Main Streamlit application
├── .env                   # Environment variables (create this)
├── requirements.txt       # Python dependencies (optional)
├── README.md             # This file
└── .gitignore           # Git ignore file
🔧 Technical Details
Core Components
FinanceChatbot Class

Knowledge Base: Structured financial advice organized by user type and topic
Intent Classification: Identifies user questions and provides relevant responses
Personalization Engine: Customizes advice based on user profile
Response Generation: Creates contextual, helpful financial guidance

Key Methods

get_response(): Main method that processes user input and generates personalized advice
classify_intent(): Determines the topic of user questions using keyword matching
personalize_response(): Adds user-specific context to generic financial advice

User Profile System
The chatbot maintains a user profile with:

Type: Life stage category for targeted advice
Age: Used for risk tolerance and investment timeline recommendations
Income: Enables income-proportional savings and budgeting advice
Goals: Helps focus recommendations on user priorities

Knowledge Base Categories

Savings: Emergency funds, high-yield accounts, automation strategies
Budgeting: Expense tracking, allocation rules, subscription management
Investing: Asset allocation, account types, risk management
Debt: Payoff strategies, consolidation, student loan management
Retirement: Age-appropriate planning, account maximization
Quick Responses: Common financial questions and immediate answers

🎨 User Interface
Main Features

Clean Chat Interface: Streamlit's native chat components for smooth conversation flow
Responsive Sidebar: Dynamic profile management with instant updates
Contextual Tips: Sidebar shows relevant quick tips based on user type
Error Handling: Graceful error management with user-friendly messages

Visual Elements

Emojis: Enhance readability and engagement
Formatted Responses: Clear structure with headers, bullets, and emphasis
Profile Indicators: Visual confirmation of personalization in responses
Goal Integration: Responses reference user's selected financial goals

🔮 Future Enhancements
Potential Features

External API Integration: Real-time market data, interest rates, economic indicators
Advanced Analytics: Spending analysis, goal progress tracking, financial health scoring
Document Upload: Analysis of bank statements, investment portfolios, tax documents
Calculation Tools: Built-in calculators for loans, investments, retirement planning
Export Functionality: Save advice, generate action plans, create financial reports

Technical Improvements

Database Integration: Persistent user profiles and conversation history
Machine Learning: Enhanced intent recognition and response generation
Multi-language Support: Expanded accessibility for diverse users
Mobile Optimization: Enhanced mobile experience and responsive design

⚠️ Disclaimer
This chatbot provides general financial education and guidance. It is not a substitute for professional financial advice. Always consult with qualified financial advisors, accountants, or other professionals for personalized financial planning, investment decisions, or tax advice.
The information provided is for educational purposes only and should not be considered as specific investment recommendations or financial planning advice tailored to your individual circumstances.
📝 License
This project is open source and available under the MIT License.
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.
Areas for Contribution

Additional financial knowledge and advice
New user profile types or life stages
Enhanced personalization algorithms
UI/UX improvements
Bug fixes and performance optimizations

📧 Support
If you encounter any issues or have questions about the Personal Finance Chatbot, please:

Check the existing issues on GitHub
Create a new issue with detailed information
Include your Python version and any error messages
