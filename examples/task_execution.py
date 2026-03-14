from src.agent import AstraeusAgent
from src.tools import get_market_data, perform_search, calculate_risk

def main():
    # Configuration
    api_key = "sk-..." # Should be loaded from .env
    
    # Initialize Agent
    agent = AstraeusAgent(api_key=api_key)
    
    # Register Domain-Specific Tools
    agent.register_tool("fetch_data", get_market_data)
    agent.register_tool("search_web", perform_search)
    agent.register_tool("calc_risk", calculate_risk)
    
    # Execute Complex Task
    task = \"\"\"
    Analyze the current risk for ticker 'AAPL'. 
    Search for recent news that might affect volatility, 
    then calculate a risk score based on the current price of 150.0 
    and a volatility estimate of 0.4.
    \"\"\"
    
    # agent.execute(task)
    print(f"Task prepared for execution: {task}")
    print("Astraeus is ready for autonomous planning.")

if __name__ == "__main__":
    main()