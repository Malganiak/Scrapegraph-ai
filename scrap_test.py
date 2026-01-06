from scrapegraphai.graphs import SmartScraperGraph

# Configuration settings for the scraper graph
graph_config = {
    "llm": {
        "model": "ollama/llama3",  # Specifies the large language model to use
        "temperature": 0,          # Temperature controls randomness; 0 makes it deterministic
        "format": "json",          # Output format is set to JSON
        "base_url": "http://localhost:11434",  # Base URL where the Ollama server is running
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",  # Specifies the embedding model to use
        "temperature": 0,                    # Keeps the generation deterministic
        "base_url": "http://localhost:11434",  # Base URL for the embeddings model server
    },
    "verbose": True,  # Enables verbose output for more detailed log information
}

# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="Extract useful information from the webpage, including a description of what the company does, founders and social media links",
    source="https://www.lemondeinformatique.fr/actualites/lire-l-ia-claude-aide-a-concevoir-un-langage-de-programmation-98936.html",
    config=graph_config
)

# Run the pipeline
result = smart_scraper_graph.run()

import json
print(json.dumps(result, indent=4))