const body = document.getElementById("body");
const submit_btn = document.getElementById("generate");
const input = document.getElementById("input");

async function generate_and_display() {
  try {
    const data = {
      ingredientes: document.querySelector('input[name="ingredientes"]').value,
      culinaria: document.querySelector('input[name="culinaria"]').value,
      porcoes: document.querySelector('input[name="porcoes"]').value,
      refeicao: document.querySelector('select[name="refeicao"]').value,
      apenas_ingredientes: document.querySelector(
        'input[name="apenas-ingredientes"]'
      ).checked,
      tempo: document.querySelector('input[name="tempo"]').value,
      nao_informa_refeicao: document.querySelector(
        'input[name="nao-informa-refeicao"]'
      ).checked,
      nao_informa_culinaria: document.querySelector(
        'input[name="nao-informa-culinaria"]'
      ).checked,
    };

    const response = await fetch("/nova-receita/resposta", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error("Erro ao gerar receita");
    }

    const recipeData = await response.json();

    // Atualiza a interface com os dados da receita
    document.getElementById("recipeTitle").innerText = recipeData.titulo;
    document.getElementById("difficulty").innerText = recipeData.dificuldade;
    document.getElementById("prepTime").innerText = recipeData.tempo_de_preparo;
    document.getElementById("MealType").innerText = recipeData.tipo_de_refeicao;

    // Atualiza o botão de favorito com o ID da receita
    const favoriteBtn = document.getElementById("favoriteBtn");
    if (favoriteBtn && recipeData.recipe_id) {
      favoriteBtn.setAttribute("data-recipe-id", recipeData.recipe_id);
    }

    // Lista de ingredientes
    const ingredientsList = document.getElementById("ingredientsList");
    if (ingredientsList) {
      ingredientsList.innerHTML = recipeData.ingredientes
        .map((ing) => `<li>${ing.quantidade} de ${ing.nome}</li>`)
        .join("");
    }

    // Lista de passos
    const recipeSteps = document.getElementById("recipeSteps");
    if (recipeSteps) {
      recipeSteps.innerHTML = recipeData.passos
        .map((step, index) => `<li>${index + 1}. ${step}</li>`)
        .join("");
    }

    // Atualiza a lista de compras
    const shoppingListItems = document.getElementById("shoppingListItems");
    if (shoppingListItems) {
      shoppingListItems.innerHTML = recipeData.ingredientes
        .map((ing) => `<li>${ing.quantidade} de ${ing.nome}</li>`)
        .join("");
    }

    // Atualiza o título da lista de compras
    document.getElementById("shoppingListRecipeTitle").innerText =
      recipeData.titulo;

    // Mostra a seção de resultado
    document.getElementById("loading").classList.add("hidden");
    document.getElementById("recipeResult").classList.remove("hidden");
  } catch (error) {
    console.error("Erro:", error);
    alert("Erro ao gerar a receita. Por favor, tente novamente.");
  }
}

function loading_screen() {
  document.getElementById("recipeForm").classList.add("hidden");

  text = [
    "Preparando uma receita maravilhosa...",
    "Buscando as melhoras receitas...",
    "Sua receita já está quase pronta!",
  ];

  const elementText = document.querySelector("#loader-text");
  num = Math.floor(Math.random() * text.length);
  elementText.innerText = text[num];

  setInterval(function () {
    num = Math.floor(Math.random() * text.length);
    elementText.innerText = text[num]; // Pegar textos diferentes
  }, 4500);

  document.getElementById("loading").classList.remove("hidden");
}

// Event listener para o botão de favorito
document.addEventListener("DOMContentLoaded", () => {
  const favoriteBtn = document.getElementById("favoriteBtn");
  if (favoriteBtn) {
    favoriteBtn.addEventListener("click", () => {
      const recipeId = favoriteBtn.getAttribute("data-recipe-id");
      if (recipeId) {
        toggleFavorite(recipeId);
      } else {
        console.error("Receita não encontrada");
        alert("Por favor, gere uma receita primeiro");
      }
    });
  }
});

// Event listeners para os botões de gerar receita
document.getElementById("generate").addEventListener("click", (e) => {
  e.preventDefault();
  loading_screen();
  generate_and_display();
});

document.getElementById("generateNew").addEventListener("click", (e) => {
  e.preventDefault();
  loading_screen();
  generate_and_display();
});

// Event listener para o botão de gerar lista de compras
document
  .getElementById("generateShoppingList")
  .addEventListener("click", (e) => {
    e.preventDefault();
    document.getElementById("recipeResult").classList.add("hidden");
    document.getElementById("shoppingList").classList.remove("hidden");
  });

