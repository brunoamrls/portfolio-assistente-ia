import os
import base64


app_content = os.environ.get('APP_PY_CONTENT')

if app_content:

    decoded = base64.b64decode(app_content).decode('utf-8')
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(decoded)
    print("✅ app.py criado com sucesso!")
else:
    print("❌ Variável APP_PY_CONTENT não encontrada!")
    exit(1)