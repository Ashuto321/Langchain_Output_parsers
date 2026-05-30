from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b", temperature=0.7)

# 1st prompt: -> detailed Report
template1 = PromptTemplate(
    template = " write a detailed report on the following topic: {topic}",
    input_variables=["topic"]
)
# 2nd prompt: -> summary
template2 = PromptTemplate(
    template = "Summarize the followig report in 4 sentences: {report}",
    input_variables=["report"]
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

response = chain.invoke({"topic": "About Graph Rag"})

print(response)