from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

data = PyPDFLoader("document loaders/Aryaabhisek_Mahapatra_Resume.pdf")

docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap=10
)

chunks = splitter.split_documents(docs)

print(chunks[0].page_content)

#print(docs[3]) to print a specific page
#print(len(docs)) to get the length of the pdf and the no of pages in pdf == document length or pdf length
#print(docs)
