# 5.0 Mise au point de programme : spécification

![image](data/bo.jpg){: .center}

![yoda](data/yoda_specs.jpg){: .center width=30%}

##	1. Introduction 

En tant que codeur débutant, il est indispensable de prendre les bonnes habitudes dès le départ. De nombreuses conventions se sont imposées au fil du temps devant la complexité, la taille croissante du code mais aussi parce que le partage du travail devient de plus en plus indispensable. L'accroissement de la mémoire a aussi permis d'améliorer la lisibilité du code. Et oui, il fut un temps où chaque octet était important et une variable à une lettre moins couteuse qu'une de 20, où un commentaire prenait trop de place dans le fichier...Aujourd'hui, la longueur du nom d'une variable ou d'un commentaire ne doit plus vous effrayer.


Votre code doit être facile à lire par une autre personne. Et cette autre personne peut très bien être-vous 2 ans plus tard....on est parfois surpris de ne pas comprendre ce que l'on a bien pu faire! 

##	2.  Idées générales

Voici quelques conventions propres à Python mais qui fonctionnent pour tous les langages. Elles sont disponibles sur le site de Python : [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/). Allez voir !

Je les résume en français : **beau est mieux que laid**, **explicite c'est mieux qu'implicite** (C'est évident, mais ca va mieux en le disant !), **simple mieux que complexe**, éviter si possible trop d'imbrications, aérer le code, nommer correctement les variables (i,j,k pour un increment, elt pour désigner un élément ...) etc.…

Je vais isoler la dernière idée : ==maintenant c'est mieux que jamais mais jamais est parfois préférable à immédiatement.==

:octicons-milestone-16: Oui, bien souvent, on veut tellement finir et tester notre code que l'on en oublie d'être propre et judicieux, mieux vaut faire une pause. 

##	3. Idées en pratique sur Python

Je les résume au maximum. Pour bien comprendre l'intérêt de tout cela, gardez à l'esprit que vous passerez plus de temps à relire votre code qu'à l’écrire !

:arrow_right:	En python ne mélangez jamais tabulations et espaces<br />
:arrow_right:	Une ligne de code ne devrait pas dépasser 79 caractères.<br />
:arrow_right:	Encoder en Utf-8 <br />
:arrow_right:	Importer les bibliothèques en début de programme sur des lignes séparées. (Pour en savoir plus sur les bibliothèques.) <br />

Il y a de nombreuses conventions sur les espaces. Globalement on met un (et un seul) espace avant et après les affectation, comparaisons, booléens et opérations et pas d'espace pour le reste (, {,[...


##	4. Commentaires

Les commentaires doivent être des phrases complètes de préférence en anglais. Je ne vais pas vous obliger à suivre cette règle mais soyez cohérents. Je vois très régulièrement des codes en Franglais. Des variables en français, d'autre en anglais et de même pour les noms de fonctions. Faites un choix une fois pour toute (sauf pour les commentaires pour l'instant).

En Python les commentaires commencent par un ```#```. Nous allons donc adopter pour cette année: commentaires en français et au choix noms de fonctions ET variables dans une même langue (français ou anglais).

:arrow_right:	Pensez à mettre à jour vos commentaires si vous modifiez le code !

Commenter ce n'est pas commenter chaque ligne mais plutôt indiquer les grandes étapes lorsque le code s'allonge et expliquer certaines lignes qui vous paraissent techniques.

##	5. Dans les fonctions

Nous verrons en terminale la programmation orienté objet. Pour différencier les fonctions, variables et constantes on utilise des conventions de nommage différentes.

==nomDeMaFonction== : pour les fonctions, variables et méthodes tout en minuscule avec _ pour séparer les mots ou en **CamelCase**.<br />

==maVariable== : la variable est explicite pour son rôle dans la fonction. On utilise le **CamelCase**. Usuellement, les lettres i, j, k désigne des incréments et donc des entiers. Eviter de les utiliser pour autre chose.

Les ==constantes== sont entièrement en majuscule : NOM_DE_MA_CONSTANTE. Une constante est une variable à laquelle on donne une valeur qui ne changera pas dans tout le programme. Par exemple, on code un jeu et au début, on préfère s'en tenir à deux joueurs. On peut créer ```NB_MAX_JOUEURS=2``` et on utilisera cette variable dans tout le programme sans jamais la changer. Imaginons que le code permette de jouer à trois joueurs. Il suffit de changer la valeur de la constante ```NB_MAX_JOUEURS=3```.


