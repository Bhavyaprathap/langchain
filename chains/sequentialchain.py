from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt1=PromptTemplate(
    template="Generate a detailed report about the {topic}",
    input_variables=['topic']
    
)
prompt2=PromptTemplate(
    template="Generate 5 points from the following text {text}",
    input_variables=['text']
    
)
llm=ChatOllama1(model="gemma3:4b")
parser=StrOutputParser()
chain=prompt1 | llm | parser | prompt2 | llm | parser
topic=input()
text=input()
res=chain.invoke({'topic':topic})
print(res)