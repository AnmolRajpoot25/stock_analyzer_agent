from phi.agent import Agent
import phi.api

from phi.model.groq import Groq
from phi.playground import serve_playground_app
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import phi
from phi.playground import Playground , serve_playground_app
from dotenv import load_dotenv
import os
load_dotenv()

phi.api = os.getenv("phidata_key ")

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
app= Playground(agents = [finance_agent, web_search_agent]).get_app()

if __name__ == '__main__':
    serve_playground_app("playground:app", reload= True)