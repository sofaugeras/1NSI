!!! example "Manipulation de tableau"
    === "Énoncé"
        On considère la suite d'instructions donnée ci-contre. 
        Quelles sont les valeurs affectées aux variables a, b et c à la fin de cette séquence d'instructions ?
        ```python linenums='1'
        tuple1 = (19, -2.2, 888)
        tuple2 = ("Mlle", "Mme", "M.")
        a, b, c = tuple1
        c, a = a, c
        d, e, f = tuple2
        (b, a) = (f, e)
        ```

    === "Correction"
        a vaut Mme 

        b vaut M. 

        c vaut 19

!!! example "Manipulation de tableau"
    === "Énoncé"
        On rappelle que la fonction randint(a, b) du module random retourne un nombre entier aléatoire compris entre a et b (b compris).

        1.	Écrire une fonction ```lancer_trois_des``` permettant de retourner une liste de 3 nombres entiers simulant le lancer de 3 dés cubiques.

        2. On appelle cette fonction avec l'instruction suivante :
        ```
        mon_lancer = lancer_trois_des()
        ```
        Quel est le type de la variable mon_lancer ?

        3. Quelle instruction permet alors de calculer la somme des trois dés ?
            - [ ] somme = mon_lancer[1] + mon_lancer[2] + mon_lancer[3]
            - [ ] somme = mon_lancer[0] + mon_lancer[1] + mon_lancer[2]
            - [ ] somme = mon_lancer + mon_lancer + mon_lancer

        4.	On appelle cette fonction avec l'instruction suivante :
            ```de_1, de_2, de_3 = lancer_trois_des()```

            Cette instruction génère-t-elle une erreur ? 
            
            Si oui, pourquoi ? Si non, donner une instruction permettant d'affecter à une variable la somme des trois dés.

    === "Correction"
        1. Question 1 : 

            ```python linenums='1'
            import random

            def lancer_trois_des():
                a = random.randint(1, 6)
                b = random.randint(1, 6)
                c = random.randint(1, 6)
                return a, b, c
            ```
        2. c'est une liste
        3. 
            - [ ] somme = mon_lancer[1] + mon_lancer[2] + mon_lancer[3]
            - [x] somme = mon_lancer[0] + mon_lancer[1] + mon_lancer[2]
            - [ ] somme = mon_lancer + mon_lancer + mon_lancer
        4. Non mais on peut écrire ```somme = de_1 + de_2 + de_3```

!!! example "Manipulation de tableau"
    === "Énoncé"
        On considère la suite d'instructions données ci-contre.
        Donner l'état des deux tableaux à la fin de la suite d'instructions.

        ```python 
            tab_x = [7, 77, 777, 7777]
            tab_y = [5, 55, 555, 5555]
            tab_x[2] = tab_y[1]
            tab_y[3] = tab_x[0]
            tab_x[1] = tab_x[2]
            tab_y[1] = tab_y[3]
        ```

    === "Correction"
        tab_x vaut [7, 55, 55, 7777]

        tab_y vaut [5, 7, 555, 7]

!!! example "Manipulation de tableau"
    === "Énoncé"
        On considère la suite d'instructions données ci-contre.
        Donner les valeurs de chacune des variables a à f.
        ```python linenums='1'
        tab = ['z', 'yy', 'xxx', 'wwww', 'paf']

        a = len(tab)
        b = tab[ len(tab)–1 ]
        c = tab[-1]
        d = tab[ len(tab)–2 ]
        e = tab[-2]
        f = tab[-3]
        ```
    === "Correction"
        ```python linenums='1'
        a=5 
        b='paf'
        c='paf'
        d='wwww'
        e='wwww'
        f='xxx'
        ```

!!! example "Manipulation de tableau"
    === "Énoncé"
        Pour chacune des instructions ci-dessous, écrire le tableau qui a été créé.
        ```python linenums='1'
        tab_a = [ 2**x for x in range(11) ]
        tab_b = [ 7 * x%2 for x in range(11) ]
        tab_c = [ 7 * ((10**x) // 9) for x in range(1, 5) ]
        tab_d = [ 'M. ' + car + ' ?' for car in 'XYZ' ]
        ```
    
    === "Correction"
        ```python linenums='1'
        tab_a vaut [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        tab_b vaut [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        tab_c vaut [7, 77, 777, 7777]
        tab_d vaut ['M. X ?', 'M. Y ?', 'M. Z ?']
        ```

