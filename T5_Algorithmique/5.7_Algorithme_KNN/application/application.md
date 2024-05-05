# Le Choixpeau Magique

![a l'école des sorciers](./data/ecoleDesSorciers.png){: .center width=70%}
![choipeau](./data/choipeau.jpg){: .center width=25%}

Lien vers la documentation de la librairie [PANDAS](https://pandas.pydata.org) (en anglais)

!!! note "Crédits"
    « Aidons le choixpeau magique », Prépabac 1ere NSI, éditions Hatier. Sujet adapté et remanié.

A l’entrée à l’école de Poudlard, le choixpeau magique répartit les élèves dans les différentes maisons (Gryffondor, Serpentard, Serdaigle et Poufsouffle) en fonction de leur courage, leur loyauté, leur sagesse, et leur malice.

Le choixpeau magique dispose d’un fichier CSV dans lequel sont répertoriées les données d’un échantillon d’élèves. Voici les 6 premières lignes de ce fichier :

![extrait](./data/extractCSV.png){: .center width=60%}

Et voici les élèves que le choixpeau magique souhaite orienter :

![a orienter](./data/eleves.png){: .center width=30%}

:arrow_forward: L’objectif de cet exercice est d’aider le choixpeau à déterminer la maison des nouveaux élèves.

## Partie I : Modéliser un élève

On décide de modéliser chaque élève par un dictionnaire avec les données à disposition. Par exemple : 

```python
adrian = {"nom" : "Adrian", "courage":9,"loyaute":4,"sagesse":7,"malice":10,"maison":"serpentard"}
hermione = {"nom" : "Hermione", "courage":8,"loyaute":6,"sagesse":6,"malice":6}
```

!!! example "Question 1"
    === "question"
        Donner la modélisation de l’élève Anthony

    === "Réponse"
        anthony = {"nom" : "anthony", "courage":2,"loyaute":8,"sagesse":8,"malice":3}


On décide d’utiliser la **distance de Manhattan** pour calculer la distance entre 2 élèves, c’est-à-dire : <br />
$distance(eleve1, eleve2) = |c1-c2|+|l1-l2|+|s1-s2|+|m1-m2|$

!!! example "Question 2"
    === "question"
        Avec cette formule, vérifier que la distance entre Hermione et Adrian est bien égale à 8

!!! example "Question 3"
    === "question"     
        Quelle est la distance entre Arthur et Drago ?
    === "Réponse"
        12

!!! example "Question 4"
    === "question"     
        Ecrire le code d’une fonction distance qui prend deux élèves en paramètre et qui renvoie la distance entre ces 2 élèves. Ne pas oublier de préciser la documentation (docstring) et de donner au moins un test (assert).<br />
        ^^Note :^^ la valeur absolue d’un nombre s’obtient par `abs(nombre)`
    === "Réponse"

        ```python
        adrian = {"nom" : "Adrian", "courage":9,"loyaute":4,"sagesse":7,"malice":10,"maison":"serpentard"}
        hermione = {"nom" : "Hermione", "courage":8,"loyaute":6,"sagesse":6,"malice":6}

        def distance (E1,E2) :
            """
            prend en paramètres 2 élèves
            @param : E1 : Dictionnaire
            @param : E2 : Dictionnaire
            @Returns : int : renvoie la distance de Manhattan entre les 2 eleves
            """
            return abs(E1["courage"]-E2["courage"])+abs(E1["loyaute"]-E2["loyaute"])+abs(E1["sagesse"]-E2["sagesse"])+abs(E1["malice"]-E2["malice"])

        assert (distance(adrian,hermione)) == 8
        ```

## Partie III : Charger le dataframe

Voici le code d’une fonction qui permet de récupérer les données des élèves d’un fichier CSV pour les stocker dans un dataframe pandas.

Le jeu de données : [choipeau Magique](./data/choixpeauMagique.csv){. target="_blank" .md-button }

??? note "Code charger_eleve"

    ```python
    import pandas as pd #import du module pandas, abrégé classiquement par "pd"

    def charger_eleve(fichier) : 
        """
        permet de charger une liste d eleves d'un fichier CSV
        Return  : dataframe
        """
        return pd.read_csv(fichier, encoding = 'utf-8')

    poudlard = charger_eleve('choixpeauMagique.csv')
    ```
!!! example "Question 5"
    === "question"     
        Quel est le nom du premier élève ?
    === "Réponse"

        ```python
        poudlard.loc[0]
        ```
        ```prompt
        Nom            Adrian
        Courage             9
        Loyauté             4
        Sagesse             7
        Malice             10
        Maison     Serpentard
        Name: 0, dtype: object
        ```

!!! example "Question 6"
    === "question"     
        Indiquer le nombre d’élèves par maison
    === "Réponse"

        ```python
        poudlard['Maison'].value_counts()
        ```
        ```prompt        
        Gryffondor     17
        Serpentard     12
        Serdaigle      11
        Poufsouffle    10
        Name: Maison, dtype: int64
        ```

!!! example "Question 7"
    === "question"     
        Quel est la maison ayant le plus d’élève ? 
    === "Réponse"

        ```python
        poudlard['Maison'].describe().top
        ```
        ```prompt   
        'Gryffondor'
        ```

## Partie III : Maison majoritaire

Ecrire le code d’une fonction qui prend en paramètre un dataframe Pandas et qui renvoie la maison la plus représentée dans la liste.
Ne pas oublier de préciser la documentation (docstring) et de donner au moins un test (assert).

??? tips "correction"

    ```python
    def majoritaire(data) :
        """
        Fonction renvoyant la maison majoritaire dans un DataFrame de données sur Poudlard.
        @param : Data : DataFrame contenant les données sur les maisons des élèves de Poudlard.
        @Returns: str: La maison la plus fréquente dans la colonne 'Maison' du DataFrame.
        """
        return poudlard['Maison'].describe().top
    assert majoritaire(poudlard)== 'Gryffondor'
    ```

## Partie IV : Sept plus proches voisins

Donner la fonction `choipeauMagique` qui prend en paramètre la liste des élèves déjà présent à Poudlard sous forme de dataFrame et un nouvel élève qui n'a pas encore de maison, et qui retourne la maison choisi grace à l'algorithme des plus proche voisins avec $k=3$, puis $k=7$

Note : Vous utiliserez la distance de Manhattan préparer dans les parties précédentes.

??? tips "Correction"

    ```python
    def septPlusProches(cm,nouveau):
        """
        Fonction renvoyant la maison choisi par le choipeau par l'algorithme des plus proches voisins.
        @param : cm : DataFrame contenant les données sur les maisons des élèves de Poudlard.
        @param : nouveau : dictionnaire contenant le nouvel élève à affecter à une maison
        @Returns: str : La maison choisie
        """
        #On ajoute une nouvelle colonne distance à notre jeu de données pandas
        #correspondant la la distance euclienne entre le nouveau et la ligne traitée
        cm['distance']= abs(cm['Courage']-nouveau["courage"])+abs(cm['Loyaute']-nouveau["loyaute"])+abs(cm['Sagesse']-nouveau["sagesse"])+abs(cm['Malice']-nouveau["malice"])
        # On trie le jeu de donnée sur cette nouvelle colonne
        newcm = cm.sort_values(by='distance', ascending=True)
        #On ne garde que les 7 premières lignes que l'on 'copie' dans un nouveau dataframe
        newcmtri = newcm.head(7) #on prend les 7 eleves les plus proches
        #On ne garde que le poste le plus fréquent sur ces 7 lignes
        sol = newcmtri['Maison'].describe().top
        return sol
    Harry = {"nom" : "Harry", "courage":10,"loyaute":9,"sagesse":6,"malice":3}
    assert septPlusProches(poudlard,Harry) == 'Gryffondor'
    ```

