# Les algos Gloutons

![image](data/BO.png){: .center}

![](data/greedy.png){: .center}

## 1. La NASA

Vous faites partie de l'équipage d'un vaisseau spatial qui doit rejoindre une base installée sur la face visible de la Lune. Mais, suite à un certain nombre de problèmes, vous êtes contraints de vous poser en catastrophe, à 320 km du point prévu.

![](data/moon.jpg){: .center width=50%}

Au cours de cet alunissage d'urgence, la plupart des équipements de bord de votre vaisseau sont endommagés, à l'exclusion de vos scaphandres de sortie dans l'espace et de quinze objets cités ci-dessous.

Il s'agit donc pour votre équipage de rejoindre la base lunaire au plus vite en emportant le strict minimum avec vous. Vous ne pouvez emmener que 10 objets parmi les 15 cités ci -dessous.

- Une boîte d’allumettes
- Des aliments concentrés
- 50 mètres de corde en nylon
- Un parachute en soie
- Un appareil de chauffage fonctionnant sur l’énergie solaire
- Deux pistolets calibre 45
- Une caisse de lait en poudre
- Deux réservoirs de 50 kg d’oxygène chacun
- Une carte céleste des constellations lunaires
- Un canot de sauvetage autogonflable
- Un compas magnétique
- 25 litres d’eau
- Une trousse médicale et des seringues hypodermiques
- Des signaux lumineux
- Un émetteur-récepteur fonctionnant sur l’énergie solaire

Pour résoudre le dilemne posé, une solution serait d'attribuer une "valeur" numérique à chaque objet. La valeur la plus forte est donnée pour l'objet de plus grande importance, et la valeur la plus faible à l'objet de moindre importance.

> Classez les objets ci dessous pour ordre de valeur, le 15ème ayant le plus d'importance vitale (selon vous !)

|Nom de l'objet|Valeur|
|:--:|:--:|
| Une boîte d’allumettes||
| Des aliments concentrés||
| 50 mètres de corde en nylon||
| Un parachute en soie||
| Un appareil de chauffage fonctionnant sur l’énergie solaire||
| Deux pistolets calibre 45||
| Une caisse de lait en poudre||
| Deux réservoirs de 50 kg d’oxygène chacun||
| Une carte céleste des constellations lunaires||
| Un canot de sauvetage autogonflable||
| Un compas magnétique||
| 25 litres d’eau||
| Une trousse médicale et des seringues hypodermiques||
| Des signaux lumineux||
| Un émetteur-récepteur fonctionnant sur l’énergie solaire||

??? tips "Correction"

    |Nom de l'objet|Valeur|Explications|
    |:--:|:--:|:--:|
    | Une boîte d’allumettes|1|Absence d’oxygène sur la lune : on ne peut pas les enflammer. |
    | Des aliments concentrés|12|Moyen efficace pour se nourrir |
    | 50 mètres de corde en nylon|10|Utile pour se mettre en cordée, escalader les roches, éventuellement hisser les blessés |
    | Un parachute en soie|8|Peut servir à se protéger des rayons solaires|
    | Un appareil de chauffage fonctionnant sur l’énergie solaire|3|Sans utilité : les combinaisons sont chauffantes|
    | Deux pistolets calibre 45|5|Peuvent servir à accélérer la propulsion ; à la rigueur à mettre fin à ses jours|
    | Une caisse de lait en poudre|4|Plus encombrant que les aliments concentrés|
    | Deux réservoirs de 50 kg d’oxygène chacun|15|Premier élément de survie : essentiel|
    | Une carte céleste des constellations lunaires|13|Indispensable pour s’orienter|
    | Un canot de sauvetage autogonflable|7|Peut servir de traîneau pour tracter des objets ; le gaz (CO) employé pour cet engin peut servir à la propulsion|
    | Un compas magnétique|2|Sans utilité sur la lune, le champ magnétique n’y étant pas valorisé |
    | 25 litres d’eau|14|Indispensable pour compenser une forte déshydratation due à la très grande chaleur sur la face éclairée de la lune|
    | Une trousse médicale et des seringues hypodermiques|9|Les piqûres de vitamines, sérum, etc. nécessitent une ouverture spéciale (prévue par la NASA) dans la combinaison|
    | Des signaux lumineux|6|Utiles quand la fusée-mère sera en vue|
    | Un émetteur-récepteur fonctionnant sur l’énergie solaire|11|Utile pour essayer de communiquer avec la fusée-mère mais cet appareil n’a pas une grande portée|

