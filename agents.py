from crewai import Agent, LLM
import os
from dotenv import load_dotenv

load_dotenv()
import os
os.environ["LITELLM_DROP_PARAMS"] = "True"
llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
    max_tokens=100
)








water_analysis_agent = Agent(
    role="Water Management Analyst",
    goal="Analyze Saudi Arabia water challenges related to Vision 2030 and SDG 6.",
    backstory="Expert in sustainable water management systems.",
    llm=llm,
   verbose=False
)

climate_prediction_agent = Agent(
    role="Climate Prediction Specialist",
    goal="Predict future water risks from 2030 to 2040.",
    backstory="AI researcher focused on climate and sustainability.",
    llm=llm,
    verbose=False
)

solution_agent = Agent(
    role="AI Sustainability Solution Expert",
    goal="Design AI-based water saving solutions.",
    backstory="Specialist in smart cities and resource optimization.",
    llm=llm,
    verbose=False
)

report_agent = Agent(
    role="Vision 2030 Strategy Advisor",
    goal="Create final sustainability recommendations.",
    backstory="Advisor for Saudi Vision 2030 projects.",
    llm=llm,
    verbose=False
)