Intéressons-nous maintenant à la **documentation des fonctions**. Lorsque vous créez une fonction, vous devez la documenter. C'est le rôle du ==docstring==. Le docstring se place juste après la création de la fonction par def. Il commence et termine par trois guillemets **```**.

Votre docstring doit décrire le rôle de la fonction, puis les paramètres passés en arguments (type et rôle), ainsi que le type de ce qui est retourné

Ce docstring, peut être lu en tapant en console : 
`nom_de_ma_fonction.__doc__` (deux underscores de chaque côté). 


Exemple :

```python
def mettre_au_carre(x):
    """renvoie le carré de x

    Paramètres d’entrée : x -> (int, float ou decimal) : un nombre quelconque
    Paramètre de sortie : Un nombre -> (int, float ou decimal)
    """
    return(x*x)
```

!!! faq "A faire" 
    - Copier le code de la fonction mettre_au_carre dans votre editeur.
    - Testez la docstring sur la console. Si on tape `print(mettre_au_carre.__doc__)` ou `help(nom_de_la_fonction)` en console, on lira "renvoie le ....quelconque".


##	6.Exercices

!!! note "exercice 1 : mesure d'une angle"
    === "Enoncé"
        La mesure d'un angle peut être donnée en degrés ou en radian. L'unité de calcul naturelle pour les angles est le radian. La bibliothèque math ne sait donc calculer le cosinus que d'un angle donné en radian. `ma_fontion1`, convertit des degrés en radians car **pi** radians correspondent à 180°. <br />
        :arrow_right: Modifier les noms des fonctions, variables et créez la docstring selon les normes énoncées plus haut.

        ```python
            # import math
            from math import pi,cos
            def ma_fonction1(x):
                return(x*math.pi/180)

            def ma_fonction2(x):
                return(math.cos(ma_fonction1(x)))
        ```
        Petite remarque, on a importé le module math de la bibliothèque standard (la bibliothèque de Python) avec `import math`. Dans ce cas, le programme charge en mémoire toutes les fonctions de la bibliothèque `math`. Ce qui est bien inutile dans notre cas, ou l on a besoin que de la fonction `pi` et `cos`.
        J importe uniquement ce que je vais utiliser. Les fonctions sont chargées en mémoire et donc directement connues dans mon programme (je tape `cos` directement, plus `math.cos`). 

    === "Correction"

        ```python
        from math import cos, pi
 
        def conversion_degre_radian(angle):
            """renvoie la conversion des données en radians
            
            Paramètres d'entrée : x -> int ou decimal : valeur de l'angle de degré à convertir
            Paramètres de sortie : retourne --> int ou float : valeur de l'angle en radian
            
            """
            return(angle*pi/180)

        def calcul_cosinus(angle):
            """renvoie le cosinus d'un angle
            
            Paramètres d'entrée : x -> int ou decimal : valeur de l'angle en radian
            Paramètres de sortie : retourne --> int ou float : cosinus en radian
            
            """
            return(cos(conversion_degre_radian(angle)))
        ```

!!! note "exercice 2 : Mystère"
    === "Enoncé"
        Comprendre ce que fait le code suivant et corriger tous les problèmes de spécification.

        ```python
        def fonction(a,b):
            return(a*100/b)
        ```
    === "Correction"

        ```python
        def pourcentage(a,b):
            """
            renvoie le pourcentage de a par rapport à b
            Paramètres d'entrée : 
                a -> int ou decimal : valeur du sous-ensemble
                b -> int ou decimal, b>0 : valeur de l'ensemble
            Paramètres de sortie : retourne --> int ou float : pourcentage
            
            """
            assert b != 0
            return(a*100/b)
        ```

