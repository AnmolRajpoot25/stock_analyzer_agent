from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

from dotenv import load_dotenv
import os

load_dotenv() 

print("GROQ_API_KEY loaded:", os.getenv("GROQ_API_KEY"))


web_search_agent = Agent(
    name = "web_search_ agent",
    role = " search the web  for the information ",
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = ["always include sources "],
    show_tools_calls = True,
    markdown = True ,
)
## financial agent

finance_agent = Agent(
    name = "finance_agent",
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [YFinanceTools(
        stock_price= True , analyst_recommendations = True , stock_fundamentals= True ,
        company_news= True
    ),
],
    instructions = [" use tables to display  the data "],
    show_tools_calls = True,
    markdown =  True ,
)
multi_ai_agent = Agent(
    model = Groq(id = "llama-3.3-70b-versatile"),
    team = [web_search_agent, finance_agent ],
    instructions = ["Always  include the  sources" , " use table to display the data"],
    show_tools_calls = True,
    markdown= True ,
)
multi_ai_agent.print_response(" summarize analyst recommentdation and share the latest news of the NIVIDIA " , stream = True )