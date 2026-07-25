import os
from crewai import Crew
from agents import hate_speech_detector
from tasks import hate_speech_detection_task

# Define the Crew with agents and tasks
crew = Crew(
    agents=[hate_speech_detector],
    tasks=[hate_speech_detection_task],
    verbose=True
)

# Kickoff the Crew with the input query
# Text = "Public libraries are important resources for everyone in the city."
# Text = "That country is less intelligent and incapable of contributing to society."
Text = "That country is less intelligent and incapable of contributing to society."

result = crew.kickoff(inputs={"text": Text})

print("Response:", result)
