document.getElementById("toggle-password-form").addEventListener("click", function() {
    document.getElementById("password-form").classList.toggle("hidden");
});
document.getElementById("close-password-form").addEventListener("click", function() {
    document.getElementById("password-form").classList.add("hidden");
});

