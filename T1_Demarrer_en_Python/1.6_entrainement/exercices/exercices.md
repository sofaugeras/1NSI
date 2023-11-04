!!! example "Exercice 1"
    === "Énoncé"
        Ecrire un programme qui simule le lancer de 1000 dés et qui affiche la moyenne des résultats obtenus.

    === "Correction"
        ```python
        from random import *

        somme = 0
        for i in range(1000):
            dé = randint(1,6)
            somme = somme + dé
        moyenne = somme / 1000
        print("La moyenne des 1000 lancers est",moyenne)
        ```

!!! example "Exercice 2"
    === "Énoncé"
        Ecrire un programme qui demande à l'utilisateur un entier a et un entier n et qui calcule $a^n$ à l'aide d'une boucle <code>for</code> (on verra plus tard un algorithme plus rapide que celui-ci).<br>
        Remarque : il est interdit d'utiliser <code>**</code> ici! 

    === "Correction"
        ```python
        a = int(input("Veuillez saisir la valeurs de a (la base) : "))
        n = int(input("Veuillez saisir la valeur de n (l'exponsant) : "))
        puissance = 1
        for i in range(n):
            puissance = puissance * a
        print(a,"puissance",n,"est égal à",puissance)
        ```

!!! example "Exercice 3"
    === "Énoncé"
        Ecrire une fonction <code>aire</code> qui prend deux paramètres : la longueur d'un rectangle et sa largeur, et qui renvoie l'aire du rectangle correpondant.<br>
        Tester ensuite cette fonction en utilisant les deux <code> assert()</code> suivants.

        ```python
        assert(aire(5,3) == 15)
        assert(aire(1,2) == 2)
        ```

    === "Correction"
        ```python
        def aire(longueur,largeur):
            return longueur * largeur
        ```

!!! example "Exercice 4"
    === "Énoncé"
        Ecrire une fonction <code>rectangle()</code> qui prend trois paramètres : le nombre de lignes, le nombre de colonnes et un caractère à afficher.<br>
        Cette fonction devra afficher un rectangle .
        Par exemple l'appel <code>rectangle(2,5,'A')</code> devra afficher :<br>
        AAAAA<br>
        AAAAA<br>
        Tester ensuite votre fonction avec divers appels.

        ```python
        rectangle(2,5,'A')   # appel en respectant l'ordre des paramètres
        print()   # ligne vide séparatrice
        rectangle(caractère = 'K',nbLignes = 3,nbColonnes = 10)  # appel sans respecter l'ordre des paramètres
        ```

        __Remarque__ : En Python, il est possible de ne pas respecter l'ordre des paramètres d'une fonction lors de son appel. Dans ce cas, il faut préciser le rôle des paramètres comme par exemple : <code>rectangle( nbColonnes = 4, caractère = '+', nbLignes = 7)</code>

    === "Correction"
        ```python
        def rectangle(nbLignes,nbColonnes,caractère):
            for ligne in range(nbLignes):
                for colonne in range(nbColonnes):
                    print(caractère,end="")
                print()
        ```

!!! example "Exercice 5"
    === "Énoncé" 
        Ecrire une fonction <code>nbSecondes()</code> qui prend trois paramètres : un nombre d'heures, un nombre de minutes et un nombre de secondes (par exemple (3,47,5) pour 3 heures 47 minutes 5 secondes) et qui renvoie le nombre total de secondes correspondant.<br>
        Indiquer la valeur 0 comme valeur par défaut pour le nombre d'heures, le nombre de minutes et le nombres de secondes.<br>
        Tester ensuite cette fonction avec zéro, un, deux et trois paramètres.

    === "Correction"
        ```python
        def nbSecondes(heures = 0, minutes = 0, secondes = 0):
            return heures * 3600 + minutes * 60 + secondes

        print(nbSecondes())
        print(nbSecondes(2))
        print(nbSecondes(0,30))
        print(nbSecondes(1,30,12))       
        ```

!!! example "Exercice 6"
    === "Énoncé"  
        Ecrire une fonction <code>bissextile(année)</code> qui renvoie <code>True</code> si le paramètre correspond à une année bissextile et qui renvoie <code>False</code> sinon.<br>
        Votre fonction ne doit utiliser ni des conditions imbriquées ni <code>else</code> ni des opérateurs booléens.
        <u>remarque : </u> vous pouvez effectuer une recherche sur la façon de *calculer* une année bissextile.

    === "Correction"
        ```python
        def bissextile(année):
            if année % 400 == 0:
                return True
            if année % 100 == 0:
                return False
            if année % 4 == 0:
                return True
            return False

        print(bissextile(2021))
        print(bissextile(2020))
        print(bissextile(2000))
        print(bissextile(1900))
        ```

<h2 style="text-decoration:underline;" >Dessiner avec Turtle</h2>

La bibliothèque **turtle** permet de dessiner à l'écran.<br>
Le petit programme commenté ci-dessous permet d'obtenir un tracé intéressant :


