from crewai import Task
from agents import (
    water_analysis_agent,
    climate_prediction_agent,
    solution_agent,
    report_agent
)

water_task = Task(
    description="Analyze Saudi Arabia water challenges.",
    agent=water_analysis_agent,
    expected_output="Maximum 50 words."
)

climate_task = Task(
    description="Predict water risks till 2040.",
    agent=climate_prediction_agent,
    expected_output="Maximum 50 words."
)

solution_task = Task(
    description="Suggest 5 AI water solutions.",
    agent=solution_agent,
    expected_output="Maximum 50 words."
)

report_task = Task(
    description="Write a 150-word final report.",
    agent=report_agent,
    expected_output="150-word report."
)