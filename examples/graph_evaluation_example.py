import os
from scrapegraphai.evaluetor import TrulensEvaluator
from dotenv import load_dotenv

load_dotenv()

# Define the configuration for the language model
openai_key = os.getenv("OPENAI_APIKEY")

llm_config = {
    "api_key": openai_key,
    "model_name": "gpt-3.5-turbo",
}

list_of_inputs = [
    ("List me all the titles and project descriptions", "https://perinim.github.io/projects/", llm_config),
    ("Who is the author of the project?", "https://perinim.github.io/projects/", llm_config),
    ("What is the project about?", "https://perinim.github.io/projects/", llm_config)
]

# Create the TrulensEvaluator instance
trulens_evaluator = TrulensEvaluator()
# Evaluate SmartScraperGraph on the list of inputs
trulens_evaluator.evaluate(list_of_inputs)