// Event listener para o botão de compartilhar no WhatsApp
// document.getElementById("shareWhatsApp").addEventListener("click", () => {
//   const recipeTitle = document.getElementById("recipeTitle").innerText;
//   const ingredients = Array.from(
//     document.getElementById("ingredientsList").children
//   )
//     .map((li) => li.innerText)
//     .join("\n");
//   const steps = Array.from(document.getElementById("recipeSteps").children)
//     .map((li) => li.innerText)
//     .join("\n");

//   const message = `Confira esta receita incrível de ${recipeTitle}:\n\nIngredientes:\n${ingredients}\n\nModo de Preparo:\n${steps}\n\nEnviado via CulinarIA!`;

//   const whatsappUrl = `https://wa.me/?text=${encodeURIComponent(message)}`;
//   window.open(whatsappUrl, "_blank");
// });

// Event listener para o botão de copiar receita
document.getElementById("copyRecipe").addEventListener("click", () => {
  const recipeTitle = document.getElementById("recipeTitle").innerText;
  const ingredients = Array.from(
    document.getElementById("ingredientsList").children
  )
    .map((li) => li.innerText)
    .join("\n");
  const steps = Array.from(document.getElementById("recipeSteps").children)
    .map((li) => li.innerText)
    .join("\n");

  const message = `Confira esta receita incrível de ${recipeTitle}:\n\nIngredientes:\n${ingredients}\n\nModo de Preparo:\n${steps}\n\nEnviado via CulinarIA!`;

  navigator.clipboard
    .writeText(message)
    .then(() => {
      alert("Receita copiada para a área de transferência!");
    })
    .catch((err) => {
      console.error("Erro ao copiar receita: ", err);
    });
});

// Event listener para o botão de exportar imagem
document.getElementById("exportImage").addEventListener("click", () => {
  const shoppingList = document.getElementById("toExport");
  if (!shoppingList) {
    console.error("Elemento 'toExport' não encontrado");
    alert("Erro ao gerar imagem: elemento não encontrado");
    return;
  }

  html2canvas(shoppingList)
    .then((canvas) => {
      const ctx = canvas.getContext("2d");
      ctx.drawImage(logo, canvas.width - logo.width - 10, 10);
      const link = document.createElement("a");
      link.download = "lista-de-compras.png";
      link.href = canvas.toDataURL("image/png");
      link.click();
      alert("Imagem gerada com sucesso!");
    })
    .catch((err) => {
      console.error("Erro ao gerar imagem: ", err);
    });
});

// Event listener para o botão de copiar lista
document.getElementById("copyList").addEventListener("click", () => {
  const recipeTitle = document.getElementById(
    "shoppingListRecipeTitle"
  ).innerText;
  const ingredients = Array.from(
    document.getElementById("shoppingListItems").children
  )
    .map((li) => li.innerText)
    .join("\n");

  const message = `Confira esta lista de compras para a receita de ${recipeTitle}:\n\nIngredientes:\n${ingredients}\n\nEnviado via CulinarIA! Acesse: [link da plataforma]`;

  navigator.clipboard
    .writeText(message)
    .then(() => {
      alert("Lista copiada para a área de transferência!");
    })
    .catch((err) => {
      console.error("Erro ao copiar lista: ", err);
    });
});

async function toggleFavorite(recipeId) {
  try {
    if (!recipeId) {
      console.error("Recipe ID não encontrado");
      return;
    }

    const response = await fetch(`/nova-receita/favorito/${recipeId}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    const favoriteBtn = document.getElementById("favoriteBtn");

    if (data.is_favorite) {
      favoriteBtn.classList.add("text-orange-500");
      favoriteBtn.classList.remove("text-gray-400");
    } else {
      favoriteBtn.classList.remove("text-orange-500");
      favoriteBtn.classList.add("text-gray-400");
    }
  } catch (error) {
    console.error("Erro ao favoritar:", error);
    alert("Erro ao favoritar receita: " + error.message);
  }
}

function updateCookTime() {
  document.getElementById("cookTimeValue").innerText =
    document.getElementById("cookTime").value;
}

function updatePorcaoQntd() {
  document.getElementById("porcaoqntdvalue").innerText =
    document.getElementById("porcaoqntd").value;
}

function backToForm() {
  document.getElementById("recipeResult").classList.add("hidden");
  document.getElementById("shoppingList").classList.add("hidden");
  document.getElementById("recipeForm").classList.remove("hidden");
}

function backToRecipeResult() {
  document.getElementById("shoppingList").classList.add("hidden");
  document.getElementById("recipeResult").classList.remove("hidden");
}
