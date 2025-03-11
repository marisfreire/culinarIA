const body = document.getElementById('body');
const submit_btn = document.querySelector('button');
const input = document.getElementById('input');

submit_btn.addEventListener("click", async (e) => {
    e.preventDefault();
    
    const data = {
        ingredientes: document.querySelector('input[name="ingredientes"]').value,
        culinaria: document.querySelector('input[name="culinaria"]').value,
        porcoes: document.querySelector('select[name="porcoes"]').value,
        refeicao: document.querySelector('select[name="refeicao"]').value,
        apenas_ingredientes: document.querySelector('input[name=apenas-ingredientes]').checked
    };
    
    const response = await fetch("./resposta", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });
    
    const reader = response.body.getReader();
    let output = "";
    
    while (true) {
        const { done, value } = await reader.read();
        output += new TextDecoder().decode(value);
        body.innerHTML = marked.parse(output);
        
        if (done) {
            return;
        }
    }

})

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

