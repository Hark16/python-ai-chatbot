from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from config import api_token


template = "<s>[INST] </s>{question}[/INST]"

prompt_template = PromptTemplate.from_template(template)
formatted_prompt_template = prompt_template.format(
    
    question = ""
    
)

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(
    repo_id=repo_id, huggingfacehub_api_token= api_token)
# response = llm.invoke(formatted_prompt_template)
# print(response)

# Streaming
response = llm.stream(formatted_prompt_template)
for res in response:
    print(res, end="", flush=True)
