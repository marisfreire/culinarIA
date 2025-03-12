const body = document.getElementById('body');
const submit_btn = document.getElementById('generate');
const input = document.getElementById('input');

submit_btn.addEventListener("click", async (e) => {
    e.preventDefault();
    
    const data = {
        ingredientes: document.querySelector('input[name="ingredientes"]').value,
        culinaria: document.querySelector('input[name="culinaria"]').value,
        porcoes: document.querySelector('input[name="porcoes"]').value,
        refeicao: document.querySelector('select[name="refeicao"]').value,
        apenas_ingredientes: document.querySelector('input[name="apenas-ingredientes"]').checked,
        tempo: document.querySelector('input[name="tempo"]').value,
        nao_informa_refeicao: document.querySelector('input[name="nao-informa-refeicao"]').checked,
        nao_informa_culinaria: document.querySelector('input[name="nao-informa-culinaria"]').checked
    };
    
        const response = await fetch("/nova-receita/resposta", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error('Erro ao gerar receita');
        }

        const recipeData = await response.json();
        
        // Atualiza a interface com os dados da receita
        document.getElementById("recipeTitle").innerText = recipeData.titulo;
        document.getElementById("difficulty").innerText = recipeData.dificuldade;
        document.getElementById("prepTime").innerText = recipeData.tempo_de_preparo;
        document.getElementById("mealType").innerText = recipeData.tipo_de_refeicao;
        
        // Lista de ingredientes
        const ingredientsList = document.getElementById("ingredientsList");
        if (ingredientsList) {
            ingredientsList.innerHTML = recipeData.ingredientes
                .map(ing => `<li>${ing.quantidade} ${ing.nome}</li>`)
                .join('');
        }
        
        // Lista de passos
        const recipeSteps = document.getElementById("recipeSteps");
        if (recipeSteps) {
            recipeSteps.innerHTML = recipeData.passos
                .map((step, index) => `<li>${index + 1}. ${step}</li>`)
                .join('');
        }

        // Mostra a seção de resultado
        document.getElementById("recipeForm").classList.add("hidden");
        document.getElementById("recipeResult").classList.remove("hidden");
});

// Preenchendo os dados na tela
document.getElementById("recipeTitle").innerText = recipeData.title;
document.getElementById("difficulty").innerText = recipeData.difficulty;
document.getElementById("prepTime").innerText = recipeData.prepTime;
document.getElementById("mealType").innerText = recipeData.mealType;

// Ingredientes
document.getElementById("ingredientsList").innerHTML = recipeData.ingredients.map(ing => `<li>${ing}</li>`).join('');

// Passos
document.getElementById("recipeSteps").innerHTML = recipeData.steps.map(step => `<li>${step}</li>`).join('');

// Funcionalidade do botão de favoritar
const favoriteBtn = document.getElementById("favoriteBtn");
favoriteBtn.addEventListener("click", () => {
    recipeData.isFavorite = !recipeData.isFavorite;
    favoriteBtn.style.color = recipeData.isFavorite ? "orange" : "gray";
});

function updateCookTime() {
    document.getElementById("cookTimeValue").innerText = document.getElementById("cookTime").value;
}

function updatePorcaoQntd() {
    document.getElementById("porcaoqntdvalue").innerText = document.getElementById("porcaoqntd").value;
}

function generateRecipe() {
    document.getElementById("recipeForm").classList.add("hidden");
    document.getElementById("recipeResult").classList.remove("hidden");
}

function backToForm() {
    document.getElementById("recipeResult").classList.add("hidden");
    document.getElementById("recipeForm").classList.remove("hidden");
}

