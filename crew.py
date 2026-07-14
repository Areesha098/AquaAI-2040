from crewai import Crew, Process

from agents import (
    water_analysis_agent,
    climate_prediction_agent,
    solution_agent,
    report_agent
)

from tasks import (
    water_task,
    climate_task,
    solution_task,
    report_task
)


aqua_crew = Crew(
    agents=[
        water_analysis_agent,
        climate_prediction_agent,
        solution_agent,
        report_agent
    ],

    tasks=[
        water_task,
        climate_task,
        solution_task,
        report_task
    ],

    process=Process.sequential,
    verbose=False,
    cache=False
)