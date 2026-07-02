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