!!! note "exercice 3 : Mystère"
    === "Enoncé"
        Comprendre ce que fait le code suivant et corriger tous les problèmes de spécification

        ```python
        def fonction1(a,b,c,d):
            return(a+b+c+d)

        def fonction2(a,b,c,d):
            return(fonction1(a,b,c,d)/4)
        ```
    === "Correction"

        ```python
        def addition(a,b,c,d):
            """renvoie l'addition des 4 paramètres
            Paramètres d'entrée : 
                a,b,c,d -> int ou decimal : valeur à additionner
            Paramètres de sortie : retourne --> int ou float : addition
            
            """
            return(a+b+c+d)

        def division(a,b,c,d):
            """renvoie la moyenne des 4 paramètres
            Paramètres d'entrée : 
                a,b,c,d -> int ou decimal : valeur
            Paramètres de sortie : retourne --> int ou float : moyenne
            
            """
            return(addition(a,b,c,d)/4)
        ```

!!! note "exercice 4 : Mystère"
    === "Enoncé"
        Comprendre ce que fait le code suivant et corriger tous les problèmes de spécification.<br />
        Que dois-je taper pour avoir l'aire d'un rectangle de côté 3 et 4, agrandit 10 fois? <br />
        Que dois-je taper pour que le programme affiche le volume d'un pavé droit de mesure 5 ; 7 ; 6 cm, agrandit 3 fois?

        ```python
        import math

        def fonction1(a,b):
            coefficient=10
            c=coefficient*coefficient*a*b
            print("L'aire d'un rectangle de mesure",a,"et",b,"qui subit un agrandissement de coefficient",coefficient,"est",c)

        #volume d'un parallélépipède de coté a,b,c qui subit un agrandissement de coefficient d
        def fonction2(a,b,c,d):
            return(a*b*c*d*d*d)
        ```
    === "Correction"

        ```python
        def aire(a,b):
            """renvoie l'aire d'un rectangle dont les 2 côtés adjacents sont passés en paramètres
            Paramètres d'entrée : 
                a -> int ou decimal : côté
                b -> int ou decimal : côté adjacent
            Paramètres de sortie : retourne --> none
            """
            COEFFICIENT=10
            aire_rectangle=a*b*COEFFICIENT**2
            print("L'aire d'un rectangle de mesure",a,"et",b,"qui subit un agrandissement de coefficient",COEFFICIENT,"est",aire_rectangle)

        #volume d'un parallélépipède de coté a,b,c qui subit un agrandissement de coefficient d
        def volume(a,b,c,d):
            """renvoie le volume d'un parallépipède dont les 2 côtés adjacents sont passés en paramètres
            Paramètres d'entrée : 
                a -> int ou decimal : côté
                b -> int ou decimal : côté adjacent
                c -> int ou decimal : hauteur
                d -> Coefficient multiplicateur
            Paramètres de sortie : retourne --> volume du parallépipède doté d'un cef multiplicateur
            """
            COEFFICIENT=d
            return(a*b*c*COEFFICIENT**3)
        ```

!!! note "exercice 5 : Mystère"
    === "Enoncé"
        Comprendre ce que fait le code suivant et corriger tous les problèmes de spécification

        ```python
        def fonction1(a):
            print("1 - jouer à la bataille navale")
            print("2 - jouer au puissance 4")
            print("3 - quitter")
            a=input("Taper votre choix 1 ou 2 ou 3:")
            while a!="1" or a!="2" or a!="3":
                a=input("Taper votre choix :")
            return(a)
        ```
    === "Correction"

        ```python
        def console_jeu_choix():
            """Fonction de menu de la console de jeu
            Paramètres d'entrée : none
            Paramètres de sortie : retourne --> choix
            """
            print("1 - jouer à la bataille navale")
            print("2 - jouer au puissance 4")
            print("3 - quitter")
            a=int(input("Taper votre choix 1 ou 2 ou 3:"))
            #Tant que l'utilisateur n'a pas choisi son menu correctement, on l'interroge
            while a!="1" or a!="2" or a!="3" :
                a=int(input("Taper votre choix :"))
            return(a)
        ```