```python
from turtle import *      # On importe la bibliothèque turtle

speed(10)                 # On règle la vitesse du tracé (un entier compris entre 1 et 10)
color('red', 'yellow')    # On fixe la couleur du tracé à 'rouge' et la couleur de rempissage à 'jaune'
begin_fill()
for i in range(36):
    forward(200)          # La tortue avance de 200 pixels 
    left(170)             # La tortue tourne vers la gauche de 170°
end_fill()
done()                    # Il faut terminer par done() pour lancer l'exécution du tracé    
```

Voici quelques fonctionnalités de turtle :

<style>
        td{
            color : green;
        }
</style>

<table>
    <tr><th style="border:1px solid #000000; background-color:pink; text-align: center;">Fonction</th><th style="text-align:center;border:1px solid #000000; background-color:pink;">Description</th></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>forward(x)</code></td><td style="border:1px solid #000000; text-align: center;">Déplace la tortue de x pixels en marche avant.</td></tr> 
    <tr><td style="border:1px solid #000000; text-align: center;"><code>backward(x)</code></td><td style="border:1px solid #000000; text-align: center;">Déplace la tortue de x pixels en marche arrière.</td></tr> 
    <tr><td style="border:1px solid #000000; text-align: center;"><code>left(x)</code></td><td style="border:1px solid #000000; text-align: center;">Fait pivoter la tortue d'un angle de x degrés vers la gauche.</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>right(x)</code></td><td style="border:1px solid #000000; text-align: center;">Fait pivoter la tortue d'un angle de x degrés vers la droite.</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>goto(x,y)</code></td><td style="border:1px solid #000000; text-align: center;">Déplace la tortue au point de corrdonnées (x,y). Attention, l'axe des y est orienté vers le haut de l'écran comme en mathématiques!</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>penup()</code></td><td style="border:1px solid #000000; text-align: center;">Lève le crayon (la tortue arrêtera de tracer).</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>pendown()</code></td><td style="border:1px solid #000000; text-align: center;">Abaisse le crayon. La tortue se remettra à tracer.</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>hideturtle()</code></td><td style="border:1px solid #000000; text-align: center;">Cache la tortue.</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>showturtle()</code></td><td style="border:1px solid #000000; text-align: center;">Fait réapparaitre la tortue.</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>speed(n)</code></td><td style="border:1px solid #000000; text-align: center;">Règle la vitesse du tracé. n est un entier compris entre 0 et 10. 1 correspond à une vitesse lente, 10 correspond à une vitesse rapide. 0 permet d'obtenir un tracé instantané.</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>done()</code></td><td style="border:1px solid #000000; text-align: center;">Lance l'exécution du tracé.</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>circle(r)</code></td><td style="border:1px solid #000000; text-align: center;">Trace un cercle de rayon r.<br>
        On peut ajouter une deuxième paramètre facultatif a si on souhaite tracer seulement tracer un arc de cercle d'angle a.</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>color(couleur1,couleur2)</code></td><td style="border:1px solid #000000; text-align: center;">Définir la couleur du tracé (couleur1) et la couleur de remplissage (couleur2).</td></tr>
    <tr><td style="border:1px solid #000000; text-align: center;"><code>width(n)</code></td><td style="border:1px solid #000000; text-align: center;">Règle l'épaisseur du trait à n pixels.</td></tr>
</table>

!!! example "Exercice 7"
    === "Énoncé"   
        Ecrire un programme qui utilise une boucle <code>for</code> pour tracer un carré de côté 100 pixels, avec un contour bleu et colorié en vert.

    === "Correction"
        ```python
        from turtle import *

        color('blue', 'green') 
        begin_fill()
        for i in range(4):
            forward(100)
            left(90)
        end_fill()
        done()
        
        ```

!!! example "Exercice 8"
    === "Énoncé"  
        Ecrire un programme qui trace 10 cercles dont les rayons sont 10, 20, 30, ..., 100.<br>
        Choisir une couleur de tracé et une couleur de remplissage.

    === "Correction"
        ```python
        from turtle import *

        color('red', 'pink') 
        speed(10)
        begin_fill()
        for i in range(1,11):
            circle(10*i)    
        end_fill()
        done()
        ```

!!! example "Exercice 9"
    === "Énoncé"  
        Dessiner le drapeau de la France avec Turtle.

    === "Correction"
        ```python
        from turtle import *

        color('black', 'blue') 
        begin_fill()
        for i in range(2):
            forward(100)
            left(90)
            forward(200)
            left(90)
        end_fill()
        forward(100)

        color('black', 'white') 
        begin_fill()
        for i in range(2):
            forward(100)
            left(90)
            forward(200)
            left(90)
        end_fill()
        forward(100)

        color('black', 'red') 
        begin_fill()
        for i in range(2):
            forward(100)
            left(90)
            forward(200)
            left(90)
        end_fill()
        forward(100)

        done()
        ```
