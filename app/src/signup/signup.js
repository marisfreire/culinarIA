document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('signup-form');
    const pg1 = document.getElementById('pg1');
    const pg2 = document.getElementById('pg2');
    
    function nextPage() {
        const name = form.querySelector('input[name="name"]').value;
        const email = form.querySelector('input[name="email"]').value;
        const password = form.querySelector('input[name="password"]').value;
        const confirmPassword = form.querySelector('input[name="confirm-password"]').value;
        
        if (!name || !email || !password || !confirmPassword) {
            alert('Por favor, preencha todos os campos.');
            return;
        }
        
        if (password.length < 8) {
            alert('A senha deve ter no mínimo 8 caracteres.');
            return;
        }
        
        if (password !== confirmPassword) {
            alert('As senhas não coincidem.');
            return;
        }
        
        // Avança para a próxima página
        pg1.classList.add('hidden');
        pg2.classList.remove('hidden');
    }
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData(form);
        
        try {
            const response = await fetch('./signup', {
                method: 'POST',
                body: formData
            });
            
            if (response.redirected) {
                window.location.href = response.url;
            } else {
                const data = await response.json();
                if (data.error) {
                    alert(data.error);
                }
            }
        } catch (error) {
            console.error('Erro ao fazer cadastro:', error);
            alert('Erro ao fazer cadastro. Tente novamente.');
        }
    });
    
    window.nextPage = nextPage;
});
