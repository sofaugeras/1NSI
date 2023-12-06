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

!!! example "exercice"
    === "Énoncé"
        ![image](data/sanglier.jpg){: .center width=60%}
        Résolvez le **Pydéfi** proposé à [cette adresse](https://pydefis.callicode.fr/defis/Herculito04Sanglier/txt)

        Vous pouvez vous créer un compte pour valider vos résultats, ce site (géré par l'Académie de Poitiers) est **remarquable**. 
    
    === "Correction"
        (avec les valeurs de test)
        ```python linenums='1'
        lst = [0, 50, 40, 100, 70, 90, 0]

        total = 0
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                nb_pierres = (lst[i]-lst[i+1])//10 + 1
                total += nb_pierres

        print(total)
        ```