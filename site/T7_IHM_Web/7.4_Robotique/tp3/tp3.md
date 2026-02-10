# Activité 3 : Pour aller plus loin

Commençons maintenant à faire des petits projets et à s'amuser avec la carte. Vous n'êtes pas obligés de faire les programmes dans l'ordre. Faites ce qui vous plaît en premier.

Vous avez le droit de vous aider d'internet et même de l'IA ! du moment que vous comreniez ce que vous faites 😃 

## 8. Compte à rebour 💣
!!! question "Programme 8 : Compte à rebour ⭐⭐"

    On souhaite écrire un programme qui fasse un compte à rebours de 5 à 0.

    1. copier-coller ce code ci-dessous dans l'[éditeur](https://python.microbit.org/v/3){target="_blank"}. 
    2. Modifiez le programme pour qu'il fasse un compte à rebours de 5 à 0, en comptant une seconde entre chaque nombre.  Vous aurez besoin de lire la documentation de la fonction ``range()``, ou de « jouer » avec les arguments de ``range()`` dans le code.
    3. Modifiez le programme pour que la carte fasse défiler **Partez !** à la fin du compte à rebours.

    👍 Appelez l'enseignant pour validation ❗
    
    ??? info "code à copier"

        ```python linenums="1"
        from microbit import *

        # Initialiation du compteur à 0
        compteur = 0

        while True:
            display.show(compteur)

            # Si le bouton B est appuyé
            if button_b.was_pressed():
                # Alors augmenter la valeur du compteur de 1
                compteur = compteur + 1
        ```
