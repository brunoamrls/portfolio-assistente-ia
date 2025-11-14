#!/bin/bash

echo "🔐 Clonando repositório privado..."


git clone https://${GITHUB_TOKEN}@github.com/brunoamrls/portfolio-backend-private.git /tmp/private


cp /tmp/private/app.py ./
cp -r /tmp/private/base_conhecimento ./
cp -r /tmp/private/faiss_index ./


rm -rf /tmp/private

echo "✅ Arquivos privados configurados com sucesso!"