from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGroq(model ="openai/gpt-oss-safeguard-20b", temperature=0.7)

class user_info(BaseModel):
    name: str = Field(description="name of the person")
    age : int = Field(gt=18, lt=100, description="Age of the person")
    City : str= Field(description="name of the city person belong to")
    

parser = PydanticOutputParser(pydantic_object=user_info)

template = PromptTemplate(
    template = "give me the name , age and city of a fiction {place} {format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

# prompt = template.invoke({'place':'america'})

# response = model.invoke(prompt)

# final_response = parser.parse(response.content)

# chains
chain = template | model | parser

response=chain.invoke({'place': 'nepal'})

print(response)

# print("hello")