## 9. ❤️ et 🎲
!!! question "Programme 9 : Mon coeur ⭐ "

    Nous allons réutiliser l'un accéléromètre vu lors de l'activité 2. Pour rappel, cela permet à la carte de détecter son inclinaison, et de nombreux mouvements. 
    
    1. copier-coller ce code ci-dessous dans l'[éditeur](https://python.microbit.org/v/3){target="_blank"}.  Et oui il n'y a presque rien 😎. Téléverser-le sur votre carte micro:bit. Elle devrait afficher un visage triste, puis un visage content si vous la retournez vers le haut.
    2. Lisez la liste des smiley reconnus dans la documentation, puis ajouter trois lignes à ce programme pour que la carte affiche un cœur ❤️ si la carte est secouée 👋.
    2. Faites évoluer votre code, pour le transformer en un lanceur de dé 🎲. La carte devra afficher un nombre aléatoire entre 1️⃣ et 6️⃣. vous aurez besoin de la fonction [randint()](https://www.w3schools.com/python/ref_random_randint.asp)

    👍 Appelez l'enseignant pour validation ❗
    
    ??? info "code à copier"

        ```python linenums="1"
        from microbit import *
        from random import randint

        while True:
            display.show(Image.SAD)
            if accelerometer.was_gesture("face up"):
                display.show(Image.HAPPY)
                sleep(500)
        ```
## 10. Choixpeau
!!! question "Programme 10 : Choixpeau ⭐⭐ "

    L'objectif de ce travail est de réaliser un programme qui simule le Choixpeau 🎩 de l'univers d'Harry Potter.

    La carte micro:bit affiche un point d'interrogation, et attend…
    Lorsqu'elle est secouée, elle affiche, au hasard, l'un des quatre mots Poufsouffle, Serdaigle, Serpentard, Gryffondor.
    Elle revient dans son état initial (affichage du point d'interrogation).

    copier-coller ce code ci-dessous dans l'[éditeur](https://python.microbit.org/v/3){target="_blank"}. <br />
    Ce programme est incomplet. Remplacez tous les XXX par le code correct, en vous inspirant des deux premières parties de ce TP.

    👍 Appelez l'enseignant pour validation ❗
    
    ??? info "code à copier"

        ```python linenums="1"
        from microbit import *

        MAISONS = [
            "Gryffondor",
            "Poufsouffle",
            "Serdaigle",
            "Serpentard",
            ]

        while True:
            display.show("?")
            if XXX:  # Si la micro:bit est secouée
                XXX  # Choisir et afficher l'une des quatre maisons
        ```
## 11. Pierre – Feuille – Ciseaux ✊✋✌️
!!! question "Programme 11 : Pierre – Feuille – Ciseaux ✊✋✌️ ⭐⭐"

    L’objectif de ce travail est de réaliser un programme qui simule le jeu **Pierre – Feuille – Ciseaux** sur une carte **micro:bit**.

    La carte micro:bit affiche un **point d’interrogation** ❓ et attend une action de l’utilisateur.
    
    Lorsqu’elle est **secouée**, elle choisit **au hasard** l’un des trois symboles :
    - ✊ **Pierre**
    - ✋ **Feuille**
    - ✌️ **Ciseaux**

    Le résultat est affiché à l’écran pendant quelques secondes, puis la micro:bit revient à son **état initial** (affichage du point d’interrogation).

    Copier-coller le code ci-dessous dans l’[éditeur Python micro:bit](https://python.microbit.org/v/3){target="_blank"}. <br />
    Ce programme est **incomplet**. Remplacez tous les **XXX** par le code correct, en vous inspirant des exercices précédents.

    👍 Appelez l’enseignant pour validation ❗
    
    ??? info "code à copier"

        ```python linenums="1"
        from microbit import *
        import random

        CHOIX = [
            "Pierre",
            "Feuille",
            "Ciseaux",
        ]

        while True:
            display.show("?")
            if XXX:  # Si la micro:bit est secouée
                XXX  # Choisir un élément au hasard dans la liste
                XXX  # Afficher le choix à l'écran
                XXX  # Attendre quelques secondes
                XXX  # Effacer l'écran ou revenir au point d'interrogation
        ```
## 12. Thermomètre intelligent 🌡️
!!! question "Programme 12 : Thermomètre intelligent 🌡️ ⭐⭐"

    L’objectif de ce travail est de créer un **thermomètre intelligent** à l’aide de la carte **micro:bit**.

    La carte micro:bit mesure la **température ambiante** et affiche :<br />

    - un **soleil** ☀️ s’il fait chaud,
    - un **flocon** ❄️ s’il fait froid.

    Le programme doit se lancer automatiquement et se répéter en continu.

    Copier-coller le code ci-dessous dans l’[éditeur Python micro:bit](https://python.microbit.org/v/3){target="_blank"}. <br />
    Ce programme est **incomplet**. Remplacez tous les **XXX** par le code correct.

    👍 Appelez l’enseignant pour validation ❗
    
    ??? info "code à copier"

        ```python linenums="1"
        from microbit import *

        while True:
            XXX  # Lire la température
            if XXX:  # Si la température est inférieure à un seuil
                XXX  # Afficher un flocon
            else:
                XXX  # Afficher un soleil
            XXX  # Attendre quelques secondes
        ```
## 13. Maqueen 🚗
!!! question "Programme 13 : Maqueen – Robot réactif 🤖 ⭐⭐⭐"

    L’objectif de ce travail est de programmer le robot **Maqueen** afin qu’il **réagisse à son environnement**.

    La carte **micro:bit**, intégrée au robot Maqueen, pilote :

    - des **moteurs** (déplacement),
    - des **capteurs** (distance, ligne),
    - des **LED**.

    Le robot doit :

    - **avancer tout droit** ;
    - **s’arrêter** lorsqu’un obstacle est détecté ;
    - **reprendre son déplacement** lorsque l’obstacle disparaît.

    **📘 Documentation – Le robot Maqueen 🧠**

    La **micro:bit** est le **cerveau** du robot :<br />

    - elle lit les **capteurs** ;
    - elle prend une **décision** ;
    - elle commande les **moteurs**.

    📡 **Capteur de distance (ultrason)**<br />
    Le robot Maqueen possède un **capteur de distance** à ultrasons.

    - Il mesure la distance entre le robot et un obstacle.
    - La distance est exprimée en **centimètres (cm)**.

    📌 Si la distance est **faible**, cela signifie qu’un **obstacle est proche**.

    ⚙️ **Commande des moteurs**<br />
    Les moteurs permettent au robot de :
    - **avancer**,
    - **s’arrêter**,
    - **tourner**.

    Ces actions sont pilotées par des **instructions logicielles**.


    🧪 **Travail demandé**

    Compléter le programme ci-dessous afin que :

    - le robot **avance en continu** ;
    - **si un obstacle est détecté à moins de 10 cm**, le robot **s’arrête** ;
    - lorsque la distance redevient suffisante, le robot **redémarre**.

    Copier-coller le code ci-dessous dans l’[éditeur Python micro:bit](https://python.microbit.org/v/3){target="_blank"}  
    Ce programme est **incomplet**.  
    Remplacez tous les **XXX** par le code correct.

    👍 Appelez l’enseignant pour validation ❗

    ---

    ??? info "code à copier"

        ```python linenums="1"
        from microbit import *
        from maqueen import *

        while True:
            XXX  # Lire la distance devant le robot
            if XXX:  # Si la distance est inférieure à 10 cm
                XXX  # Arrêter les moteurs
            else:
                XXX  # Faire avancer le robot
            sleep(100)
        ```
