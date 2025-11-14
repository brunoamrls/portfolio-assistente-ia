#!/bin/bash
set -e

echo "🔐 Clonando repositório privado..."

git clone --depth 1 https://${GITHUB_TOKEN}@github.com/brunoamrls/portfolio-backend-private.git /tmp/p

cp /tmp/p/app.py ./
cp -r /tmp/p/base_conhecimento ./
cp -r /tmp/p/faiss_index ./

rm -rf /tmp/p

echo "✅ Arquivos copiados!"

pip install -r requirements.txt

echo "✅ Build concluído!"