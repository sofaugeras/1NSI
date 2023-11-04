!!! example "Exercice 1"
    === "Enoncé"
        Écrire une fonction **nb_chiffres** qui prend en paramètre une chaîne de caractère et qui renvoie le nombre de chiffres contenus dans la chaîne

        ```python
        def nb_chiffres(chaine):
            compteurb = 0
            #Parcours de la chaine de caractères
                #Si je rencontre un chiffre
                #ALors j'incrémente mon compteur
            
            return  compteur 

        print(nb_chiffres('rb'))
        ```

        ```python
        chaine = "Lycée Saint Sauveur - 35600 Redon"
        assert nb_chiffres(chaine)==5
        ```

    === "Correction"

        ```python
        def nb_chiffres(chaine):
            cpt =0
            for i in range(len(chaine)):
                if chaine[i] in "0123456789":
                    cpt += 1
            return  cpt
        ```


!!! example "Exercice 2"
    === "Enoncé"
        Écrire une fonction **is_email** qui prend en paramètre une chaîne de caractère et renvoie True si celle-ci est une adresse mail. On va simplifier en considérant qu'on a une adresse email si la chaîne possède les 2 propriétés suivantes : 
        - Un seul caractère @
        - Un seul caractère .(point) après @.

        ```python
        def is_email(chaine):
            # YOUR CODE HERE
            
            return 
        ```

        ```python
        assert is_email("olivier.lecluse@monfai.com")
        assert not is_email("olivier.lecluse_AT_monfai.com")
        assert not is_email("olivier.lecluse@monfai")
        ```

    === "Correction" 

        ```python
        def is_email(chaine):
            if chaine.count('@') == 1 :
                index = chaine.index('@')
                if chaine[index:].count('.') == 1 :
                    return True
        ```

!!! example "Exercice 3"
    === "Enoncé"
        Un nombre est un palindrome s'il s'écrit de la même manière de gauche à droite ou de droite à gauche. Exemple : 12521.<br />
        Ecrire une fonction **est_palindrome** prenant en paramètre un nombre et renvoyant ***True*** ou ***False*** selon que c'est un palindrom ou non.

        ```python
        def est_palindrome(n):
            # YOUR CODE HERE
        ```
        ```python
        assert est_palindrome(12521)
        assert not est_palindrome(12520)
        ```

    === "Correction" 

        ```python
        def est_palindrome(n):
            chaine = str(n)
            for i in range(len(chaine)//2):
                if chaine[i] == chaine[len(chaine)-i-1] :
                    pal = True
                else : 
                    pal = False
                    break
            return pal
        ```

!!! example "Exercice 4"
    === "Enoncé"
        Ecrire une fonction **somme_chiffres** prenant un entier en paramètre et renvoyant la somme des chiffres de ce nombre.<br />
        somme_chiffres(125) renvoie 8 puisque 1+2+5=8

        ```python
        def somme_chiffres(n):
            # YOUR CODE HERE
            raise NotImplementedError()
        ```
        ```python
        assert somme_chiffres(125)==8
        ```

    === "Correction" 

        ```python
        def somme_chiffres(n):
            somme = 0
            ch = str(n)
            for i in range(len(ch)):
                somme = somme + int(ch[i])
            return somme
        ```
