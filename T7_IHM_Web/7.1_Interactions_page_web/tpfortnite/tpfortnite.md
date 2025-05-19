# TP Fortnite

!!! info "🎯 Objectifs pédagogiques"

    - Comprendre et manipuler le DOM.
    - Savoir écouter et réagir à des événements utilisateurs (clic, survol, saisie clavier…).
    - Structurer une page web en HTML + CSS.
    - Créer des interactions avec JavaScript.

## 📝 Consignes 

Vous allez compléter une page web sur le thème de Fortnite. Le formulaire servira à simuler une inscription à un tournoi Fortnite. Vous devrez :

- Ajouter du style avec CSS.
- Compléter un fichier JavaScript pour gérer les événements suivants :
- Vérifier que tous les champs sont remplis au clic sur "S'inscrire".
- Afficher un message de confirmation si tout est OK.
- Changer la couleur de fond du formulaire au survol.
- Afficher un message d'erreur en cas de champ vide.

📁 structure des fichiers :
```prompt
    tp-fortnite/
    ├── index.html
    ├── style.css
    └── script.js
```

### ✅ index.html
```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Tournoi Fortnite</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="container">
    <h1>Inscris-toi au Tournoi Fortnite !</h1>
    <form id="inscriptionForm">
      <label for="pseudo">Pseudo Fortnite :</label>
      <input type="text" id="pseudo" name="pseudo">

      <label for="email">Adresse e-mail :</label>
      <input type="email" id="email" name="email">

      <label for="niveau">Niveau de jeu :</label>
      <select id="niveau" name="niveau">
        <option value="">-- Choisir un niveau --</option>
        <option value="debutant">Débutant</option>
        <option value="intermediaire">Intermédiaire</option>
        <option value="expert">Expert</option>
      </select>

      <button type="submit">S'inscrire</button>
    </form>

    <p id="message"></p>
  </div>
  <script src="script.js"></script>
</body>
</html>

```

### 🎨 style.css

```css
body {
  font-family: 'Arial', sans-serif;
  background-image: url('https://wallpapercave.com/wp/wp7537085.jpg');
  background-size: cover;
  color: white;
  margin: 0;
  padding: 0;
}

.container {
  background-color: rgba(0, 0, 0, 0.7);
  padding: 30px;
  margin: 100px auto;
  width: 300px;
  border-radius: 10px;
  box-shadow: 0 0 15px #00f0ff;
}

h1 {
  text-align: center;
  color: #00f0ff;
}

form {
  display: flex;
  flex-direction: column;
}

label, input, select, button {
  margin: 10px 0;
}

button {
  background-color: #00f0ff;
  color: black;
  padding: 10px;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
}

button:hover {
  background-color: #0080ff;
}

#message {
  margin-top: 20px;
  text-align: center;
  font-weight: bold;
}

```
### ⚙️ script.js

```js
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('inscriptionForm');
  const pseudo = document.getElementById('pseudo');
  const email = document.getElementById('email');
  const niveau = document.getElementById('niveau');
  const message = document.getElementById('message');

  // TODO : Ajouter un événement 'submit' sur le formulaire
  form.addEventListener('submit', function(event) {
    event.preventDefault();
    
    // TODO : Vérifier que tous les champs sont remplis


  // TODO : Ajouter un événement 'mouseover' et 'mouseout' sur le formulaire pour changer la couleur de fond

});

```

??? tips "Correction"
```js
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('inscriptionForm');
  const pseudo = document.getElementById('pseudo');
  const email = document.getElementById('email');
  const niveau = document.getElementById('niveau');
  const message = document.getElementById('message');

  // TODO : Ajouter un événement 'submit' sur le formulaire
  form.addEventListener('submit', function(event) {
    event.preventDefault();
    
    // TODO : Vérifier que tous les champs sont remplis
    if (pseudo.value.trim() === '' || email.value.trim() === '' || niveau.value === '') {
      message.textContent = "Tous les champs doivent être remplis !";
      message.style.color = "red";
    } else {
      message.textContent = "Inscription réussie ! Rendez-vous sur l'île.";
      message.style.color = "lime";
    }
  });

  // TODO : Ajouter un événement 'mouseover' et 'mouseout' sur le formulaire pour changer la couleur de fond
  form.addEventListener('mouseover', function() {
    form.style.backgroundColor = "#222";
  });

  form.addEventListener('mouseout', function() {
    form.style.backgroundColor = "transparent";
  });
});

```

## 💡 Bonus 
- Ajouter un effet sonore lors du clic sur le bouton submit.
- Faire apparaître une animation ou image Fortnite en cas d’inscription réussie.