!!! example "Manipulation de tableau"
    === "Énoncé"
        On rappelle que la fonction len() permet de retourner la longueur d'un tableau mais aussi la longueur d'une chaîne de caractères.

        1. Combien de noms vont être affichés à l'issue de la séquence d'instructions ci-dessous ? 
        ```python linenums='1'
        grands_noms = ["Lovelace", "Clarke", "Goldstine", "Hopper", "Recoque", "Hamilton"]
        for nom in grands_noms:
            if "o" in nom:
                print(nom)
        ```
        2. Quelle sera la valeur de quantite_mystere à la fin de la sequence d'instructions ci-dessous 
        ```python linenums='1'
        grands_noms = ["Lovelace", "Clarke", "Goldstine", "Hopper", "Recoque", "Hamilton"]
        quantite_mystere = 0
        for nom in grands_noms:
            quantite_mystere = quantite_mystere + len(nom)

        ```
    
    === "Correction"
        1. Cinq. Tout ceux qui comporte un O dans leur nom
        2. 44 (somme des nombres de caractères de chacun des noms)

!!! example "Manipulation de tableau"
    === "Énoncé"
        On représente la matrice donnée ci-contre grâce au tableau ma_belle_matrice.
        ```python linenums='1'
        ma_belle_matrice = [ ['a', 'b', 'c', 'd'],
                             ['e', 'f', 'g', 'h'],
                             ['i', 'j', 'k', 'l'],
                             ['m', 'n', 'o', 'p'],
                             ['q', 'r', 's', 't'] ]
        a = ma_belle_matrice[3]
        b = ma_belle_matrice[3][2]
        c = ma_belle_matrice[1][2]
        d = ma_belle_matrice[2][1]
        ```

        1. Donner les valeurs de chacune des variables a, b, c et d
        2. Proposer une suite d'instructions permettant de modifier ```ma_belle _matrice``` afin qu'elle corresponde à la matrice donnée ci-contre.
            <table>
                <tr>
                    <td>a</td>
                    <td>b</td>
                    <td>X</td>
                    <td>d</td>
                </tr>
                <tr>
                    <td>X</td>
                    <td>X</td>
                    <td>X</td>
                    <td>X</td>
                </tr>
                <tr>
                    <td>i</td>
                    <td>j</td>
                    <td>X</td>
                    <td>l</td>
                </tr>
                <tr>
                    <td>m</td>
                    <td>n</td>
                    <td>X</td>
                    <td>p</td>
                </tr>
                <tr>
                    <td>q</td>
                    <td>r</td>
                    <td>X</td>
                    <td>t</td>
                </tr>
            </table>

    === "Correction"
        1. a vaut ['m', 'n', 'o', 'p']<br />
           b vaut o, c vaut g, d vaut j

        2. une possibilité est 

        ```python linenums='1'
            #Pour la première ligne
            ma_belle_matrice[1] = ['X', 'X', 'X', 'X']
            #Pour la troisième colonne
            for ligne in range(5):
                ma_belle_matrice[ligne][2] = 'X'
        ```

!!! example "Manipulation de tableau"
    === "Énoncé"
        Colorier les bonnes cases en fonction de l'algorithme proposé

        1. Cas n°1 
        ```python linenums='1'
        for i in range(0, 8):
            for j in range(0, i):
                 M[i][j] = 'X'
        ```

        2. Cas n°2
        ```python linenums='1'
        for i in range(0, 8):
            for j in range(i+1, 8):
                M[i][j] = 'X'
        ```

         3. Cas n°3
        ```python linenums='1'
        for i in range(1, 8):
            for j in range(0, 8-i):
                M[i][j] = 'X'
        ```

         4. Cas n°4
        ```python linenums='1'
        for i in range(0, 8):
            for j in range(3, 5):
                M[i][j] = 'X'
        ```

         2. Cas n°5
        ```python linenums='1'
        for i in range(3, 5):
            for j in range(1, 7):
                M[i][j] = 'X'
        ```

         2. Cas n°6
        ```python linenums='1'
        for i in range(1, 8):
            for j in range(8-i, 8):
                M[i][j] = 'X'
        ```
    === "Correction Cas n°1"
        
        ![correction du cas n°1](data/cas1.jpg)

    === "Correction Cas n°2"

        ![correction du cas n°2](data/cas2.jpg)

    === "Correction Cas n°3"

        ![correction du cas n°3](data/cas3.jpg)
    
    === "Correction Cas n°4"

        ![correction du cas n°4](data/cas4.jpg)
    
    === "Correction Cas n°5"

        ![correction du cas n°5](data/cas5.jpg)

    === "Correction Cas n°6"
    
        ![correction du cas n°6](data/cas6.jpg)





