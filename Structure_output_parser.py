from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema  

load_dotenv()

model = ChatGroq(model ="openai/gpt-oss-120b", temperature=0.7)

schema = [
    ResponseSchema(name='fact_1', description="Give me any fact 1"),
    ResponseSchema(name='fact_2', description="Give me any fact 2"),
    ResponseSchema(name='fact_3', description="Give me any fact 3"),
    ResponseSchema(name='fact_4', description="Give me any fact 4"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = "Give me 4 facts about the topic: {topic} {format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt = template.invoke({"topic":"Black hole"})

response = model.invoke(prompt)

final_response=parser.parse(response.content)

print(final_response)


