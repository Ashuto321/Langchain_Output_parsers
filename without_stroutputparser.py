from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b", temperature=0.7)


# 1st prompt: -> detailed Report
template1 = PromptTemplate(
    template=" Write a detalied report on the following topic: {topic}",
    input_variables=["topic"]
)

# 2nd prompt: -> summary
template2 = PromptTemplate(
    template = "Summarize the following report in 3 sentences: {report}",
    input_variables=["report"]
)

# we will fill the placegolders for these
prompt1 = template1.invoke({"topic": "About Graph Rag"})

response1 = model.invoke(prompt1)

prompt2 = template2.invoke({"report": response1.content})

# now we will call the model with these prompts in hand
response = model.invoke(prompt2)

print(response.content)