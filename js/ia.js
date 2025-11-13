document.addEventListener('DOMContentLoaded', function() {
    const perguntaInput = document.getElementById('pergunta-usuario');
    const botaoPerguntar = document.querySelector('button[type="submit"]');
    const respostaDiv = document.getElementById('resposta');
    
    const originalPlaceholderHTML = respostaDiv.innerHTML;

    const BACKEND_URL = 'http://127.0.0.1:5000/perguntar';
    
    async function fazerPergunta(pergunta) {
        try {
            respostaDiv.innerHTML = `
                <div class="loading">
                    <p>🤖 Processando sua pergunta...</p>
                </div>
            `;
            
            const response = await fetch(BACKEND_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    pergunta: pergunta
                })
            });
            
            if (!response.ok) {
                throw new Error(`Erro HTTP: ${response.status}`);
            }
            
            const dados = await response.json();
            exibirResposta(dados);
            
        } catch (error) {
            console.error('Erro ao fazer pergunta:', error);
            respostaDiv.innerHTML = `
                <div class="error">
                    <p>❌ <strong>Erro:</strong> Não foi possível processar sua pergunta.</p>
                    <p><small>Verifique se o backend Python está rodando.</small></p>
                    <p><small>Erro técnico: ${error.message}</small></p>
                </div>
            `;
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
        fazerPergunta(pergunta);
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