!!! example "structure"
    === "Enoncé"
        **Quelle(s) structure(s) algorithmique(s), vous paraissent pertinentes pour enregistrer vos valeurs ?** <br />
        ▶️Codez une solution <br />

    === "Correction"
        ```python
        nasa=[('allumettes', 1), ('aliments', 12), ('corde', 10), ('parachute', 8), ('chauffage', 3), ('pistolets', 5), ('lait', 4), ('oxygène', 15), ('carte', 13), ('canot', 7), ('compas', 2), ('eau', 14), ('seringues', 9), ('signaux', 6), ('emetteur', 11)]
        ```
        et pour trier ce dictionnaire, nous allons utiliser la fonction sorted :
        ```python
        nasa_trie = sorted(liste, key=lambda x: x[1], reverse=True)
        ```
        La ligne fait trois choses en une :

        1. récupére l'objet à trier, ici ``liste``
        2. key=lambda x: x[1] cible la valeur (index=1) comme critère de comparaison,
        3. reverse=True trie du plus grand au plus petit.

Revenons à notre résolution de problème, c'est à dire trouver les "meilleurs" objets pour la survie.

⁉️ La solution optimum est de prendre les :keycap_ten: valeurs les plus fortes. Et à présent que la liste est triée par ordre décroissante, cela devrait être plus facile ! Il suffit de prendre les 10 premièrs objets.

!!! example "tri"
    === "Enoncé"
        Codez l'affichage des 10 objets les plus importants

    === "Correction"

        ```python linenums='1'
        liste_sel = []
        for i in range(10):
            liste_sel.append(liste_triee[i][0])
        print(liste_sel)
        ```

Et si l'on rajoute une **contrainte de poids** ? Les astronautes ne peuvent emporter que **200 kg** de matériel.

|Nom de l'objet|Valeur|Poids en kg|
|:--:|:--:|:--:|
| Une boîte d’allumettes|1|0.1|
| Des aliments concentrés|12|2|
| 50 mètres de corde en nylon|10|5|
| Un parachute en soie|8|0.5|
| Un appareil de chauffage fonctionnant sur l’énergie solaire|3|25|
| Deux pistolets calibre 45|5|0.5|
| Une caisse de lait en poudre|4|5|
| Deux réservoirs de 50 kg d’oxygène chacun|15|100|
| Une carte céleste des constellations lunaires|13|0.1|
| Un canot de sauvetage autogonflable|7|100|
| Un compas magnétique|2|0.5|
| 25 litres d’eau|14|25|
| Une trousse médicale et des seringues hypodermiques|9|0.5|
| Des signaux lumineux|6|1|
| Un émetteur-récepteur fonctionnant sur l’énergie solaire|11|5|

❓ En partant la structure suivante `nasa=[('allumettes', 1), ('aliments', 12), ('corde', 10))`, comment ajouter la notion de poids ?

??? tips "Correction"

    ```python
    liste = [
        ('allumettes', 1,  0.1),
        ('aliments',   12, 2),
        ('corde',      10, 5),
        ('parachute',  8,  0.5),
        ('chauffage',  3,  25),
        ('pistolets',  5,  0.5),
        ('lait',       4,  5),
        ('oxygène',    15, 100),
        ('carte',      13, 0.1),
        ('canot',      7,  100),
        ('compas',     2,  0.5),
        ('eau',        14, 25),
        ('seringues',  9,  0.5),
        ('signaux',    6,  1),
        ('emetteur',   11, 5)
    ]
    ```

