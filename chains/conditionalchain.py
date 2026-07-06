



# ChatOllama -> Connects LangChain to local Ollama models.
from langchain_ollama import ChatOllama
# PromptTemplate -> Creates reusable and dynamic prompts.

from langchain_core.prompts import PromptTemplate
# RunnableParallel -> Runs multiple chains at the same time.

from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda

# StrOutputParser -> Converts AI output into a simple string.
from langchain_core.output_parsers import StrOutputParser

# PydanticOutputParser -> Converts AI output into a structured Python object.
from langchain_core.output_parsers import PydanticOutputParser

# BaseModel -> Defines the schema of the structured output.
# Field -> Adds descriptions, validation, and constraints to schema fields.
from pydantic import BaseModel,Field
 
# Literal -> Restricts a value to fixed choices (e.g., "Beginner", "Intermediate", "Advanced").
from typing import Literal


# -------------------------------
# Create LLM
# -------------------------------
model=ChatOllama(model="gemma3:4b")



# -------------------------------
# Define Output Schema
# -------------------------------
class Feedback(BaseModel):
    sentiment: Literal['Positive','Negative']=Field(description="Give te sentiment of the feedback")
    
    
# -------------------------------
# Create Parser
# -------------------------------
parser=PydanticOutputParser(pydantic_object=Feedback)
string_parser=StrOutputParser()

# -------------------------------
# Prompt 1 : Sentiment Classifier
# -------------------------------
prompt1 = PromptTemplate(
    template="""
        Classify the following feedback.{format_instructions}
        Feedback:{feedback}
        """,
    input_variables=["feedback"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    },
)

# -------------------------------
# Prompt 3 : Psitive Reply
# -------------------------------
prompt2=PromptTemplate(
    template="give the appropriate response to this positive feedback\n {feedback}",
    input_variables=['feedback']
)

# -------------------------------
# Prompt 3 : Negative Reply
# -------------------------------

prompt3=PromptTemplate(
    template="give the approriate response of this negative feedback\n {feeback}",
    input_variables=['feedback']
    
)

# -------------------------------
#classifier chain
# -------------------------------

branch_chain=RunnableBranch(
    (lambda x:x.sentiment=="Positive",prompt2 | model | string_parser),
    (lambda x:x.sentiment =="Negatve",prompt3 | model | string_parser),
    RunnableLambda(lambda x:"could not find the  sentiment")
)
classifier= prompt1 | model | parser

res=classifier | branch_chain
ans=res.invoke({'feedback':'this is a best college'})
print(ans)
res.get_graph().print_ascii()

