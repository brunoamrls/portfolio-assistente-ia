import os
import base64

# Cria a pasta se não existir
os.makedirs('base_conhecimento', exist_ok=True)

# Reconstrói o PDF
pdf_content = os.environ.get('PDF_CONHECIMENTO')
if pdf_content:
    pdf_bytes = base64.b64decode(pdf_content)
    with open('base_conhecimento/conhecimento_assistente_ia.pdf', 'wb') as f:
        f.write(pdf_bytes)
    print("✅ PDF criado com sucesso!")
else:
    print("❌ Variável PDF_CONHECIMENTO não encontrada!")

# Reconstrói o TXT
txt_content = os.environ.get('TXT_SOBRE_PORTFOLIO')
if txt_content:
    txt_decoded = base64.b64decode(txt_content).decode('utf-8')
    with open('base_conhecimento/sobre_o_portfolio.txt', 'w', encoding='utf-8') as f:
        f.write(txt_decoded)
    print("✅ TXT criado com sucesso!")
else:
    print("❌ Variável TXT_SOBRE_PORTFOLIO não encontrada!")