!!! note "exercice 6 : Coder à partir de la spécification"
    === "Enoncé"
        Vous devez être capable de programmer une fonction à partir de sa spécification.

        ```python
            def encoder(chaine):
            '''
            Encode une chaîne de caractère en son équivalent ASCII 

            Paramètres d’entrée : chaine de caractère -> char
            Paramètre de sortie : encodage ASCII -> int
            '''
                # votre code ici
        ```
    === "Correction"

        ```python
        def encoder(chaine): 
            """
            Encode une chaîne de caractère en son équivalent ASCII 
            Paramètres d’entrée : chaine de caractère -> char 
            Paramètre de sortie : encodage ASCII -> int
            """
            #Initialisation de la chaine de caractère que l'on utiliser pour concaténer
            machAscii = ''
            #Parcours par élément de la chaine de caractère passée en paramètre
            for lettre in chaine :
                #ord renvoie un entier, il faut caster en string pour pour concaténer
                machAscii += str(ord(lettre))
            #On doit renvoyer un entier conformément aux spécifications, on caste en int la chaine de caractère
            return int(machAscii)
        ```

## 7. Mise au point de programme : Les tests

![Les tests](data/testing_meme3.png){: .center width=30%}

De toute évidence, le code qu'on écrit n'a aucune assurance de fonctionner si on ne le teste pas ... Un programmme peut fonctionner, dans le sens où il ne plante pas mais où il ne fait pas du tout ce qu'on lui demande ...

Ce qui doit être Tester : <br />
    :arrow_right: Cas correct <br />
    :arrow_right: Cas faux <br />
    :arrow_right: Cas limite <br />

_Exemple_ avec la fonction qui teste si des nombres sont en ordres croissants.

```python
def croissant(a,b,b):
  """Fonction de test de la croissance d’une suite de nombre
  Paramètres d'entrée : a,b,c -> int ou float
  Paramètres de sortie : retourne -> valeur booléenne 
				(True si a,b,c sont tels que a<b<c ; False sinon)
  """
	Return a<b<c

  # Jeu d'essai
  assert(croissant(1,5,9)==True) #je teste le cas où les nombres sont croissants --> Cas normal
  assert(croissant(1,5,2)==False) #je teste le cas où les nombres ne sont pas croissants --> Cas faux
  assert(croissant(7,3,4)==False) #je teste le cas où les nombres sont décroissants --> Cas faux
  assert(croissant(5,5,5)==False) #je teste le cas où les nombres sont tous égaux --> Cas limite
```

Il existe plusieurs approches en Python pour s'assurer qu'un code fonctionne.

##	8. Écrire les tests soi même :poop:

Le moyen le plus simple consiste à écrire un jeu de test après `if __name__="__main__` à l'aide de print :
```python
def ma_fonction(n):
  #code ici
  pass

if __name__ == '__main__':
    print(ma_fonction(5))
```

C'est généralement ce qu'on fait quand on développe. Ces tests doivent couvrir **tous** les cas possibles et être compréhensibles.

Selon les contextes (devoir, projet, développement en cours…) on peut les laisser ou les effacer.
Il est préférable de les remplacer par de vrais tests… 

##	9. Assert :heart:

Python intègre un mot clef `assert` qui va lever une exception `AssertionError` si la condition qui suit est fausse:
```python
>>> assert 1 == 1 # ne fait rien
>>> assert 1 == 2 # plante le programme
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```

C'est le moyen le plus efficace et rapide de tester un programme ou une fonction.<br />
Il ne faut pas intégrer les assertions à la fonction elle-même. Il est préférable de les intégrer à des fonctions de tests indépendantes du programme.

!!! example "Un exemple sur la suite de Fibonacci"
    Prenons la fonction qui affiche la suite de Fibonacci. Elle utilise une structure que vous connaissez la liste.

    ```python
        def fibonacci(n):
        '''
        Liste des termes de la suite de Fibonacci de l'indice 0 à l'indice n inclus

        Paramètres d’entrée :  n->int : l'indice maximal voulu
        Paramètres de sortie : suite_fibonacci -> list : la liste des termes
        '''
        if type(n) != int or n < 0:
            return None
        x = 1
        y = 1
        suite_fibonacci = [x]
        indice = 0
        while indice < n:
            x, y = y, x + y
            suite_fibonacci.append(x)
            indice += 1
        return suite_fibonacci
    ```

    On peut tester plusieurs choses :<br />
    :arrow_right:	La taille de la liste : n + 1 <br />
    :arrow_right:	Différents résultats : 0, 1, 5 etc.<br />
    :arrow_right:	Les éléments de la liste sont des entiers<br />
    :arrow_right:	La propriété de Fibonacci : un+un+1=un+2<br />
    :arrow_right:	La sortie dans les cas impossibles : paramètre négatif, paramètre non entier

    ```python
    def tester_fibonacci():
        '''
        Teste certaines propriétés de la fonction Fibonacci

        Paramètres de sortie : None
        Conditions d’utilisation : lève une exception AssertionError 
                si la fonction est mal programmée
        '''
        fib_10 = fibonacci(10)

        # longueur de la liste
        assert len(fib_10) == 11

        # différents résultats
        assert fibonacci(0) == [1]
        assert fibonacci(1) == [1, 1]
        assert fibonacci(5) == [1, 1, 2, 3, 5, 8]

        # ses éléments sont entiers
        for terme in fib_10:
            assert type(terme) == int

        # La propriété de récurrence
        assert fib_10[-3] + fib_10[-2] == fib_10[-1]

        # Valeur de retour dans les cas impossibles
        assert fibonacci(-1) == None
        assert fibonacci('a') == None
        assert fibonacci(3.14) == None
    ```

