document.addEventListener("DOMContentLoaded", function () {
    const togglePasswordFormBtn = document.getElementById("toggle-password-form");
    const closePasswordFormBtn = document.getElementById("close-password-form");
    const passwordForm = document.getElementById("password-form");
    const changePasswordForm = passwordForm.querySelector("form");

    togglePasswordFormBtn.addEventListener("click", function () {
        passwordForm.classList.toggle("hidden");
    });

    closePasswordFormBtn.addEventListener("click", function () {
        passwordForm.classList.add("hidden");
    });

    changePasswordForm.addEventListener("submit", async function (event) {
        event.preventDefault();

        const currentPassword = document.getElementById("current-password").value;
        const newPassword = document.getElementById("new-password").value;
        const confirmPassword = document.getElementById("confirm-password").value;

        if (!currentPassword || !newPassword || !confirmPassword) {
            alert("Todos os campos são obrigatórios.");
            return;
        }
        if (newPassword !== confirmPassword) {
            alert("As novas senhas não coincidem.");
            return;
        }
        if (newPassword.length < 8) {
            alert("A nova senha deve ter pelo menos 8 caracteres.");
            return;
        }
        try {
            const response = await fetch("./perfil/mudar-senha", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    current_password: currentPassword,
                    new_password: newPassword,
                    confirm_password: confirmPassword
                })
            });
            if (!response.ok) {
                throw new Error("Erro ao alterar senha");
            }
            else{
                alert("Senha alterada com sucesso!")
            }
        }
        catch (error) {
            alert(error);
        }

    });
});