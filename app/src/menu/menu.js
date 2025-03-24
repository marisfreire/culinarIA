function openModal(recipe) {
    const modal = document.getElementById('recipeModal');
    // Preenche os dados
    document.getElementById('modalTitle').textContent = recipe.title;
    document.getElementById('modalDifficulty').textContent = recipe.difficulty;
    document.getElementById('modalTime').textContent = recipe.time;
    document.getElementById('modalMealType').textContent = recipe.meal_type;
    
    // Preenche as tags
    const tagsContainer = document.getElementById('modalTags');
    if (recipe.tags ) {
        tagsContainer.innerHTML = recipe.tags
            .map(tag => `
                <span class="bg-[#00BF63] font-semibold text-white px-3 py-1 rounded-full text-s inline-block">
                        ${tag}
                    </span>
            `).join('');
    } else {
        tagsContainer.innerHTML = '';
    }
    
    // Preenche ingredientes
    const ingredientsList = document.getElementById('modalIngredients');
    ingredientsList.innerHTML = recipe.ingredients
        .map(ing => `<li>${ing.quantidade} de ${ing.nome}</li>`)
        .join('');
    
    // passos
    const stepsList = document.getElementById('modalSteps');
    stepsList.innerHTML = recipe.instructions
        .map(step => `<li>${step}</li>`)
        .join('');
    
    // Mostra o modal
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    document.getElementById('recipeModal').classList.add('hidden');
    document.body.style.overflow = 'auto';
}

// event listeners para o botão expandir
document.addEventListener('DOMContentLoaded', () => {
    const expandButtons = document.querySelectorAll('.expand-recipe-btn');
    expandButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            const recipeData = JSON.parse(button.dataset.recipe);
            openModal(recipeData);
        });
    });
}); 