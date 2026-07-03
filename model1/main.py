from langchain_ollama import ChatOllama
llm=ChatOllama(model="gemma3:4b")#just to prepare the connection
# ans=llm.invoke("Explain langchain in detailed")#invoke 
# print(ans.content)
# print(type(ans))
# print(ans)
question=input("Ask any question!")
res=llm.invoke(question)
print("\nbhavya: \n")
print(res.content)



from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

llm=ChatOllama(model="gemma3:4b")


topic=input("Enter topic: ")
difficulty=input("Enter difficulty: ")

#prompt template
prompt=PromptTemplate.from_template(
    """you are an experienced technical interviewer.
    Generate 10 {difficulty} interview questions on {topic}
    Only generate the questions.
    Do not provide the answers.
    """
)

#invoking
final_prompt=prompt.invoke({
    "topic":topic,
    "difficulty":difficulty
}
)
response=llm.invoke(final_prompt)

print("\n=*10")
print("response generator!")
print("\n=*10")
print(response.content)