**Quelle serait alors la combinaison optimum pour maximiser ses chances de survie ?**

Plus difficile, non ? :skull:

## 2. le sac à dos

![](data/sac_a_dos.png){: .center width=50%}

Le problème du sac à dos est un problème classique d'**optimisation** : on dispose d'un ensemble d'objets, chacun ayant une valeur et un poids, et d'un sac pouvant supporter un poids maximum. L'objectif est de choisir quels objets emporter pour maximiser la valeur totale sans dépasser la limite de poids.

Lien vers l'article de [Wikipedia](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos) :

En algorithmique, le problème du sac à dos, noté également KP (en anglais, Knapsack problem) est un **problème d'optimisation combinatoire**. ...<br />
Ou plus simplement, les objets mis dans le sac à dos doivent maximiser la valeur totale, sans dépasser le poids maximum.

C'est un problème du quotidien déguisé en maths : un cambrioleur qui choisit quoi voler, un randonneur qui prépare son sac, un directeur sportif qui recrute avec un budget limité...

## 2.1 Formulation mathématique du problème du sac à dos 

Toute formulation commence par un énoncé des données. Dans notre cas, nous avons un sac à dos de poids maximal $W$ et $n$ objets. Pour chaque objet $i$, nous avons un poids $w_{i}$ et une valeur $p_{i}$.

Pour quatre objets ($n=4$) et un sac à dos d'un poids maximal de 30 kg ($W=30$), nous avons par exemple les données suivantes :</p>

|Objet|1|2|3|4|
|:--:|:--:|:--:|:--:|:--:|
|$p_{i}$|7|4|3|3|
|$w_{i}$|13|12|8|10|

Ensuite, il nous faut définir les variables qui représentent en quelque sorte les actions ou les décisions qui amèneront à trouver une solution. On définit la variable $x_{i}$ associée à un objet $i$ de la façon suivante : $x_{i}=1$ si l’objet $i$ est mis dans le sac, et $x_{i}=0$ si l’objet $i$ n’est pas mis dans le sac.

Dans notre exemple, une solution réalisable est de mettre tous les objets dans le sac à dos sauf le premier, nous avons donc : 
$x_{1}=0$, $x_{2}=1$, $x_{3}=1$, et $x_{4}=1$.</p>

Puis il faut définir les contraintes du problème. Ici, il n'y en a qu’une : la somme des poids de tous les objets dans le sac doit être inférieure ou égale au poids maximal du sac à dos.

Cela s’écrit : $x_{1}*w_{1}+x_{2}*w_{2}+x_{3}*w_{3}+x_{4}*w_{4} <= W$

ou plus généralement pour $n$ objets : $\sum_{i=1}^{n} x_{i}*w_{i} \le W$<br />
    
Pour vérifier que la contrainte est respectée dans notre exemple, il suffit de calculer cette somme : $0 × 13 + 1 × 12 + 1 × 8 + 1 × 10 = 30$, ce qui est bien inférieur ou égal à 30, donc la contrainte est respectée. Nous parlons alors de solution réalisable. <br />
:bangbang: Mais ce n’est pas nécessairement la meilleure solution.<br />
Enfin, il faut exprimer la fonction qui traduit notre objectif : **maximiser la valeur totale des objets dans le sac**.<br />
Pour $n$ objets, cela s’écrit : $Max \sum_{i=1}^{n} x_{i}*w_{i}$ <br />
    
Dans notre exemple, la valeur totale contenue dans le sac est égale à $10$. Cette solution n’est pas la meilleure, car il existe une autre solution de valeur plus grande que $10$ : il faut prendre seulement les objets $1$ et $2$ qui donneront une valeur totale de $11$ pour un poids de $25$. Il n’existe pas de meilleure solution que cette dernière, nous dirons alors que cette solution est **optimale**.

