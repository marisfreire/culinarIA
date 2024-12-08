const body = document.getElementById('body');
const submit_btn = document.querySelector('button');
const input = document.getElementById('input');

submit_btn.addEventListener("click", async (e) => {
    e.preventDefault();

    const data = {
        restricoes: document.querySelector('input[name="restricoes"]').value,
        tipo: document.querySelector('input[name="tipo"]').value,
        ingredientes: document.querySelector('input[name="ingredientes"]').value,
        gastronomia: document.querySelector('input[name="gastronomia"]').value
    };

    const response = await fetch("/resposta", {
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