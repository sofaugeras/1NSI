!!! example "Manipulation de tuple"
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
        a vaut Mme <br />
        b vaut M. <br />
        c vaut 19

!!! abstract "Exercice"
    === "Énoncé"
        On considère deux points A et B d'un repère quelconque. Leurs coordonnées sont des tuples à deux éléments.
        Écrire une fonction qui prend en argument les coordonnées de deux points et qui renvoie le milieu de ces deux points.

        La fonction doit fonctionner de cette manière :
        ```python
        >>> C = (45, 12)
        >>> D = (49, 32)
        >>> milieu(C,D)
        (47, 22)
        ```

    === "Correction"
        ```python
        def milieu(point1, point2):
            abscisse = (point1[0]+point2[0]) / 2
            ordonnee = (point1[1]+point2[1]) / 2
            return (abscisse, ordonnee)
        ```
