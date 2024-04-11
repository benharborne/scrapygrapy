""" 
Basic example of scraping pipeline using SmartScraper
"""
from scrapegraphai.graphs import SmartScraperGraph

# ************************************************
# Define the configuration for the graph
# ************************************************
""" 
            Avaiable models:
            - ollama/llama2
            - ollama/mistral
            - ollama/codellama
            - ollama/dolphin-mixtral
            - ollama/mistral-openorca
"""

graph_config = {
    "llm": {
        "model": "ollama/mistral",
        "temperature": 0,
        "format": "json",  # Ollama needs the format to be specified explicitly
        # "model_tokens": 2000, # set context length arbitrarily,
        # "base_url": "http://ollama:11434", # set ollama URL arbitrarily
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "temperature": 0,
    }
}

# ************************************************
# Create the SmartScraperGraph instance and run it
# ************************************************

smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the news with their description.",
    # also accepts a string with the already downloaded HTML code
    source="https://www.wired.com/category/science/",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)
