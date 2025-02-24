// Add any JavaScript functionality here
document.addEventListener('DOMContentLoaded', function() {
    // Example: Toggle favorite status
    const favoriteButtons = document.querySelectorAll('.favorite-btn');
    favoriteButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.classList.toggle('active');
        });
    });
});