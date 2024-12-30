// Fonction pour ajouter un effet de défilement fluide sur les liens
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Fonction pour afficher un message d'alerte au clic sur le bouton de déconnexion
document.querySelector('a[href="/logout/"]').addEventListener('click', function (e) {
    if (!confirm("Êtes-vous sûr de vouloir vous déconnecter ?")) {
        e.preventDefault();
    }
});
