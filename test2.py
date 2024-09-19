from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from config import api_token

# Initialize the LLM
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(repo_id=repo_id, huggingfacehub_api_token=api_token)

# Define the prompt template
template = "<s>[INST]Write long answer of</s>{question}[/INST]"
prompt_template = PromptTemplate.from_template(template)

while True:
    # Get the user's question
    user_question = input("Enter your question (type 'exit' to quit): ")

    # Check if the user wants to exit
    if user_question.lower() == "exit":
        print("Exiting the loop. Goodbye!")
        break

    # Format the prompt with the user's question
    formatted_prompt_template = prompt_template.format(question=user_question)

    # Get the response from the LLM
    response = llm.stream(formatted_prompt_template)
    
    # Print the response
    for res in response:
        print(res, end="", flush=True)
    print("\n")  # Print a newline for better readability between responses
