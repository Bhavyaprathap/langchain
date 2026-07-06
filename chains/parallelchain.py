# from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv
# load_dotenv()
from langchain.schema.runnable import RunnableParallel

model1=ChatOllama(model="qwen3:4b")
model2=ChatOllama(model="qwen3:4b")

prompt1=PromptTemplate(
    template="Generate short and simple notes from the following text\n {text}",
    input_variables=['text']
)
prompt2=PromptTemplate(
    template="Generate 5 questions and answers from the following text\n {text}",
    input_variables=['text']
)

prompt3=PromptTemplate(
    template="merge the provided notes and quiz into a single document\n {notes} and {quiz}",
    input_variables=['notes','quiz']
)

parser=StrOutputParser()

#create a dictionary 
paralle_chain=RunnableParallel({
    'notes':prompt1 | model1 | parser,
    'quiz':prompt2 | model2 | parser
})

merge_chain=prompt3 | model1 | parser

res=paralle_chain | merge_chain

text = """
LangChain is an open-source framework used to build applications powered by Large Language Models (LLMs). 
It simplifies the process of developing AI applications by providing components such as prompt templates, 
chains, tools, agents, memory, document loaders, retrievers, and output parsers.

A PromptTemplate helps developers create dynamic prompts by inserting variables into predefined templates. 
This avoids writing hardcoded prompts repeatedly and makes applications more flexible.

Chains allow developers to connect multiple components together so that the output of one component becomes 
the input of another. This enables complex workflows with minimal code.

Tools are functions that an AI model can call to perform specific tasks such as calculations, searching the web, 
or fetching live weather information. Agents use these tools intelligently by deciding which tool should be used 
for a given user request.

Output Parsers help convert the raw output of an LLM into structured formats such as strings, JSON objects, 
or custom Python objects, making the output easier to process programmatically.
"""

final=res.invoke({'text':text})
print(final)
res.get_graph().print_ascii()



