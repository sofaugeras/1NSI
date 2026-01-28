# Activité 2 : Découverte des cartes

Dans l'activité précédente, nous avons utilisé « l'écran » composé de 25 DELS.

Mais ce n'est pas le seul intérêt de ces cartes. Dans les exercices suivant, nous allons apprendre à utiliser les différents composants.

Elles possèdent entre autres :

- Deux boutons (A et B)
- Un accéléromètre
- Un compas
- Un thermomètre
- Une antenne radio
- Une antenne bluetooth
- Un haut-parleur (seulement en v2)
- Un micro (seulement en v2)
- Un bouton tactile (seulement en v2)
- Un capteur de lumière

## 1. Les boutons

La carte **micro:bit** a deux boutons A et B situés à gauche et à droite de l'écran. On peut détecter s'ils sont pressés en utilisant les deux fonctions suivantes :

!!! info "button"
    ``button_a.is_pressed()`` qui renvoit ``True`` (vrai) si le bouton A est pressé au moment où cette fonction est exécutée, et ``False`` (faux) sinon <br />
    ``button_a.was_pressed()`` qui renvoit ``True`` (vrai) si le bouton A a été pressé depuis que la carte a été allumée, ou depuis le dernier appel de cette fonction, et ``False`` (faux) sinon <br />
    ``button_b.is_pressed()`` et ``button_b.was_pressed()`` a la même signification, mais pour l'autre bouton.

Les deux fonctions semblent à première vue très proche. Une différence apparaîtra en exécutant une action dans une boucle si le bouton est appuyé. Si le bouton est appuyé longtemps (plus d'un centième de secondes) :<br />
- avec ``is_pressed()``, l'action risquera d'être exécutée plusieurs fois ;<br />
- avec ``was_pressed()``, l'action ne sera exécutée qu'une seule fois.

En pratique, vous aurez peu à vous soucier de cette différence.

!!! question "Programme 5 : Horloge"

    1. copier-coller ce code ci-dessous dans l'[éditeur](https://python.microbit.org/v/3){target="_blank"}
    2. Vérifiez qu'en appuyant sur le bouton de droite, l'aiguille s'arrête de tourner, et qu'en appuyant sur le bouton de gauche, elle se remet à tourner.
    3. Lisez et comprenez comment le programme fonctionne.
    4. Modifiez le programme pour inverser le rôle des deux boutons.

    👍 Appelez l'enseignant pour validation ❗

    ??? info "code à copier"

        ```python linenums="1"
        from microbit import *

        # Liste des images d'aiguilles à afficher
        AIGUILLES = [
            Image.CLOCK1,
            Image.CLOCK2,
            Image.CLOCK3,
            Image.CLOCK4,
            Image.CLOCK5,
            Image.CLOCK6,
            Image.CLOCK7,
            Image.CLOCK8,
            Image.CLOCK9,
            Image.CLOCK10,
            Image.CLOCK11,
            Image.CLOCK12,
        ]

        # Etat initial : l'aiguille tourne
        etat = "tourne"

        while True:
            # Si l'état est "tourne", alors affiche la bonne aiguille.
            # Cette partie-là est un peu compliquée ; ne cherchez pas à la comprendre.
            if etat == "tourne":
                display.show(AIGUILLES[
                    (running_time() // 50) % len(AIGUILLES)
                ])

            # Si on appuie sur le bouton A, alors l'état devient "tourne"
            if button_a.is_pressed():
                etat = "tourne"

            # Sinon, si on appuie sur le bouton B, alors l'état devient "stop"
            elif button_b.is_pressed():
                etat = "stop"
        ```

!!! question "Programme 6 : Compteur"

    1. copier-coller ce code ci-dessous dans l'[éditeur](https://python.microbit.org/v/3){target="_blank"}
    2. Vérifiez qu'il fonctionne comme attendu : il doit afficher le nombre 0, et augmenter de 1 à chaque fois que vous appuyez sur le bouton B.<br />
    3. Modifiez ce programme pour diminuer le compteur de 1 lorsque vous appuyez sur le bouton A.<br />
    4. Modifiez ce programme pour remettre le compteur à 0 lorsque vous appuyez sur les deux boutons en même temps. Pour faire ceci, vous devrez :<br />

        - utiliser le mot-clef ``and`` pour tester deux conditions en même temps ;<br />
        - utiliser, pour ce test, ``is_pressed()`` plutôt que ``was_pressed()``.

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
    
## 2. Accéléromètre

Les cartes micro:bit embarquent en leur sein un accéléromètre.<br />

Cet accéléromètre, comme celui intégré dans votre téléphone, permet de détecter les mouvement et leur direction.<br />
Ainsi la carte est capable de reconnaître différent mouvement/gestes. Parmi lesquels sont : face visible, face cachée, haut, bas, gauche, droit, chute libre, 3g, 6g, 8g et secouer.<br />

Pour plus d'information, on peut se référer à la [documentation de la carte](https://microbit-micropython.readthedocs.io/en/latest/tutorials/gestures.html){target="_blank"}.

!!! question "Programme 7 : Smiley Joyeux"

    Maintenant que nous savons ce qu'est un accéléromètre, on veut programmer notre carte, afin qu'elle affiche un smiley joyeux quand on est face visible et un smiley pas content sinon.

    👍 Appelez l'enseignant pour validation ❗

    ??? tip "Indice 1"
        Tout d'abord, nous avons besoin de récupérer l'état de notre accéléromètre. Pour ce faire, on utilise le code suivant qui obtient l'état de l'accéléromètre et le stocke dans une variable.

        ```python
        geste = accelerometer.current_gesture()
        ```

    ??? tip "Indice 2"
        Maintenant que l'on à le geste, il nous faut le comparer au geste qui correspond à être face visible (face up).

        Pour ce faire, on a le code suivant qui vaut Vrai (True) si le geste est face visible et Faux (False) sinon.

        ```python
        geste == "face up"
        ```

        On prendra bien garde à noter le double égal ``==``.

        Le double égal est l'opérateur d'**égalité**, comme le symbole égal en mathématique, alors que le simple égal est l'opérateur d'**affectation**, i.e. la variable de gauche prend la valeur de l'expression de droite.

    ??? tip "Indice 3"

        Maintenant que nous savons récupérer l'état de l'accéléromètre et regarder sa valeur, il est temps de faire une action en fonction de si on est face visible ou non.

        Pour ce faire on utilise l'instruction **if else**

        ```python 
        if condition:
            # Fait ce code si la condition vaut Vrai
        else:
            # Fait cet autre code sinon
        ```
        L'instruction **if**, prend une condition en paramètre. Une condition est une expression qui vaut soit **Vrai**, soit **Faux**, comme le code de l'indice précédent. (On prendra garde à bien ajouter le "« : »" à la fin de la condition)

        **Si** la condition est **Vrai**, alors on exécute le bloc immédiatement après. (On prendra bien soin de bien décalé ce code de 4 espaces supplémentaires)

        **Sinon**, si la condition est **Fausse**, alors on exécute le bloc après else (sinon en anglais). (On prendra bien soin de bien décalé aussi ce code de 4 espaces supplémentaires)

        Une fois l'un ou l'autre des codes exécuté, on reviendra à l'exécution du code aligné avec le **if**.