## 2.2 Résolution par Force brute

Dans un problème d'optimisation chaque solution possède une valeur, et on cherche à déterminer parmi toutes les solutions celle dont la valeur est optimale.

La technique la plus basique pour résoudre ce type de problème consiste à énumérer de façon exhaustive toutes les solutions possibles, puis à choisir la meilleure. Cette approche est nommée par **force brute**.

Le principe de la résolution par force brut est de générer toutes les combinaisons possibles. Puis de sélectionner uniquement celle qui maximise la valeur, tout en respectant les contraintes données.

Pour résoudre cette problématique par force brute, la bibliothèque [itertools](https://docs.python.org/fr/3/library/itertools.html) pour générer toutes les combinaisons possibles.

```prompt
allumettes
allumettes\aliments
allumettes\corde
...
allumettes\aliments\corde
allumettes\aliments\parachute
...
```

!!! question "Question"
    Combien y a t'il de combinaisons possible ?

??? tips "Réponse"
    Au rang $1$ : on a $1$ éléments dans la liste, il y a $15$ combinaisons possibles.<br />
    Au rang $2$ : on a $2$ éléments dans la liste, il y a $105$ combinaisons possibles.(On ne compte pas les permutations : carte/eau est la même combinaison que eau/carte)

    Au rang $p$ : cela fait appel à des notions mathématiques, non vu par vous en première.
    La formule est $\mathrm{C}_{n}^{p} = \frac{n!}{(n-p)!*p!}$ <br />

    où $p$ est le nombre d'objet dans la combinaison et $n$ le nombre total d'objet.<br />
    Avec cette formule, on obtient bien 105.<br />

    Ici, on cherche la somme de toutes ces combinaisons, et la formule est ici $2^{n}$.Donc $2^{15} = 32 768$

!!! question "Question"
    Que pouvez vous en déduire sur la complexité de l'algorithme par force brut ?

??? tips "Réponse"
    La complexite de l'algorithme brut du problème du sac à dos est de l'ordre de $2^{n}$

    | Temps |Type de complexité|Temps pour $n = 5$|Temps pour $n = 10$|	Temps pour $n = 20$|Temps pour $n = 50$|	Temps pour $n = 250$|Temps pour $n = 1 000$|Temps pour $n = 10 000$	|Temps pour $n = 1 000 000$|Problème exemple|
    ||||||||||||
    |$\displaystyle O\left(2^{\rm {{poly}(n)}}\right)$ |complexité exponentielle |	320 ns |10 µs |	10 ms |130 jours |$\displaystyle 10^{59}$ ans|... |...	|... |problème du sac à dos par force brute |

    [Source wikipedia](https://fr.wikipedia.org/wiki/Analyse_de_la_complexit%C3%A9_des_algorithmes)

Vous trouverez ci dessous le code de résolution du problème de la NASA par force brut.

??? note "Code par force brute"

    ```python linenums='1'
    ################################
    #       --- Force brute ---    #        
    ################################
    print("--- Solution force brute ---")
    # chaque tuple : (nom, valeur, poids)
    #                 x[0]  x[1]   x[2]

    # --- Contraintes ---
    POIDS_MAX  = 200
    MAX_OBJETS = 10

    # --- Initialisation ---
    meilleur_valeur = 0
    meilleur_comb   = []
    meilleur_poids  = 0

    # --- Force brute ---
    for r in range(1, MAX_OBJETS + 1):
        for combinaison in itertools.combinations(liste, r):
            print(f"Combinaison testée : {[objet[0] for objet in combinaison]}")
            valeur_totale = sum(objet[1] for objet in combinaison)
            poids_total   = sum(objet[2] for objet in combinaison)

            if poids_total <= POIDS_MAX and valeur_totale > meilleur_valeur:
                meilleur_valeur = valeur_totale
                meilleur_poids  = poids_total
                meilleur_comb   = [objet[0] for objet in combinaison]

    # --- Résultat ---
    print(f"Meilleure combinaison : {meilleur_comb}")
    print(f"Valeur totale         : {meilleur_valeur}")
    print(f"Poids total           : {meilleur_poids} kg")
    ```

## 3. Algorithmie "Glouton"

!!! abstract "Définition :heart:"
    Un algorithme est qualifié de **glouton** si le problème qu'il essaie de résoudre est décomposé en une succession de problèmes identiques pour lesquels l'algorithme va chercher une solution optimale.  

La question (presque philosophique) est :

*Lorsqu'on fait à chaque étape le meilleur choix possible, est-ce que la solution finale à laquelle on arrive est la meilleure possible ?*

Formulé autrement :

*Est-ce que faire le meilleur choix à chaque étape nous assure le meilleur choix global ?*

Il existe dans la littérature informatique deux problèmes classiques, dont les informaticiens ont essayé de généraliser la résolution : le problème du sac à dos et celui du rendu de monnaie

??? info "Le rendu de monnaie"

    ![](data/monnaie.jpg){: .center width=50%}

    Le problème du rendu de monnaie s’énonce de façon simple : étant donné un ensemble de pièces à disposition (je ne peux rendre que des pièces de 50 centimes, 1 euro, 2 euros…) et un montant à rendre, rendre ce montant avec un <u>nombre minimal de pièces</u> du système que l’on s’est donné. Les applications d’une solution à ce problème sont faciles à imaginer : nul n’a envie de récupérer 1 euro en pièces de 1 centime s’il s’est aventuré à payer 2 euros pour une malheureuse bouteille de soda à un distributeur !!

    Lien vers l'article de [Wikipedia](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_rendu_de_monnaie) 

### 3.1 principes et définitions

Les algorithmes gloutons sont des algorithmes assez simples dans leur logique. Ainsi que leur nom le suggère, ils sont conçus pour prendre le **maximum** de ce qui est **disponible à un moment donné**.

L’algorithme glouton choisit la **solution optimale** qui se présente à lui à chaque instant, sans se préoccuper, ni du passé ni de l’avenir. Il répète cette même stratégie à chaque étape jusqu’à avoir entièrement résolu le problème.

!!! note "Définition"
    Un algorithme glouton est un algorithme qui effectue à chaque instant, le meilleur choix possible sur le moment, sans retour en arrière ni anticipation des étapes suivantes, dans l’objectif d’atteindre au final un résultat optimal.

Les algorithmes gloutons sont parfois appelés algorithmes gourmands ou encore algorithmes voraces.<br />
La **répétition** de cette stratégie très simple, permet de résoudre rapidement et de manière souvent satisfaisante des problèmes d’optimisation sans avoir à tester systématiquement toutes les possibilités.

!!! info "**NP-complet**"
    Le problème du sac à dos est **NP-complet**.

    **P** regroupe les problèmes résolubles rapidement (en temps polynomial). **NP** regroupe les problèmes dont on peut vérifier une solution rapidement, mais pas nécessairement en trouver une rapidement.

### 3.2 Application

!!! warning "Algorithme"
    
    ```text
    calculer la valeur (pi / wi) pour chaque objet i,
    trier tous les objets par ordre décroissant de cette valeur,
    Boucle sur les objets dans l'ordre : 
        ajouter l’objet sélectionné dans le sac si le poids maximal reste respecté.
    ```

??? info "Code par la méthode gloutonne."

    ```python linenums='1'  
    ################################
    #       --- Glouton ---        #        
    ################################
    print("\n--- Solution gloutonne ---")
    # --- Contraintes ---
    POIDS_MAX  = 200
    MAX_OBJETS = 10

    # --- Étape 1 : tri par valeur décroissant ---
    #liste_triee = sorted(liste, key=lambda x: x[1], reverse=True)

    # --- Étape 2 : sélection gloutonne ---
    meilleur_valeur = 0
    meilleur_poids  = 0
    meilleur_comb   = []

    for objet in liste_triee:
        if meilleur_poids + objet[2] <= POIDS_MAX and len(meilleur_comb) < MAX_OBJETS:
            meilleur_valeur += objet[1]
            meilleur_poids  += objet[2]
            meilleur_comb.append(objet[0])

    # --- Résultat ---
    print(f"Meilleure combinaison : {meilleur_comb}")
    print(f"Valeur totale         : {meilleur_valeur}")
    print(f"Poids total           : {meilleur_poids} kg")
    ```

!!! question "Question"
    === "Enoncé"
        L'exécution du programme est il plus rapide ?
    === "Correction"
        La méthode par glouton est beaucoup plus rapide.

*remarque :* Ici, on obtient le même résultat par force brute et par méthode gloutonne. Nous allons voir dans le TP mercato que ce n'est pas toujours le cas. Le problème fondamental est que le glouton ne revient jamais en arrière : un mauvais choix au début (prendre un objet un peu trop lourd) bloque des combinaisons potentiellement meilleures pour la suite.

## 4. Complexité
**Algorithme force brute** : la génération de toutes les combinaisons possibles de $n$ objets produit $2^n$ combinaisons à évaluer. La complexité est donc **exponentielle** : $O(2^n)$. Elle devient rapidement ingérable quand $n$ grandit.

**Algorithme glouton** : deux opérations dominent le coût :

- le **tri** préalable par ratio valeur/poids : $O(n \log n)$
- le **parcours** de la liste triée : $O(n)$

La complexité totale est $O(n \log n + n)$, ce qui se simplifie en $O(n \log n)$ car le terme $n$ devient négligeable devant $n \log n$ quand $n$ est grand.

La différence est considérable en pratique :

| $n$ | $O(n \log n)$ | $O(2^n)$ |
|:--:|:--:|:--:|
| 10 | 33 opérations | 1 024 |
| 50 | 282 opérations | $10^{15}$ |
| 100 | 664 opérations | $10^{30}$ |

Le glouton reste **quasi-instantané** là où la force brute devient impossible à exécuter.

![Classe de complexite](./data/classes-de-complexité.png){: .center width=60%}

<p style="padding:5px;color:red;text-align:center;font-weight: bold;font-size:20px;">!!! Un algorithme glouton ne fournit pas toujours le meilleur résultat possible !!!</p>

### Cas d'usage des algorithmes gloutons

Les algorithmes gloutons sont souvent employés pour résoudre des **problèmes d’optimisation**. <br />

- déterminer le plus court chemin dans un réseau<br />
- optimiser la mise en cache de données<br />
- compresser des données<br />
- organiser au mieux le parcours d’un voyageur visitant un ensemble de villes<br />
- organiser au mieux des plannings d’activité ou d’occupations de salles.<br />

!!! example "Source" 
    - [pixees](https://pixees.fr/informatiquelycee/n_site/nsi_prem_glouton_algo.html)
    - [wikipedia](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos)
    - [Fiche cours schoolmouv](https://www.schoolmouv.fr/cours/algorithmes-gloutons/fiche-de-cours)
    - [Fiche interstice sur le sac à dos](https://interstices.info/le-probleme-du-sac-a-dos/)
    - PrépaBac hatier : Algorithme glouton sur le rendu de monnaie
    - "Programmation efficace" aux éditions Ellipses
    - [Lumni : survivre sur la lune](https://www.lumni.fr/article/jouer-a-survivre-sur-la-lune)
    - [site du zéro : fiche sac à dos](http://sdz.tdct.org/sdz/les-algorithmes-gloutons.html)
    - [Gilles Glassus - académie de Bordeaux](https://glassus.github.io/premiere_nsi/T4_Algorithmique/4.6_Algorithmes_gloutons/cours/)