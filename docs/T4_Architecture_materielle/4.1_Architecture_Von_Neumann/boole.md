# 4.1 Les portes logiques

![image](data/Bobinaire.png){: .center}

## 1. Notions d’algèbre de Boole

Dans les systèmes digitaux (systèmes informatiques et autres automatismes numériques) toutes les données sont traitées et enregistrées à partir d'éléments d'informations binaires.<br />
Ces informations binaires à la manière des **contacts électriques** n'ont que deux états possibles : un contact électrique est ouvert ou fermé, de même le bit est une information élémentaire qui ne peut prendre que deux valeurs 0 et 1.<br />

Les opérations logiques sont en informatique aussi courantes si ce n'est pas plus que les opérations arithmétiques. La logique combinatoire tout comme l'arithmétique repose sur quelques opérations élémentaires.<br />

•	En **arithmétique**, ces opérations sont l'addition, la soustraction, la multiplication et la division ( $+$, $-$, $*$, $/$ ). Il est possible à partir de là d'imaginer toutes les autres opérations telles que les exposants, les racines, les logarithmes etc.<br />
•	En **logique**, les opérations fondamentales sont le **ET**, le **OU** et le **NON**.<br />

Nous utiliserons des signes particuliers pour représenter ces trois opérations fondamentales lors d'écriture d'équations logiques. C'est [George Boole](https://fr.wikipedia.org/wiki/George_Boole), un mathématicien britannique, qui le premier eu l'idée de reprendre des notations algébriques pour créer les bases de ce qui sera la logique informatique. Nous ferons donc de la _logique booléenne_ et aussi de l'_algèbre booléenne_ en écrivant des équations logiques pour exprimer les relations entre les variables logiques appelées aussi variables booléennes.<br />
Cette logique a trouvé après George Boole ses premières applications dans les circuits électriques. C'est [Claude Shannon](https://fr.wikipedia.org/wiki/Claude_Shannon), un autre père fondateur des théories à la base de l'informatique, qui entreprit de mettre en équation les circuits électriques où des relais électriques considérés comme des variables logiques en agissent sur des contacts ouverts (0) ou fermé (1).<br />

La manière la plus simple de comprendre les fonctions logiques est de se les représenter par des schémas électriques qui comportent un ou plusieurs contacts et une lampe. Cette lampe s'allume "à condition" que les contacts électriques y laissent passer le courant. C'est dans l'expression de cette condition que va intervenir la logique.<br />

![lampe allumée](data/schema1.png){: width=20% .center}

Le schéma ci-dessus traduit la condition la plus simple : La lampe s'allume si le bouton poussoir A est actionné. Autrement dit ( S = 1) si ( A = 1). Le fonctionnement de ce circuit s'exprime par l'équation logique $S = A$<br />

c'est ce que l'on a mis en oeuvre dans le chapitre sur les booléens ([exercice 4](../../T2_Type_de_base/2.5_Booleens/cours.md)) en utilisant un simulateur de courant électrique. Toutes les tables de vérités ET, OU, NON, NAND peuvent être simulés à l'aide d'un circuit électriques.<br />

![circuit électrique](./data/ex_circuit.png){: width=50% .center}

## 2. Les portes logiques

### 2.1 Présentation

Nous avons jusqu'ici utilisé des boutons poussoirs et une lampe pour illustrer le fonctionnement des opérateurs logiques. En électronique digitale, les opérations logiques sont effectuées par des portes logiques. Ce sont des circuits de très petite taille implantés en très grand nombre sur des puces de silicium et qui combinent les signaux logiques présentés à leurs entrées sous forme de tensions. On aura par exemple 5V pour représenter l'état logique **1** et 0V pour représenter l'état **0**.<br />

Dans un microprocesseur moderne on compte plusieurs dizaines de milliards de portes logiques. Selon leur type, il faut de 2 à 10 transistors (composant électronique de base des portes logiques) pour réaliser chaque porte logique.<br />

