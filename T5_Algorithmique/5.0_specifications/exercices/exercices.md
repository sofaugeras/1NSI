# 5.0 Exercices Spécifications et tests

!!! warning "Exigence !"
    Pour chacun des exercices ci-dessous, vous devez rédiger l'entête de la donction (docstring) puis les tests nécessaires (assert)

Les exercices ci dessous sont des révisions d'algorithmie et reprennent également ce que vous avez vu sur les listes.

Vous pouvez télécharger le fichier [notebook d'exercice](data/Exercices_specifications.ipynb).

!!! note "Exercice 1"
    === "Enoncé"
        On rappelle que la fonction `randint(a, b)` du module `random` permet de tirer un nombre au hasard entre `a` et `b` compris.  En particulier elle permet de tirer l'indice d'un élément de tableau au hasard ...

        ```python
        import random

        def tirer_une_carte():
            couleurs = ('pique','trèfle','coeur','carreau')
            valeurs = ('7', '8', '9', '10', 'V', 'D', 'R', 'AS')
            # à compléter ...
            #x = random.randint( ...
            #
            #
            #
            #
            #return ...
        ```

        ici, avec le module random, est il possible de rédiger un test d'égalité 
        exemple ``` assert tirer_une_carte() == 1 ```
        Si non, Comment peut-on  faire autrement ?

    === "correction"
        ```python
        import random

        def tirer_une_carte():
            couleurs = ('pique','trèfle','coeur','carreau')
            valeurs = ('7', '8', '9', '10', 'V', 'D', 'R', 'AS')
            indice_c = random.randint(0,3)
            indice_v = random.randint(0,7)
            coul = couleurs[indice_c]
            val = valeurs[indice_v]
            return (val, coul)

        assert tirer_une_carte()[0] is not None
        assert tirer_une_carte()[1] is not None
        #ou
        assert len(tirer_une_carte())==2
        ```

!!! note "Exercice 2"
    === "Enoncé"
        On vous donne une liste et on veut écrire une fonction qui donne le nombre d'élément dans cette liste qui sont supérieurs ou égaux à 100. <br />
        1. Ecrire la fonction documentée correspondant à ce besoin<br />
        2. rédiger les tests nécessaires pour tester tous les cas.<br />
        3. Rédiger le test pour la liste `[50*i for i in range(7)]`

    === "Correction"
        ```python
        def compter_occurences_sup100(uneliste):
        """
        fonction qui compte dans une liste le nombre d'occurrences supérieur à 100
        
        Paramètre d'entrée : uneliste : type liste : liste d'entiers.
        Paramètre de sortie : un entier : compteur d'occurrence
        """
            #initialistaion du compteur d'occurrence
            compteur = 0
            #Boucle qui analyse chaque élément de la liste
            for elt in uneliste:
                #Test de supériorité à 100 de l'élément 
                if elt >= 100:
                    #Incrémentation du compteur
                    compteur = compteur + 1
            return compteur
        
        li1 = [100,20,50,150,240,99]
        assert compter_occurences_sup100(li1) == 3
        li2 = [200,500,300]
        #Cas limite toutes les occurrences > 100
        assert compter_occurences_sup100(li2) == 3
        li3 = [1,2,3,5,2]
        #Cas limite aucune occurrence > 100
        assert compter_occurences_sup100(li3) == 0
        #Cas limite de la liste vide
        assert compter_occurences_sup100([]) == 0

        list2 = [50*i for i in range(7)]
        assert compter_occurences_sup100(list2) == 5
        ```
!!! note "Exercice 3"
    === "Fonction 1"
        Sur les fonctions suivantes, déterminer les assertions à mettre en oeuvre pour tester ces fonctions.
        Et corriger si nécessaire le code de la fonction pour qu'elle fonctionne comme l'indique sa spécifications

        ```python
        def echange_v1(liste):
        """
        modifie la liste, la met dans l'ordre inverse
        @param d'entrée : liste : type List : liste à renverser
        @param de sortie : Liste : typ List : Liste renversée
        """
            n=len(liste)
            #Il faut s'arrêter à la moitiè de la liste sinon on defait ce que l'on vient de faire
            for i in range(n//2):
                liste[i], liste[n-1-i] = liste[n-1-i], liste[i]
            #il faut retourner la liste
            return liste
        ```

    === "Fonction 2"

        ```python
        def echange_v2(liste):
            """modifie la liste, la met dans l'ordre inverse"""
            n=len(liste)
            for i in range(n//2):
                #on perd liste[i] en l'écrasant avec la valeur de liste[n-1-i]
                #Il faut passer par une variable temporaire pour ne pas perdre la valeur
                temp  = liste[i]
                liste[i]=liste[n-1-i]
                liste[n-1-i]=temp
            #il faut retourner la liste
            return liste
        ```
    === "Fonction 3"

        ```python
        def ajoutUnListe(liste):
            """modifie la liste, ajoute 1 à chacun des termes"""
            n= len(liste)
            #Il faut commencer à l'indice 0
            #et Il faut s'arrêter un cran avant la fin de la liste
            for i in range(n):
                liste[i] = liste[i]+1
            #il faut retourner la liste
            return liste
        ```

    === "Correction 1"

        ```python
        #cas 1 : liste avec un nombre pair d'items
        l1 = [1,2,3,4]
        assert echange_v1(l1) == [4,3,2,1]
        #cas 2 : liste avec un nombre impair d'items
        l2 = [1,2,3]
        assert echange_v1(l2) == [3,2,1]
        #Cas limite : liste vide
        assert echange_v1([]) == []
        ```

    === "Correction 2"

        ```python
        #cas 1 : liste avec un nombre pair d'items
        l1 = [1,2,3,4]
        assert echange_v2(l1) == [4,3,2,1]
        #cas 2 : liste avec un nombre impair d'items
        l2 = [1,2,3]
        assert echange_v2(l2) == [3,2,1]
        #Cas limite : liste vide
        assert echange_v2([]) == []
        ```
    
    === "Correction 3"

        ```python
        l3 = [1,2,3]
        assert ajoutUnListe(l3) == [2,3,4]
        #Cas limite : liste vide
        assert ajoutUnListe([]) == []
        ```

!!! note "Recherche d'extremum dans une liste :blue_heart:"
    === "Activité débranchée"
        Vous disposez d'un paquet de cartes **mélangés**.

        Vous disposez aussi d'un emplacement "support" nommée `m`.  

        ![](data/deck.png)


        :arrow_right: Exprimer oralement l'algorithme permettant de trouver quelle est la carte portant la valeur maximale.
    
    === "Création d'une fonction `maximum(liste)`"
        *Attention : nous allons recréer une fonction qui, bien sûr, existe déjà en Python, sous le nom `max()`.*
        <br />
        Ecrire l'algorithme en Python.  

        Il est expressément demandé de construire une fonction nommée `maximum()`, qui prenne en argument une liste, et qui renvoie le plus grand nombre de cette liste.

        Vous prendrez soin de **documenter** et **tester** votre fonction.

        **Exemple d'utilisation :**

        ```python
        >>> maximum([3,1,6,2])
        >>> 6
        ```

    === "Correction"

        ```python
        def maximum(liste):
            #Traitement du cas limite de la recherche sur une liste vide
            if len(liste)==0 :
                return None
            #par defaut, le plus petit élt est le premier de la liste
            m = liste[0]
            #Parcours de la liste, et on compare chaque elt avec le dernier maximum trouvé
            for k in liste :
                if k > m :
                    m = k
            #On retourne le dernier maximum trouvé
            return m    
        
        #Cas classique avec la valeur positionnée au milieu
        assert maximum([3,1,6,2])== 6
        #Cas classique avec la valeur positionnée en premier
        assert maximum([9,1,6,2])== 9
        #Cas classique avec la valeur positionnée en dernier
        assert maximum([3,1,6,9])== 9
        #Cas limite d'une liste vide
        assert maximum([]) == None
        ```

!!! note "Calcul de la moyenne des termes d'une liste :blue_heart:"
    === "Enoncé"
        Créer une fonction `moyenne()` qui prenne en argument une liste et qui renvoie la moyenne des nombres de cette liste.

        Vous prendrez soin de **documenter** et **tester** votre fonction.

    === "Correction"

        ```python
        def moyenne(liste):
            if len(liste)==0 :
                return 0
            #Initialisation de la somme des termes de la liste
            som = 0
            for k in liste :
                som += k
            return som/len(liste)

        assert moyenne([1,2,3,4,5]) == 3
        assert moyenne([]) == 0 
        ```

