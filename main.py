from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

data = PyPDFLoader("document loaders/Aryaabhisek_Mahapatra_Resume.pdf")

docs = data.load()

template = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful assistant that summarizes text."),
     ("human", "{data}")]
)

model = ChatMistralAI(model = "mistral-small-2506")
embedding_model = MistralAIEmbeddings(model="mistral-embed")

prompt = template.format_messages(data=docs[0].page_content)

result = model.invoke(prompt)

print(result.content)