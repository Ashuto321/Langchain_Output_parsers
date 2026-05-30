from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b", temperature=0.7)
#  we will ceate a parser object
parser = JsonOutputParser()

# now we will create a template for the prompt
template = PromptTemplate(
    template ="write a name, age, city of a fictional character{format_instructions}",
    input_variables = [],
    partial_variables = {"format_instructions": parser.get_format_instructions()}
)

prompt = template.format()

response = model.invoke(prompt)

final_response = parser.parse(response.content) # this will give us a dictionary in json format

print(final_response)