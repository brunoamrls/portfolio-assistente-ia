document.addEventListener('DOMContentLoaded', function() {
    const perguntaInput = document.getElementById('pergunta-usuario');
    const botaoPerguntar = document.querySelector('button[type="submit"]');
    const respostaDiv = document.getElementById('resposta');
    
        const originalPlaceholderHTML = respostaDiv.innerHTML;

    const isLocalhost = window.location.hostname === '127.0.0.1' || window.location.hostname === 'localhost';


    const BACKEND_URL = isLocalhost 
        ? 'http://127.0.0.1:5000/perguntar' 
        : 'https://bruno-portfolio-ia.onrender.com/perguntar';

    console.log(`Ambiente detectado: ${isLocalhost ? 'LOCAL' : 'PRODUÇÃO'}`);
    console.log(`Conectando em: ${BACKEND_URL}`);
    

    const MAX_RETRIES = 3;
    const RETRY_DELAYS = [0, 10000, 20000]; // 0s, 10s, 20s

    async function fazerPerguntaComRetry(pergunta, tentativa = 0) {
        try {

            if (tentativa === 0) {
                respostaDiv.innerHTML = `
                    <div class="loading">
                        <p>🤖 Carregando assistente...</p>
                        <p><small>A primeira resposta pode levar até 1 minuto enquanto o servidor inicia.</small></p>
                    </div>
                `;
            } else {
                respostaDiv.innerHTML = `
                    <div class="loading">
                        <p>🤖 Tentando novamente... (tentativa ${tentativa + 1}/${MAX_RETRIES})</p>
                        <p><small>Aguarde, o servidor está iniciando...</small></p>
                    </div>
                `;
            }
            
            const response = await fetch(BACKEND_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    pergunta: pergunta
                }),
                signal: AbortSignal.timeout(60000) // Timeout de 60 segundos
            });
            
            if (!response.ok) {
                throw new Error(`Erro HTTP: ${response.status}`);
            }
            
            const dados = await response.json();
            exibirResposta(dados);
            
        } catch (error) {
            console.error(`Erro na tentativa ${tentativa + 1}:`, error);
            
            if (tentativa < MAX_RETRIES - 1) {
                const delay = RETRY_DELAYS[tentativa + 1];
                
                respostaDiv.innerHTML = `
                    <div class="loading">
                        <p>⏳ Servidor iniciando... Tentando novamente em ${delay / 1000} segundos...</p>
                    </div>
                `;
                
                setTimeout(() => {
                    fazerPerguntaComRetry(pergunta, tentativa + 1);
                }, delay);
            } else {

                respostaDiv.innerHTML = `
                    <div class="error">
                        <p>❌ <strong>Não foi possível conectar ao assistente.</strong></p>
                        <p>O servidor pode estar temporariamente indisponível.</p>
                        <p><small>Tente novamente em alguns instantes. Se o problema persistir, entre em contato.</small></p>
                    </div>
                `;
            }
        }
    }
    
    function exibirResposta(dados) {
        let html = '';
        if (dados.resposta) {
            const respostaFormatada = dados.resposta.replace(/\n/g, '<br>');
            html = `<p class="resposta-p">${respostaFormatada}</p>`;
        }
        respostaDiv.innerHTML = html;
    }
    
    botaoPerguntar.addEventListener('click', function(e) {
        e.preventDefault();
        const pergunta = perguntaInput.value.trim();
        
        if (!pergunta) {
            respostaDiv.innerHTML = `
                <div class="error">
                    <p>⚠️ Por favor, digite uma pergunta antes de enviar.</p>
                </div>
            `;
            return;
        }
        
        fazerPerguntaComRetry(pergunta);
    });
    
    perguntaInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            botaoPerguntar.click();
        }
    });
    
    perguntaInput.addEventListener('input', function() {
        if (perguntaInput.value.trim() === '') {
            respostaDiv.innerHTML = originalPlaceholderHTML;
        }
    });
});

async function testarBackend() {  }
window.addEventListener('load', () => {  });