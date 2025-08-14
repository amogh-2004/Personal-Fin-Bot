

import streamlit as st
import os
import random
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class FinanceChatbot:
    def __init__(self):
        self.api_key = os.getenv("HF_API_KEY")
        
        # Comprehensive financial knowledge base
        self.knowledge_base = {
            "savings": {
                "student": [
                    "Start with the 50/30/20 rule: 50% for needs, 30% for wants, 20% for savings",
                    "Even saving $25-50 per month as a student builds great habits for the future",
                    "Look for high-yield savings accounts that offer better interest rates",
                    "Use apps like Mint or YNAB (often free for students) to track spending",
                    "Take advantage of student discounts wherever possible to save money"
                ],
                "working professional": [
                    "Aim to save 20-25% of your gross income if possible",
                    "Build an emergency fund covering 6-8 months of expenses first",
                    "Automate your savings so the money is moved before you can spend it",
                    "Consider a high-yield savings account for better returns on emergency funds",
                    "Maximize employer 401(k) matching - it's free money!"
                ],
                "recent graduate": [
                    "Start building an emergency fund, even if it's just $500-1000 initially",
                    "Focus on paying off high-interest debt while building savings gradually",
                    "Look into employer benefits like 401(k) matching right away",
                    "Consider automatic transfers to savings to build the habit",
                    "Don't feel pressure to save huge amounts immediately - consistency matters more"
                ]
            },
            
            "budgeting": {
                "student": [
                    "Track where your money goes for a month to identify spending patterns",
                    "Use free budgeting apps or even a simple spreadsheet to start",
                    "Cook at home more often - dining out adds up quickly",
                    "Look for free entertainment options on campus and in your community",
                    "Consider buying used textbooks or renting them to save money"
                ],
                "working professional": [
                    "Use zero-based budgeting where every dollar has a purpose",
                    "Review and optimize recurring subscriptions quarterly",
                    "Automate bill payments to avoid late fees",
                    "Track net worth monthly, not just expenses",
                    "Plan for annual expenses like insurance, gifts, and vacations"
                ],
                "entrepreneur": [
                    "Keep personal and business finances completely separate",
                    "Plan for irregular income with conservative budgeting",
                    "Set aside money for taxes quarterly if self-employed",
                    "Build a larger emergency fund due to income variability",
                    "Track business expenses carefully for tax deductions"
                ]
            },
            
            "investing": {
                "student": [
                    "Start learning about investing even with small amounts ($25-50/month)",
                    "Consider low-cost index funds for broad market exposure",
                    "Understand that time is your biggest advantage with compound interest",
                    "If you work, take advantage of any employer 401(k) matching",
                    "Focus on learning before investing large amounts"
                ],
                "working professional": [
                    "Diversify across different asset classes (stocks, bonds, real estate)",
                    "Consider low-cost index funds and ETFs for core holdings",
                    "Rebalance your portfolio annually or when allocations drift significantly",
                    "Maximize tax-advantaged accounts (401k, IRA, HSA) first",
                    "Consider target-date funds if you prefer a hands-off approach"
                ],
                "retiree": [
                    "Focus on capital preservation and steady income generation",
                    "Consider a bond ladder or dividend-paying stocks for regular income",
                    "Maintain some stock exposure to protect against inflation",
                    "Plan for healthcare costs which typically increase with age",
                    "Consider working with a fee-only financial advisor for complex decisions"
                ]
            },
            
            "debt": {
                "general": [
                    "List all debts with balances, minimum payments, and interest rates",
                    "Consider the debt snowball (smallest balance first) or avalanche (highest interest first) method",
                    "Make minimum payments on all debts, then extra on your target debt",
                    "Avoid taking on new debt while paying off existing debt",
                    "Consider debt consolidation if it lowers your overall interest rate"
                ],
                "student": [
                    "Focus on high-interest debt (credit cards) before student loans",
                    "Look into income-driven repayment plans for federal student loans if needed",
                    "Consider making interest payments on student loans while in school if possible",
                    "Avoid lifestyle inflation after graduation - use raises for debt payments",
                    "Research loan forgiveness programs if you work in qualifying fields"
                ]
            },
            
            "emergency_fund": [
                "Start with a goal of $500-1000 for initial emergency fund",
                "Gradually build to 3-6 months of expenses (6-8 months for irregular income)",
                "Keep emergency funds in a separate, easily accessible savings account",
                "Don't invest emergency funds - they should be liquid and stable",
                "Replenish the fund immediately after using it for true emergencies"
            ],
            
            "retirement": {
                "20s": [
                    "Start contributing to employer 401(k), especially if there's matching",
                    "Consider a Roth IRA for tax-free growth if you're in a lower tax bracket",
                    "Aim to save 10-15% of income for retirement",
                    "Focus on growth investments due to long time horizon",
                    "Don't panic about market volatility - you have decades to recover"
                ],
                "30s": [
                    "Increase retirement savings as income grows",
                    "Consider both traditional and Roth retirement accounts for tax diversification",
                    "Review beneficiaries on retirement accounts regularly",
                    "Balance retirement savings with other goals like home buying",
                    "Consider life insurance if you have dependents"
                ],
                "40s": [
                    "Maximize retirement contributions if possible",
                    "Start thinking about catch-up contributions at age 50",
                    "Review investment allocation - may want to reduce risk slightly",
                    "Consider long-term care insurance",
                    "Help kids with college while still prioritizing retirement"
                ]
            }
        }
        
        # Common financial questions and responses
        self.quick_responses = {
            "credit score": "Your credit score affects loan rates and approval. Pay bills on time, keep credit utilization below 30%, don't close old accounts, and check your credit report annually for errors.",
            
            "401k": "A 401(k) is an employer-sponsored retirement account. Contribute at least enough to get full employer matching, choose low-cost index funds, and increase contributions with raises.",
            
            "roth ira": "A Roth IRA offers tax-free growth and withdrawals in retirement. You contribute after-tax dollars now but pay no taxes later. Great for young people in lower tax brackets.",
            
            "emergency fund": "An emergency fund should cover 3-6 months of expenses in a liquid savings account. Start with $500-1000, then gradually build it up.",
            
            "index funds": "Index funds are low-cost investments that track market indices like the S&P 500. They offer broad diversification and historically solid returns with minimal fees."
        }
    
    def get_response(self, user_message, user_profile):
        """Generate personalized financial advice"""
        
        # Clean and analyze the user message
        message_lower = user_message.lower()
        user_type = user_profile.get("type", "general")
        user_age = user_profile.get("age", 25)
        user_goals = user_profile.get("goals", [])
        user_income = user_profile.get("income", 0)
        
        # Check for quick responses first
        for keyword, response in self.quick_responses.items():
            if keyword in message_lower:
                return self.personalize_response(response, user_profile)
        
        # Classify the main intent
        intent = self.classify_intent(message_lower)
        
        # Get appropriate advice based on intent and user profile
        if intent == "savings":
            advice = self.get_savings_advice(user_type, user_profile)
        elif intent == "budgeting":
            advice = self.get_budgeting_advice(user_type, user_profile)
        elif intent == "investing":
            advice = self.get_investing_advice(user_type, user_age)
        elif intent == "debt":
            advice = self.get_debt_advice(user_type)
        elif intent == "retirement":
            advice = self.get_retirement_advice(user_age)
        else:
            advice = self.get_general_advice(user_message, user_profile)
        
        return self.personalize_response(advice, user_profile)
    
    def classify_intent(self, message):
        """Classify user intent based on keywords"""
        intents = {
            "savings": ["save", "saving", "savings", "emergency fund", "money aside", "rainy day"],
            "budgeting": ["budget", "budgeting", "expenses", "spending", "track money", "allocate"],
            "investing": ["invest", "investing", "investment", "stocks", "portfolio", "401k", "ira", "mutual fund", "etf"],
            "debt": ["debt", "loan", "credit card", "pay off", "owe", "mortgage", "student loan"],
            "retirement": ["retirement", "retire", "pension", "401k", "403b", "roth", "traditional ira"],
            "credit": ["credit score", "credit report", "credit card", "credit history"],
            "taxes": ["tax", "taxes", "deduction", "refund", "irs", "filing"]
        }
        
        for intent, keywords in intents.items():
            if any(keyword in message for keyword in keywords):
                return intent
        
        return "general"
    
    def get_savings_advice(self, user_type, user_profile):
        """Get personalized savings advice"""
        if user_type in self.knowledge_base["savings"]:
            base_advice = random.choice(self.knowledge_base["savings"][user_type])
        else:
            base_advice = random.choice(self.knowledge_base["savings"]["student"])
        
        # Add income-specific advice if available
        income = user_profile.get("income", 0)
        if income > 0:
            if income < 3000:
                base_advice += f"\n\n💡 With your current income of ${income:,}/month, start by saving just $50-100 monthly. Small amounts build great habits!"
            elif income < 6000:
                base_advice += f"\n\n💡 With ${income:,}/month income, try to save $300-600 monthly (10-20% of income)."
            else:
                base_advice += f"\n\n💡 With ${income:,}/month income, aim for saving $1,000+ monthly if possible."
        
        return base_advice
    
    def get_budgeting_advice(self, user_type, user_profile):
        """Get personalized budgeting advice"""
        if user_type in self.knowledge_base["budgeting"]:
            advice = random.choice(self.knowledge_base["budgeting"][user_type])
        else:
            advice = random.choice(self.knowledge_base["budgeting"]["student"])
        
        # Add goal-specific advice
        goals = user_profile.get("goals", [])
        if "Budget Better" in goals:
            advice += "\n\n🎯 Since budgeting is one of your goals, try the 50/30/20 rule as a starting point, then adjust based on your specific needs."
        
        return advice
    
    def get_investing_advice(self, user_type, age):
        """Get age and type appropriate investing advice"""
        if user_type in self.knowledge_base["investing"]:
            advice = random.choice(self.knowledge_base["investing"][user_type])
        else:
            advice = random.choice(self.knowledge_base["investing"]["student"])
        
        # Add age-specific guidance
        if age < 30:
            advice += "\n\n📈 At your age, you can afford to take more risk for potentially higher returns. Consider 80-90% stocks, 10-20% bonds."
        elif age < 50:
            advice += "\n\n⚖️ Consider a balanced approach - maybe 70-80% stocks, 20-30% bonds as you're building wealth."
        else:
            advice += "\n\n🛡️ As you're closer to retirement, consider gradually shifting to more conservative investments."
        
        return advice
    
    def get_debt_advice(self, user_type):
        """Get debt management advice"""
        base_advice = random.choice(self.knowledge_base["debt"]["general"])
        
        if user_type == "student" or user_type == "recent graduate":
            base_advice += "\n\n" + random.choice(self.knowledge_base["debt"]["student"])
        
        return base_advice
    
    def get_retirement_advice(self, age):
        """Get age-appropriate retirement advice"""
        if age < 30:
            return random.choice(self.knowledge_base["retirement"]["20s"])
        elif age < 40:
            return random.choice(self.knowledge_base["retirement"]["30s"])
        else:
            return random.choice(self.knowledge_base["retirement"]["40s"])
    
    def get_general_advice(self, message, user_profile):
        """General financial wisdom"""
        general_tips = [
            "💰 Pay yourself first - automate savings so you don't have to think about it.",
            "📊 The best investment is in your financial education. Keep learning!",
            "🎯 Set specific, measurable financial goals and review them regularly.",
            "⏰ Time in the market beats timing the market for long-term investing.",
            "🔄 Compound interest is incredibly powerful - start early and be consistent.",
            "📝 Track your net worth monthly to see your overall financial progress.",
            "🚫 Avoid lifestyle inflation - as income grows, save the difference.",
            "🏦 Build multiple income streams when possible for financial security.",
            "📱 Use technology and apps to automate and simplify your finances.",
            "👥 Don't compare your finances to others - focus on your own goals and progress."
        ]
        
        return random.choice(general_tips)
    
    def personalize_response(self, base_response, user_profile):
        """Add personalization based on user profile"""
        user_type = user_profile.get("type", "")
        goals = user_profile.get("goals", [])
        
        # Add greeting based on user type
        if user_type == "student":
            prefix = "As a student, "
        elif user_type == "working professional":
            prefix = "For a working professional like you, "
        elif user_type == "recent graduate":
            prefix = "As a recent graduate, "
        elif user_type == "entrepreneur":
            prefix = "As an entrepreneur, "
        elif user_type == "retiree":
            prefix = "In retirement, "
        else:
            prefix = ""
        
        # Add goal-specific encouragement
        goal_encouragement = ""
        if goals:
            if len(goals) == 1:
                goal_encouragement = f"\n\n🎯 I see you're focused on '{goals[0]}' - this advice should help with that goal!"
            else:
                goal_encouragement = f"\n\n🎯 This aligns well with your goals of {', '.join(goals[:2])}!"
        
        return f"{prefix}{base_response}{goal_encouragement}"


