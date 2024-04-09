# Algorithmes gloutons
en anglais : _greedy algorithms_

##  Le problème du rendu de monnaie

###  La méthode gloutonne

![image](data/monnaie.jpg){: .center width=50%}

Nous allons travailler avec des pièces (ou billets) de 1, 2, 5, 10, 20, 50, 100, 200 euros.

L'objectif est de créer un programme renvoyant, pour une somme ```somme_a_rendre``` entrée en paramètre, la combinaison utilisant un **minimum** de pièces ou de billets pour fabriquer la somme ```somme_a_rendre```. 

Par exemple, lorsque vous payez avec 20 € un objet coûtant 11 €, vous préférez qu'on vous rende vos 9 € de monnaie par $$ 9 = 5 + 2+2$$ plutôt que par $$ 9=2+2+2+1+1+1$$

La résolution de ce problème peut se faire de manière gloutonne : à chaque étape, vous allez essayer de rendre la plus grosse pièce (ou billet) possible.

??? tips "Solution du problème"

    ```python 
    def rendu(somme_a_rendre,pieces):
        """
        Rend la somme donnée en utilisant le moins de pièces possible.
        @param : somme_a_rendre (int): La somme à rendre en utilisant les pièces disponibles.
        @param : pieces (list of int): La liste des valeurs des pièces disponibles, triée par ordre décroissant.

        @return : list of int: Liste des valeurs des pièces utilisées pour rendre la somme.

        Exemple:
            >>> rendu(15, [10, 5, 2, 1])
            [10, 5]
            >>> rendu(28, [25, 10, 5, 1])
            [25, 1, 1, 1]
        """
        i =  len(pieces) - 1   # on part de l'indice de la dernière pièce, la plus grande
        solution = []
        while somme_a_rendre > 0:
            if pieces[i] <= somme_a_rendre : # est-ce que la pièce peut-être rendue ?
                solution.append(pieces[i])   # on garde la pièce dans la liste solution
                somme_a_rendre = somme_a_rendre - pieces[i] # on met à jour la somme à rendre
            else :
                i -= 1   # la pièce était trop grosse, on recule dans la liste
        return solution

    P  = [1,2,5,10,20,50,100,200]
    assert rendu(13, P) == [10,2,1]
    assert rendu(58,P) == [50, 5, 2, 1]
    ```

###  Une solution optimale ?

Imaginons qu'il n'y ait plus de pièces de 10 et 5 euros. 
Faites fonctionner votre algorithme pour la somme de 63 euros.

```python 
P  = [1,2,20,50,100,200]

assert rendu(63,P) == [50, 2, 2, 2, 2, 2, 2, 1]
```

Mais ce n'est pas une solution optimale !  `[20, 20, 20, 2, 1]` serait bien mieux.

**Moralité** : Lors d'un rendu de monnaie, l'algorithme glouton n'est optimal que _sous certaines conditions_, ce qui est un peu décevant. Un système de monnaie qui rend l'algorithme glouton est dit **canonique**. Il est difficile de caractériser mathématiquement si un système de monnaie est canonique ou pas.

!!! info "Entrainement"

    [Nombre minimal de quais](https://codex.forge.apps.education.fr/exercices/nombre_quais/) Difficulté : :star::star: <br />
    [Livraisons à Manhattan](https://codex.forge.apps.education.fr/en_travaux/manhattan/) Difficulté : :star::star: