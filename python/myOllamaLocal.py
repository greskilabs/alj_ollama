#Requires packages:
#pip install langchain langchain-ollama  ollama

import os
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

#Load Env variables
#load_dotenv()
context_variables = {"name": "Charlie", "user_id": 8675309}
name = context_variables.get("name", None)
    
template = """
    Answer the question below.

    here is the conversation history: {context}

    Question: {question}

    Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def handle_conversation():
    context = ""
    user_input = ""
    print("Welcome to your ollama chat bot. Type 'exit' to quit.")
    while True:
        user_input = input(f"{name}: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Ollama Bot: ",result)
        context += f"\n{name}: {user_input}\nBot: {result}"


if __name__ == "__main__":
    handle_conversation()