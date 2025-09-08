# 🐢 TP – Boucle `for` et module `turtle`

## Objectifs

* Découvrir la boucle `for` en Python.
* Utiliser la bibliothèque `turtle` pour tracer des formes géométriques.
* Comprendre la répétition d’instructions.

---

## 1. Prise en main de `turtle`

```python
import turtle

t = turtle.Turtle()
t.speed(3)

for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
```

👉 Question : Que dessine ce programme ? <br />
👉 Modifier les valeurs pour comprendre le rôle de `forward()` et `right()`.

---

## 2. Polygones réguliers

Écrire un programme qui dessine un polygone régulier à **n côtés**, chaque côté mesurant 100 pixels.

💡 Rappel : l’angle de rotation est `360 / n`.

Exemple attendu pour `n = 6` : un hexagone.

??? tip "Correction"

    ```python
    import turtle
    t = turtle.Turtle()
    t.speed(0)
    n=6
    angle = 360 / n
    for i in range(n):
        t.forward(50)
        t.right(angle)
    turtle.done()
    ```

---

## 3. Spirale carrée

Écrire un programme qui dessine une spirale de carrés :

![spirale carré](./data/spiraleCarre.png){: .center} 

??? tip "Correction"

    ```python
    import turtle

    t = turtle.Turtle()
    t.speed(0)

    for i in range(50):
        t.forward(10 + i*5)
        t.right(90)

    turtle.done()
    ```

👉 Modifier le pas de l’incrément pour obtenir différentes spirales.

---

## 4. Rosace d’étoiles

Écrire un programme qui dessine plusieurs étoiles à 5 branches en rotation.

💡 Indice :

* une étoile à 5 branches se fait avec `t.forward(100)` et `t.right(144)` dans une boucle de 5.
* répéter l’étoile en tournant un peu entre chaque dessin.

![rosace d'étoile](./data/rosaceEtoile.png){: .center} 

??? tip "correction"

    ```python
    import turtle

    # Paramètres
    nb_etoiles = 36     # nombre d’étoiles dans la rosace
    taille = 120        # longueur d’un segment de l’étoile
    rotation = 360 / nb_etoiles

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    # Dessin de la rosace d'étoiles 
    for k in range(nb_etoiles):
        # tracer une étoile à 5 branches
        for i in range(5):
            t.forward(taille)
            t.right(144)
        # légère rotation avant la prochaine étoile
        t.right(rotation)

    turtle.done()
    ```
👉 Change de [couleur](https://wiki.mchobby.be/index.php?title=Python-Turtle-Exemple2) à chaque étoile 

## 5. Défi final 🎯

Créer un programme qui demande à l’utilisateur (dans la console):

* le **nombre de côtés** d’un polygone,
* le **nombre de polygones** à dessiner,
  et affiche une figure géométrique artistique (effet rosace ou mandala).

💡 Indice :

* Utiliser `input()` pour récupérer une valeur :

```python
n = input("Combien de côtés ? ")
```

⚠️ Par défaut, `input()` renvoie une **chaîne de caractères** (`str`).
Il faut **caster** (convertir) en entier avec `int()` :

```python
n = int(input("Combien de côtés ? "))
```

* Même chose pour le nombre de polygones.

??? tip "Correction"

    ```python
    import turtle

    t = turtle.Turtle()
    t.speed(0)

    # Demande des paramètres à l'utilisateur
    n = int(input("Combien de côtés pour le polygone (>=3) ? "))
    nb = int(input("Combien de polygones à dessiner ? "))
    taille = int(input("Longueur d’un côté (en pixels) ? "))

    # Sécurisation simple
    if n < 3:
        n = 3

    # Calcul des angles
    angle_poly = 360 / n
    rotation = 360 / max(nb, 1)

    # Dessin de la rosace
    for k in range(nb):
        # dessiner un polygone régulier
        for i in range(n):
            t.forward(taille)
            t.right(angle_poly)
        # tourner un peu avant le polygone suivant
        t.right(rotation)

    turtle.done()

    ```

