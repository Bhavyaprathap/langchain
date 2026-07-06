from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt=PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
    
)

llm=ChatOllama1(model="gemma3:4b")
parser=StrOutputParser()

chain=prompt | llm | parser
topic=input("Enter the topic: ")
res=chain.invoke({'topic':topic})
print(res)
chain.get_graph().print_ascii()