def main():
    st.set_page_config(
        page_title="Personal Finance Chatbot",
        page_icon="💰",
        layout="centered"
    )
    
    # Initialize session state
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I'm your personal finance assistant. I can help you with savings, budgeting, investing, taxes, and general financial advice. What would you like to know?"}
        ]
    
    if 'user_profile' not in st.session_state:
        st.session_state.user_profile = {
            "type": "student",
            "income": 0,
            "age": 20,
            "goals": []
        }
    
    # Initialize chatbot
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = FinanceChatbot()
    
    # Header
    st.title("💰 Personal Finance Chatbot")
    st.markdown("Your AI-powered financial advisor for personalized guidance")
    
    # Sidebar for user profile
    with st.sidebar:
        st.header("👤 Your Profile")
        
        # User type
        user_type = st.selectbox(
            "I am a:",
            ["Student", "Working Professional", "Recent Graduate", "Entrepreneur", "Retiree"]
        )
        
        # Age
        age = st.slider("Age", 18, 80, 25)
        
        # Income (optional)
        income = st.number_input(
            "Monthly Income ($)", 
            min_value=0, 
            value=0,
            help="Optional - helps provide more personalized advice"
        )
        
        # Financial goals
        st.subheader("🎯 Financial Goals")
        goals = st.multiselect(
            "Select your goals:",
            [
                "Build Emergency Fund",
                "Pay Off Debt", 
                "Save for House",
                "Retirement Planning",
                "Start Investing",
                "Improve Credit Score",
                "Budget Better",
                "Tax Planning"
            ]
        )
        
        # Update profile
        st.session_state.user_profile = {
            "type": user_type.lower(),
            "income": income,
            "age": age,
            "goals": goals
        }
        
        # Quick tips
        st.markdown("---")
        st.markdown("💡 **Quick Tips:**")
        if user_type == "Student":
            st.markdown("• Start small with savings")
            st.markdown("• Use student discounts")
            st.markdown("• Learn about compound interest")
        elif user_type == "Working Professional":
            st.markdown("• Maximize 401(k) matching")
            st.markdown("• Build 6-month emergency fund")
            st.markdown("• Consider tax-advantaged accounts")
    
    # Main chat interface
    st.markdown("---")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me anything about personal finance..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.chatbot.get_response(
                        prompt, 
                        st.session_state.user_profile
                    )
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    error_message = "I apologize, but I encountered an error. Please try asking your question again."
                    st.markdown(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": error_message})
                    st.error(f"Debug info: {str(e)}")
    
    # Footer
    st.markdown("---")
    st.markdown("💡 *This chatbot provides general financial education. Always consult a professional advisor for personalized financial planning.*")

if __name__ == "__main__":
    main()