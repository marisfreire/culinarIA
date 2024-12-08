const body = document.getElementById('body');
const submit_btn = document.querySelector('button');
const input = document.getElementById('input');

submit_btn.addEventListener("click", async (e) => {
    e.preventDefault();

    const data = {
        ingredientes: document.querySelector('input[name="ingredientes"]').value,
        eletrodomesticos: document.querySelector('input[name="eletrodomesticos"]').value,
        culinaria: document.querySelector('input[name="culinaria"]').value,
        restricoes: document.querySelector('input[name="restricoes"]').value,
        porcoes: document.querySelector('select[name="porcoes"]').value,
        refeicao: document.querySelector('select[name="refeicao"]').value
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