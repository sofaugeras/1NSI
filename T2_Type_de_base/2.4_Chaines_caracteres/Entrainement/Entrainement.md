!!! note "Crédit"
    @crédit : Thomas Foirien et Stéphan Van Zuijlen  

!!! warning "Téléchargement"
    Vous pouvez télécharger le notebook [ici](./TP_chaines.ipynb)

!!! example "Exercice 1"
    === "Enoncé"
        Ecrire un programme qui affiche la <strong>première</strong> lettre d'un mot saisi par l'utilisateur.

    === "Correction"

        ```python
        mot = input("Veuillez saisir un mot : ")
        print(mot[0])
        ```

!!! example "Exercice 2"
    === "Enoncé"
        Ecrire un programme qui affiche la <strong>dernière</strong> lettre d'un mot saisi par l'utilisateur.

    === "Correction"

        ```python
        mot = input("Veuillez saisir un mot : ")
        print(mot[len(mot)-1])
        ```

!!! example "Exercice 3"
    === "Enoncé"
        Ecrire une fonction <code>estPrésent(lettre,message)</code> qui renvoie <code>True</code> ou <code>False</code> selon que la lettre est présente ou non dans le message.

        ```python
        assert(estPrésent('a','abracadabra') == True)
        assert(estPrésent('r','abracadabra') == True)
        assert(estPrésent('R','abracadabra') == False)
        ```

    === "Correction"

        ```python
        def estPrésent(lettre, message) :
            return lettre in message
        ```


        ```python
        def estPrésent(lettre, message) :
            for c in message :
                if lettre == c :
                    return True
            return False
        ```


