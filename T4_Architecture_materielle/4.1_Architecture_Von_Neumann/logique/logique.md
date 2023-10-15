# 3.0 Les portes logiques

![image](data/BO.png){: .center}

Dans les systèmes digitaux (systèmes informatiques et autres automatismes numériques) toutes les données sont traitées et enregistrées à partir d'éléments d'informations binaires.
Ces informations binaires à la manière des contacts électriques n'ont que deux états possibles : un contact électrique est ouvert ou fermé, de même le bit est une information élémentaire qui ne peut prendre que deux valeurs 0 et 1.
Les opérations logiques sont en informatique aussi courantes si pas plus que les opérations arithmétiques. La logique combinatoire tout comme l'arithmétique repose sur quelques opérations élémentaires.
•	En arithmétique, ces opérations sont l'addition, la soustraction, la multiplication et la division ( +, -, *, / ). Il est possible à partir de là d'imaginer toutes les autres opérations telles que les exposants, les racines, les logarithmes etc.
•	En logique, les opérations fondamentales sont le ET, le OU et le NON.
Nous utiliserons des signes particuliers pour représenter ces trois opérations fondamentales lors d'écriture d'équations logiques. C'est George Boole, un mathématicien britannique, qui le premier eu l'idée de reprendre des notations algébriques pour créer les bases de ce qui sera la logique informatique. Nous ferons donc de la logique booléenne et aussi de l'algèbre booléenne en écrivant des équations logiques pour exprimer les relations entre les variables logiques appelées aussi variables booléennes.
Cette logique a trouvé après George Boole ses premières applications dans les circuits électriques. C'est Claude Shannon, un autre père fondateur des théories à la base de l'informatique, qui entreprit de mettre en équation les circuits électriques où des relais électriques considérés comme des variables logiques en agissent sur des contacts ouverts (0) ou fermé (1).

La manière la plus simple de comprendre les fonctions logiques est de se les représenter par des schémas électriques qui comportent un ou plusieurs contacts et une lampe. Cette lampe s'allume "à condition" que les contacts électriques y laissent passer le courant. C'est dans l'expression de cette condition que va intervenir la logique.

![lampe allumée](data/schema1.png){: .center}

Le schéma ci-dessus traduit la condition la plus simple : La lampe s'allume si le bouton poussoir A est actionné. Autrement dit ( S = 1) si ( A = 1)
Le fonctionnement de ce circuit s'exprime par l'équation logique S = A