Ci-dessous les schémas des portes logiques courantes avec leurs entrées (‘pattes’ situées à gauche) et leurs sorties (‘pattes’ situées à droite)
 	 	
![portes logiques](./data/portes_logiques.png){: width=80% .center}

AND, OR, NOT n’ont plus de secret pour vous ! 

### 2.2 XOR et NAND

![meme](./data/1tpvmnavbnr71.png){: width=50% .center}

**XOR** est le **OU EXCLUSIF**. Il répond comme OR sauf quand les deux entrées sont à 1 : sa sortie est alors à 0.

^^illustration :^^
![XOR](./data/xor.webp){: width=30% .center}

- Un établissement de soin accueille des personnes âgées **OU** malades : c’est le **OR**
- Un restaurateur vous propose fromage **OU** dessert : c’est le **XOR**

**NAND** (pour Not AND) et **NOR** (pour Not OR) sont les **AND** et **OR** suivies de **NON**.
Elles répondent exactement le contraire de AND et OR.

!!! question "Exercice"
    === "Enoncé"
        Rendez-vous à la page [simulateur](https://lecture.ecc.u-tokyo.ac.jp/johzu/joho/Data/NewLogicSimulator/sample.html) ou [simulateur](https://kazuhikoarase.github.io/simcirjs/). Ce simulateur vous propose toutes ces portes logiques. 
        
        :arrow_forward: Câblez et vérifiez les tables de vérité des fonctions AND et OR Etablir les tables de vérité des fonctions XOR, NAND, NOR 

        ^^Remarque :^^ Evitez les boutons _PuschOn_ au profit des _Toggle_ (bouton à bascule) qui ont l’avantage de rester dans l’état ou vous les basculez. Ici le bouclage des cablages n’est pas représenté c’est pourquoi une alimentation (_DC_) ou une LED ne comporte qu’un seul pôle

        Préparez une trace écrite contenant les copies partielles d’écran de vos montages et les tables de vérité associées.

    === "Correction"
        ![images](./data/portes1.png){: width=50% .center}
        ![images](./data/portes2.png){: width=50% .center}

Mais quel rapport avec les ordinateurs ?<br />
Nous allons répondre à cette question en nous limitant à l’opération la plus simple que nous demandons à un ordinateur : réaliser la somme de deux entiers.<br />
C’est la plus simple mais d’elle découlent :

- les différences (même processus avec un entier signé négatif)
- certaines multiplications (sommes répétitives)

Poser verticalement et calculer en binaire la somme des deux entiers $A = {14}_{10}$    et   $B = {9}_{10}$       

??? note "somme en binaire"
    ![somme](./data/additionbinaire.png){: width=50% .center}


Qu’avez-vous fait ?<br />
Commençons par la colonne de droite (bit de $2^0$ de poids faible) : vous avez réalisé une opération logique :

- si les deux étaient à 0 vous avez écrit en dessous **0** pour la somme.
- si un des deux étaient à 0 et l’autre à 1 vous avez écrit en dessous **1** pour la somme.
- si les deux étaient à 1 vous avez écrit en dessous **0** pour la somme. et vous avez pensé à mettre la retenue à **1**.

:arrow_forward: Ecrire ci-dessous les tables de vérité des deux opérations logiques qui donnent (pour le bit de poids faible)

- la somme à partir des deux opérandes
- la retenue (0 si elle n’existe pas, 1 si elle existe)

:arrow_forward: Recherchez plus haut quelles portes logiques étudiées effectuent exactement ces même tâches.

??? question "solution"
    On obtient pour la somme la table de vérité du OU<br />
    et pour la retenue la table de vérité du ET

## 3. Les additionneurs

:arrow_forward: Recherchez sur internet une image correspondant au mot clé ‘**half adder**’ ou ‘**demi additionneur**’ le schéma doit confirmer votre réponse précédente. 

Quel mot anglais se cache dans ces schémas derrière la lettre **C** (ou Cout) ? Pourquoi parle-t-on d’une fonction logique à 2 entrées et 2 sorties ?

??? question "solution"
    ![hald adder](./data/halfadder.png){: width=50% .center}

    Le half adder ajoute deux bits ensemble. Le demi additionneur a deux signaux d'entrée représentant des chiffres binaires (a et b) et deux signaux de sortie, dont l'un est le résultat de l'addition (s), et l'autre le carry en classe supérieure (C). Il est important de noter qu'un demi additionneur ne peut pas être utilisé pour ajouter des nombres binaires à plusieurs chiffres parce qu'il n'y a pas de port de niveau inférieur. Le demi additionneur est un circuit combiné de circuits XOR et AND. Son but, comme son nom l'indique, est d'ajouter des chiffres. Le processus d'addition de nombres dans le système binaire est réduit à l'addition de chiffres, où l'on obtient ainsi une somme et un carry. Puisque le demi additionneur lui-même ne peut pas calculer le résultat entier, il est combiné avec un autre demi additionneur et un circuit OU pour faire un additionneur complet.

    [](http://www.differencebetween.net/technology/difference-between-half-adder-and-full-adder/)

A partir de la deuxième colonne (bits de $2^1$ puis suivants), la prise en compte des deux bits en provenance de A et B ne suffit plus. Il faut aussi considérer **la retenue**.<br />
La fonction logique ‘half adder’ ne suffit plus, on a besoin de la fonction ‘full adder’. 

:arrow_forward: Cherchez sur internet un schéma en portes logiques de ‘full adder’ (ou ‘plein additionneur’). Il était un peu compliqué à deviner !

??? question "solution"
    ![full adder](./data/fulladder.png){: width=50% .center}

A l’aide du simulateur, câblez un **full adder**.<br />
Vérifier qu’il fonctionne correctement et établir sa table de vérité.<br />

^^Préliminaire :^^ Construction d’entrées sélectionnables (0/1) par bouton (Toggle) puis regroupement sur un petit espace

![tips](./data/tips.png)
 
Ce petit ‘pavé’ constitue une entrée avec sa diode témoin, celle-ci n’est pas indispensable mais aide à la visualisation de l’état de l’entrée (0 ou 1). Ce pavé est à raccorder aux portes logiques à partir de la borne de sortie du **Toggle**. Vous répéterez cette petite construction pour constituer autant d’entrées que nécessaires.

Pour visualiser les sorties, il suffira bien évidemment de raccorder une DEL.

A partir du schéma que vous avez trouvé, réalisez sur le simulateur le montage de l’additionneur plein avec ses entrées, la combinaison des portes logiques, les sorties.

??? question "solution"
    ![full adder simulé](./data/fulladder_js.png){: width=50% .center}

Puis etablissez la table de vérité complète que vous avez établie à l’aide de votre montage (5 colonnes, 8 lignes)

??? question "solution"
    ![full adder table](./data/fulladder_table.png){: width=50% .center}

Le simulateur propose la fonction Full adder toute faite. Sur votre schéma précédent conservez les entrées et les sorties et retirez toutes les portes logiques. Remplacez cet ensemble de porte logique par un ‘full adder’, recâblez, vérifiez votre table de vérité.

??? question "solution"
    ![full adder simulé](./data/fulladder_js2.png){: width=50% .center}

!!! question "Réalisation d’un additionneur 4 bit"
    === "Enoncé"
        Sur l’image ci-dessous, on a représenté une addition posée verticalement. Recopiez ce schéma sur le simulateur et câblez dans l’espace libre les ‘full adder’ nécessaires pour les additions se fassent correctement quels que soient les entrées choisies

        ![image](./data/addition4bits.png){: width=50% .center}

    === "Correction"
        ![image](./data/addition4bits_simule.png){: width=50% .center}
 