!!! example "Exercice 4"
    === "Enoncé"
        Ecrire une fonction <code>nbOccurences(lettre,message)</code> qui renvoie le nombre d'occurences d'une lettre (ou d'un caractère) dans un message.

        ```python
        def nbOccurences(lettre,message):
            pass
        ```
        ```python
        assert(nbOccurences('a','abracadabra') == 5)
        assert(nbOccurences('A','abracadabra') == 0)
        ```

    === "Correction"

        ```python
        def nbOccurences(lettre,message):
            compteur = 0
            for i in range(len(message)) :
                if lettre == message[i] :
                    compteur += 1
            return compteur
        ```

        ```python
        def nbOccurences(lettre,message):
            compteur = 0
            for c in message :
                if lettre == c :
                    compteur += 1
            return compteur
        ```


!!! example "Exercice 5"
    === "Enoncé" 
        <em>Mot inversé</em> <br>
        Ecrire une fonction <code>inverse(mot)</code> qui prend en paramètre un mot, et qui retourne ce mot à l'envers (de la droite vers la gauche).

        ```python
        assert inverse("redon") == "noder"
        assert inverse("NSI") == "ISN"
        ```
    === "Correction"

        ```python
        def inverse(mot) :
            motinverse = ""
            for i in range(len(mot)):
                motinverse += (mot[len(mot)-i-1])
            return motinverse
        ```

        ```python
        def inverse(mot) :
            motinverse = ""
            for i in range(len(mot)-1,-1,-1):
                motinverse += mot[i]
            return motinverse
        ```
        ```python
        assert inverse("redon") == "noder"
        assert inverse("NSI") == "ISN"
        ```

!!! example "Exercice 6"
    === "Enoncé" 
        <em>Suppression des voyelles</em><br>
        Ecrire un programme qui demande à l'utilisateur de saisir un mot ou un message en lettres majuscules, et qui affiche ce message en supprimant toutes les voyelles.

        ```python
        message = input("Veuillez saisir un texte en majuscules : ")
        # ...
        ```

    === "Correction"

        ```python
        message = input("Veuillez saisir un texte en majuscules : ")
        nouveauMessage = ""
        for c in message:   # on utilise ici la syntaxe raccourcie : c prend comme valeur les caractères successifs de la chaîne
            if c!='A' and c!='E' and c!='I'and c!='O' and c!='U' and c!='Y':
                nouveauMessage = nouveauMessage + c
        print(nouveauMessage)
        ```

!!! example "Exercice 7"
    === "Enoncé" 
        <em>Plus longue répétition</em><br>
        Ecrire une fonction <code>plusLongueRépétition(message)</code> qui renvoie le plus grand nombre de caractères consécutifs identiques dans le message.

        ```python
        def plusLongueRépétition(message):
            pass
        ```

        ```python
        assert(plusLongueRépétition('lycanthropiques') == 1)
        assert(plusLongueRépétition('arrosoir') == 2)
        assert(plusLongueRépétition('AAaaaaAaaaA') == 4)
        assert(plusLongueRépétition('aaa') == 3)
        assert(plusLongueRépétition('a') == 1)
        assert(plusLongueRépétition('') == 0)
        ```

    === "Correction"

            ```python
            def plusLongueRépétition(message):
                if len(message) == 0:
                    return 0
                maximum = 0
                compteur = 1
                for i in range(len(message)-1):
                    if message[i] == message[i+1]:
                        compteur = compteur + 1
                    else:
                        if compteur > maximum:
                            maximum = compteur
                        compteur = 1
                if compteur > maximum: # pour le cas où la plus longue suite se trouve à la fin du message
                    maximum = compteur
                return maximum

            ```

            ```python
            assert(plusLongueRépétition('lycanthropiques') == 1)
            assert(plusLongueRépétition('arrosoir') == 2)
            assert(plusLongueRépétition('AAaaaaAaaaA') == 4)
            assert(plusLongueRépétition('aaa') == 3)
            assert(plusLongueRépétition('a') == 1)
            assert(plusLongueRépétition('') == 0)
            ```


!!! example "Exercice 8"
    === "Enoncé" 
         <em>Distance entre deux mots</em><br>
        La <em>distance de Hamming</em> entre deux mots de même longueur est le nombre d'endroit où les lettres sont <u>différentes</u>.<br />
        Par exemple : JAPON - SAVON<br />
        La première lettre de JAPON est différente de la première lettre de SAVON, les troisièmes aussi sont différentes. <br />
        La distance de Hamming entre JAPON et SAVON vaut donc 2.
        Ecrire une fonction <code>distHamming(mot1, mot2)</code> qui calcule la distance de Hamming entre deux mots passés en paramètre.


        Aide :
        - Pour connaître la longueur d’une chaîne de caractère: ```len(machaine)```
        - Pour tester la non égalité de deux éléments: ```if el1!=ele2```
        - On utilisera un compteur
        - On testera l’égalité des longueurs des mots
        - On mettra les mots en majuscule dans une autre variable: ```m = mot.upper()```
        - Pour boucler sur les lettres d’un mot: par exemple pour les afficher

        ```python
        for i in range(len(mot)):
            print(mot[i])
        ```
        ```python
        assert distHamming("JAPON", "SAVON") == 2
        assert distHamming("NON","OUI") == 3
        ```
    === "Correction"

        ```python
        def distHamming(mot1, mot2) : 
            compteur = 0
            for i in range(len(mot1)) :
                if mot1[i] != mot2[i] :
                    compteur += 1
            return compteur            
        ```

!!! example "Exercice 9"
    === "Enoncé"  
        <em>Le latin cochon</em><br>
        On transforme un mot commençant par une consonne selon la recette suivante:
        - On déplace la première lettre à la fin du mot
        - On rajoute le suffixe UM
        <br />
        Par exemple: VITRE devient ITREVUM
        Ecrire une fonction <code>latin(message)</code> qui transforme un mot en latin cochon.

        ```python
        assert latin("VITRE")=="ITREVUM"
        assert latin("REDON")=="EDONRUM"
        assert not latin("PARIS")=="PARISUM"
        ```

        Aide : <br>
        - Une chaîne de caractère est non modifiable, il faut donc en créer une autre <br>
        - On mettra le mot en majuscule: ```m=mot.upper()``` <br>
        - L’addition de caractères se nomme concaténation ```"A"+"B"="AB"``` <br>
        - On définit une chaîne de caractère vide avec: ```chaine=""```

    === "Correction"

        ```python
        def latin(mot) :
            return mot[1:]+ mot[0]+"UM"
        ```


!!! example "Exercice 10"
    === "Enoncé"  
        <em>Test de conformité d'une chaîne</em><br>
        Les codes postaux américains (ZIP codes) doivent impérativement suivre le format suivant : 99999-9999
        (cinq chiffres suivis d'un tiret suivi de quatre chiffres).<br>  
        Les services de l'US Postal ont un sens de l'humour assez limité, et quiconque ne respectera pas rigoureusement le format verra sa lettre redirigée vers le service de tri à la main, et en ressortir après une durée difficile à prédire.<br><br>
        Ecrire une fonction <code>ZIPCodeOK</code> qui prend en paramètre une chaîne de caractères, et qui renvoie la valeur booléenne <code>True</code> ou <code>False</code> selon que la chaîne est un code postal valide ou non.<br>
        Tester votre fonction avec trois cas de figure différents.

    === "correction"

        ```python
        def estChiffre(c) :
            chiffre = "0123456789"
            return c in chiffre

        def ZIPCodeOK(code) :
            estZip = False
            #Première condition : la longueur est de 10
            #Si ce n'est pas le cas, inutile de continuer d'ou le return a ce moment la du programme
            if len(code) == 10 :
                estZip = True
            else : 
                return False
            #deuxième condition : on a des chiffres en position 0 à 4
            for i in range(0, 5) :
                if estChiffre(code[i]) : 
                    estZip = True
                else : 
                    estZip = False
            #troisième condition le 6ème caractère (à l'indice 5) est un tiret   
            # on recherche le tiret et on récupère son indice grace à la fonction find()
            if code.find('-') == 5 :
                estZip = True
            else : 
                return False
            #dernière condition : on a des chiffres en position 6 à 9
            for i in range(6, 9) :
                if estChiffre(code[i]) : 
                    estZip = True
                else : 
                    estZip = False
            return estZip

        ```

        ```python
        assert ZIPCodeOK("99999-9999") 
        assert not ZIPCodeOK("4444-55555")
        assert not ZIPCodeOK("1111-22-333")
        assert ZIPCodeOk("17581-1681")
        ```

    === "Code élégant"
        Remarque : Ce genre de problème peut être traité de façon très concise et efficace à l'aide des "expressions régulières" (regular expressions en anglais, abrégées en regexpr ou regex ou re), comme le montre le code ci-dessous.<br>
                Dans cet exercice, vous ne pouvez utiliser que les notions vues en classe (boucles, conditions...).

                ```python
                import re

                def ZIPCodeOk(chaine):
                    return re.compile("\d{5}-\d{4}").fullmatch(chaine) is not None
                    
                print(ZIPCodeOk("17581-1681"))
                ```