import os
import base64


os.makedirs('base_conhecimento', exist_ok=True)
os.makedirs('faiss_index', exist_ok=True)


pdf_content = os.environ.get('PDF_CONHECIMENTO')
if pdf_content:
    pdf_bytes = base64.b64decode(pdf_content)
    with open('base_conhecimento/conhecimento_assistente_ia.pdf', 'wb') as f:
        f.write(pdf_bytes)
    print("✅ PDF criado com sucesso!")
else:
    print("❌ Variável PDF_CONHECIMENTO não encontrada!")

txt_content = os.environ.get('TXT_SOBRE_PORTFOLIO')
if txt_content:
    txt_decoded = base64.b64decode(txt_content).decode('utf-8')
    with open('base_conhecimento/sobre_o_portfolio.txt', 'w', encoding='utf-8') as f:
        f.write(txt_decoded)
    print("✅ TXT criado com sucesso!")
else:
    print("❌ Variável TXT_SOBRE_PORTFOLIO não encontrada!")


faiss_content = os.environ.get('FAISS_INDEX')
if faiss_content:
    faiss_bytes = base64.b64decode(faiss_content)
    with open('faiss_index/index.faiss', 'wb') as f:
        f.write(faiss_bytes)
    print("✅ index.faiss criado com sucesso!")
else:
    print("❌ Variável FAISS_INDEX não encontrada!")


pkl_content = os.environ.get('FAISS_PKL')
if pkl_content:
    pkl_bytes = base64.b64decode(pkl_content)
    with open('faiss_index/index.pkl', 'wb') as f:
        f.write(pkl_bytes)
    print("✅ index.pkl criado com sucesso!")
else:
    print("❌ Variável FAISS_PKL não encontrada!")