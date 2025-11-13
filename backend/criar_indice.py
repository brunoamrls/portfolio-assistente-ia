import os
import pathlib
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import PyMuPDFLoader, TextLoader 
from langchain_community.vectorstores import FAISS


load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY não encontrada no arquivo .env")

print("Iniciando processo de criação de índice...")

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=GOOGLE_API_KEY
)


docs = []
pdf_files = list(pathlib.Path("./base_conhecimento/").glob("*.pdf"))
txt_files = list(pathlib.Path("./base_conhecimento/").glob("*.txt"))
all_files = pdf_files + txt_files 

if not all_files: 
    print("Nenhum arquivo encontrado na pasta 'base_conhecimento'. Abortando.")
else:
    for n in all_files:
        try:
            if str(n).endswith(".pdf"):
                loader = PyMuPDFLoader(str(n))
            else:
                
                loader = TextLoader(str(n), encoding='utf-8')
            docs.extend(loader.load())
            print(f"Carregado: {n.name}")
        except Exception as e:
            print(f"Erro ao carregar {n.name}: {e}")


    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
    chunks = splitter.split_documents(docs)
    print(f"Total de documentos divididos em {len(chunks)} chunks.")


    print("Gerando embeddings e criando o vectorstore FAISS. Isso pode levar alguns minutos...")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    print("Vectorstore criado com sucesso.")


    vectorstore.save_local("faiss_index")
    print("Índice FAISS salvo com sucesso na pasta 'faiss_index'.")