from langchain.agents import create_agent
agent = create_agent(model="ollama:north-mini-code-1.0", tools=tools)

#for openai
from langchain.agents import create_agent
agent = create_agent(model="openai:gpt-5.5", tools=tools)

from langchain_ollama import ChatOllama #for the llms we can use the separate models(gemma,qwen..etc)
llm=ChatOllama(model="gemma3:4b")
