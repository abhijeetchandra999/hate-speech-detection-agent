from crewai import Task
from agents import hate_speech_detector

# Define a task with a description and expected output
hate_speech_detection_task = Task(
    description=(
        "Analyze the following text to determine whether it is hate speech.\n"
        "Use a high-precision policy: only label as hate speech when there is clear evidence.\n"
        "Decision rules:\n"
        "1. First identify whether a protected group or protected characteristic is targeted (for example race, ethnicity, religion, nationality, gender, disability).\n"
        "2. Label as hate speech only if both are present: (a) a clear target, and (b) hateful intent such as dehumanization, exclusion, inferiority claims, threat...\n"
        "3. Do not label as hate speech for profanity, rudeness, or insults that do not target a protected group.\n"
        "4. If hateful language is quoted, reported, or discussed in educational/news context, treat as no hate speech unless the speaker clearly endorses it.\n"
        "5. For sarcasm, irony, coded language, or dog whistles, label as hate speech only when context makes targeted hostility explicit.\n"
        "6. For self-referential or reclaimed slurs, treat as no hate speech unless used to demean or attack a protected target.\n"
        "7. If evidence is ambiguous or insufficient, choose no hate speech.\n"
        "Final check before answering: verify your label matches the rules above.\n"
        "Text:\n{text}"
    ),
    expected_output="Return exactly one label and nothing else: hate speech or no hate speech",
    agent=hate_speech_detector,
)
