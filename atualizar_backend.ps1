param(
    [string]$mensagem = "Atualizacao do backend"
)

Write-Host "===================================" -ForegroundColor Cyan
Write-Host "Iniciando atualizacao do backend..." -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan

try {
    Write-Host "1. Copiando app.py..." -ForegroundColor Yellow
    Copy-Item "D:\Tecnologia\portfolio\backend\app.py" -Destination "D:\Tecnologia\portfolio-backend-private\" -Force
    
    Write-Host "2. Copiando base_conhecimento..." -ForegroundColor Yellow
    Copy-Item "D:\Tecnologia\portfolio\backend\base_conhecimento\*" -Destination "D:\Tecnologia\portfolio-backend-private\base_conhecimento\" -Recurse -Force
    
    Write-Host "3. Copiando faiss_index..." -ForegroundColor Yellow
    Copy-Item "D:\Tecnologia\portfolio\backend\faiss_index\*" -Destination "D:\Tecnologia\portfolio-backend-private\faiss_index\" -Recurse -Force
    
    Write-Host "4. Mudando para repositorio privado..." -ForegroundColor Yellow
    Set-Location "D:\Tecnologia\portfolio-backend-private"
    
    Write-Host "5. Adicionando arquivos ao Git..." -ForegroundColor Yellow
    git add .
    
    Write-Host "6. Fazendo commit..." -ForegroundColor Yellow
    git commit -m "$mensagem"
    
    Write-Host "7. Enviando para GitHub..." -ForegroundColor Yellow
    git push
    
    Write-Host ""
    Write-Host "===================================" -ForegroundColor Green
    Write-Host "Atualizacao concluida com sucesso!" -ForegroundColor Green
    Write-Host "===================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Proximos passos:" -ForegroundColor Cyan
    Write-Host "1. Acesse: https://dashboard.render.com" -ForegroundColor White
    Write-Host "2. Entre no servico: bruno-portfolio-ia" -ForegroundColor White
    Write-Host "3. Clique: Manual Deploy -> Deploy latest commit" -ForegroundColor White
    
} catch {
    Write-Host ""
    Write-Host "===================================" -ForegroundColor Red
    Write-Host "ERRO durante a atualizacao!" -ForegroundColor Red
    Write-Host "===================================" -ForegroundColor Red
    Write-Host "Detalhes: $_" -ForegroundColor Red
}
