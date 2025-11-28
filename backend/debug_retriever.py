import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

# Carrega a API Key
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

print("🔍 Iniciando Diagnóstico do Banco de Dados...")

# Tenta carregar o índice
try:
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 20}) # Simula o mesmo k do seu app
except Exception as e:
    print(f"❌ Erro fatal ao carregar o índice FAISS: {e}")
    exit()

# APENAS ALTERE ESSA PERGUNTA PARA O DIAGNÓSTICO --->
pergunta = "Quais tipos de Notas Fiscais Bruno já atuou?"
print(f"\n❓ Pergunta Teste: {pergunta}")

# Busca os documentos (chunks) mais relevantes
docs = retriever.invoke(pergunta)

print(f"📄 Chunks encontrados: {len(docs)}\n")

encontrou_info = False

for i, doc in enumerate(docs):
    conteudo = doc.page_content.lower()
    
    # Verifica se as palavras-chave da resposta esperada estão no texto
    tem_notas = "notas fiscais" in conteudo
    tem_abastecimento = "abastecimento" in conteudo
    
    marcador = "✅" if tem_notas else "❌"
    
    print(f"--- Chunk {i+1} {marcador} ---")
    if tem_notas:
        encontrou_info = True
        # Mostra o trecho exato onde aparece 'Notas Fiscais'
        posicao = conteudo.find("notas fiscais")
        trecho = doc.page_content[posicao:posicao+150] # Pega 150 caracteres a partir da palavra
        print(f"CONTEÚDO ENCONTRADO: \"...{trecho}...\"")
    else:
        # Mostra o início do texto só para sabermos o que é
        print(f"Texto (início): {doc.page_content[:80]}...")
    print("------------------------------------------------")

if encontrou_info:
    print("\n✅ CONCLUSÃO: A informação ESTÁ no banco de dados e foi recuperada.")
else:
    print("\n❌ CONCLUSÃO: A informação NÃO foi encontrada nos top 5 resultados.")
    print("Possíveis causas: O índice não foi atualizado ou o texto está muito longe.")