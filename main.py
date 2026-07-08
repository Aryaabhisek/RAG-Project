from langchain_community.document_loaders import TextLoader
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate


from dotenv import load_dotenv

load_dotenv()

data = TextLoader("document loaders/notes.txt")

docs = data.load()

template = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful assistant that summarizes text."),
     ("human", "{data}")]
)

model = ChatMistralAI(model = "mistral-small-2506")

prompt = template.format_messages(data=docs[0].page_content)

result = model.invoke(prompt)

print(result.content)