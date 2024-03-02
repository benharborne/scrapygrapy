"""
Example of custom graph using existing nodes
"""

import os
from dotenv import load_dotenv
from scrapegraphai.models import OpenAI
from scrapegraphai.graphs import BaseGraph
from scrapegraphai.nodes import TextNode, ParseTextNode, GenerateAnswerNode

load_dotenv()

# Define the configuration for the language model
openai_key = os.getenv("OPENAI_APIKEY")
llm_config = {
    "api_key": openai_key,
    "model_name": "gpt-3.5-turbo",
    "temperature": 0,
    "streaming": True
}
model = OpenAI(llm_config)

with open("text_example.txt", "r", encoding="utf-8") as file:
    text = file.read()


# define the nodes for the graph
fetch_html_node = TextNode("load_html")
parse_document_node = ParseTextNode("parse_document")
generate_answer_node = GenerateAnswerNode(model, "generate_answer")

# create the graph
graph = BaseGraph(
    nodes={
        fetch_html_node,
        parse_document_node,
        generate_answer_node
    },
    edges={
        (fetch_html_node, parse_document_node),
        (parse_document_node, generate_answer_node)
    },
    entry_point=fetch_html_node
)

# execute the graph
inputs = {"user_input": "Give me the name of all the news",
          "url": text}
result = graph.execute(inputs)

# get the answer from the result
answer = result.get("answer", "No answer found.")
print(answer)
