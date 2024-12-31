from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from huggingface_hub import login

import os

from dotenv import load_dotenv
load_dotenv()

login(os.getenv("HUGGINGFACE_API_KEY"))

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

agent.run("Quantos tempo levaria para um carro atual de fórmula 1 percorrer toda a extensão da Ponte Rio-Niterói, respeitando seus limites de velocidade?")