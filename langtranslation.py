from langchain_core.messages import HumanMessage, SystemMessage
import os
from langchain_google_genai import ChatGoogleGenerativeAI
os.environ["GOOGLE_API_KEY"] = "give ur key here else u can read it from .evn file"

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0.7
)
messages = [
    SystemMessage("You are a helpful assistant that translates English to Odiya"),
    HumanMessage("Hello, how are you? Team working on Langchain with google gemini")
      ]

model.invoke(messages)
response = model.invoke(messages)
print(response.text)