## 9. Doctest

Note : La rédaction de la Docstring est libre. Les deux notations suivantes sont correctes. Prenez celle qui vous paraît naturelle.

!!! abstract "Doctest de fibonacci"
    ```python
        '''
        Teste certaines propriétés de la fonction Fibonacci

        Paramètres de sortie : None
        Conditions d’utilisation : lève une exception AssertionError 
                si la fonction est mal programmée
        '''
        ou

        """
        Calcule produit de a et b
        @param a: (number, str, list) premier facteur
        @param b: (number, str, list) second facteur
        @return: (number, str, list) le produit

        """
    ```

Mais revenons à l’utilisation de `Doctest`, qui s’intègre naturellement à la **docstring**.
Python permet grâce au module `doctest` d'intégrer les tests à la ^^documentation^^.
Il est parfois délicat de tester certaines fonctions, en particulier les affichages.
Pour les fonctions qui réalisent des calculs cela reste pratique.

!!! example "Un exemple qui fonctionne bien : "

    ```python
    def multiple (a, b):
        """
        Calcule produit de a et b
        @param a: (number, str, list) premier facteur
        @param b: (number, str, list) second facteur
        @return: (number, str, list) le produit

        >>> multiply(4, 3)
        12
        >>> multiply('a', 3)
        'aaa'
        """
        return a * b

    if __name__ == '__main__':
        import doctest
        doctest.testmod() # s'il ne se passe rien, les test sont justes
    ```
    Quand on exécute le programme, il ne se passe rien.

!!! example "Un exemple qui échoue :"

    ```python
    def Fonction_mal_testee():
        '''
        Simple fonction qui echoue
        >>> Fonction_mal_testee()
        3
        '''
        return 2


    if __name__ == "__main__":
        import doctest
        doctest.testmod()  # s'il ne se passe rien, les tests sont justes.
    ```

    Voici la sortie d'un exemple qui échoue

    ```
    >>> python3 2_tester_doctest.py
    **********************************************************************
    File "/home/quentin/realiser_des_tests/2_tester_doctest.py", line 5,
    in __main__.Fonction_mal_testee
    Failed example:
        Fonction_mal_testee()
    Expected:
        3
    Got:
        2
    ￼
    **********************************************************************
    1 items had failures:
    1 of   1 in __main__.Fonction_mal_testee
    ***Test Failed*** 1 failures.
    ```

!!! note "A faire"
    === "Enoncé"
        Reprendre le code de la fonction `mettre_au_carre` et indiquer les asserts nécessaires pour tester la fonction.

        ```python
        def mettre_au_carre(x):
            """renvoie le carré de x

            Paramètres d’entrée : x -> (int, float ou decimal) : un nombre quelconque
            Paramètre de sortie : Un nombre -> (int, float ou decimal)
            """
            return(x*x)

        ```

    === "Correction"

        ```python
        assert mettre_au_carre(2)==4
        assert mettre_au_carre(0)==0
        assert mettre_au_carre(-3)==9
        ```

!!! info "Pour aller plus loin : "
    [Des tests unitaires en python](https://www.test-recette.fr/tests-techniques/deployer-tests-unitaires/comprendre-tests-unitaires-exemples-en-pythton/)

    [les docstrings](https://sametmax.com/les-docstrings/)



