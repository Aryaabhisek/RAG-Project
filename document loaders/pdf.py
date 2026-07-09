from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("document loaders/Aryaabhisek_Mahapatra_Resume.pdf")

docs = data.load()

#print(docs[3]) to print a specific page
#print(len(docs)) to get the length of the pdf and the no of pages in pdf == document length or pdf length
print(docs)
