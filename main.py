import os
os.environ["LITELLM_DROP_PARAMS"] = "true"                                                                                                                                                                                                      
from crew import aqua_crew

result = aqua_crew.kickoff(
    inputs={
        "country": "Saudi Arabia",
        "vision": "Vision 2030",
        "goal": "SDG 6 Clean Water and Sanitation",
        "year": "2040"
    }
)

print("\n===== AquaAI-2040 Final Report =====\n")
print(result)
