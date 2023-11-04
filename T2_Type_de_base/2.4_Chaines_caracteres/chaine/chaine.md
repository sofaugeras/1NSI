# Les chaines de caracteres

!!! note "crédit"
    crédit du notebook : [Olivier Lecluse](https://notebooks.lecluse.fr/)

## Qu'est-ce qu'une chaîne.

!!! note "A retenir"
    Une chaîne de caractères est une liste particulière ne contenant que des caractères. Elle est délimitée par des guillemets (simples 'machaine' ou doubles "machaine").

Comme pour une liste, on peut accéder à ses éléments (les caractères) en spécifiant un indice :

```python
chaine = "Lycée Saint Sauveur"
chaine[0]
```

!!! warning "Important"
    Par contre, il est **impossible** de modifier une chaîne de caractères ! <br />
    On dit alors qu'il s'agit d'une liste **non mutable** :

```python
chaine[1]= "a"
```

Si vous décidiez de lui ajouter des caractères en fin de chaîne à l'aide d'une concaténation du type suivant :

```python
chaine = chaine+" - Redon"
chaine
```

***Remarque*** : Contrairement aux apparences, la chaine n'a pas été modifiée *puisque les chaines sont non mutables*, une nouvelle chaine a été crée par *concaténation* des deux chaines placées autour du signe ***+***

Il existe de nombreuses méthodes agissant sur les chaînes de caratères. Pour les voir, vous pouvez utiliser la fonction d'*autocompletion* de VSCode en tapant <code>chaine. </code> puis en pressant la touche *TAB*. N'oubliez pas le ***.*** !

Vous devriez voir la liste des méthodes disponibles dans le terminal:

 . | .  | .  | .
:-----------: | :----------:    |  :-----------: |  :-----------: 
x.capitalize | x.isalnum      |    x.join      |    x.rsplit 
x.casefold   |   x.isalpha     |  x.ljust        | x.rstrip 
x.center     |   x.isdecimal   |  x.lower       |  x.split
x.count      |   x.isdigit     |  x.lstrip      |  x.splitlines
x.encode     |   x.isidentifier|  x.maketrans   |  x.startswith
x.endswith   |   x.islower     |  x.partition   |  x.strip
x.expandtabs |   x.isnumeric   |  x.replace     |  x.swapcase
x.find       |   x.isprintable |  x.rfind       |  x.title
x.format     |   x.isspace     |  x.rindex      |  x.translate
x.format_map |   x.istitle     |  x.rjust       |  x.upper
x.index      |   x.isupper     |  x.rpartition  |  x.zfill


Inutile de toutes les connaître. Nous allons voir ici les fonctions les plus utiles.

## Couper et joindre

La fonction ***split()*** permet de ***découper*** la chaîne de caractères qui lui est passée en paramètre suivant un ou des caractère(s) de séparation et renvoie une liste des chaînes découpées. Les caractères de séparation lui sont également passés en paramètre et, si ce n'est pas le cas, ce sera le caractère espace qui sera utilisé :


```python
chaine="Lycée Saint Sauveur - Redon"
chaine.split()
```

```python
chaine.split('-')
```

L'opération inverse s'appelle ***join()***. Elle consiste a rendre une liste de chaînes de caractères pour former une chaîne en concaténant tous les éléments et en les assemblant à l'aide d'un caractère.

Cette méthode prend en paramètre une liste de caractères et s'applique à une chaîne de caractères désignant le ou les caractère(s) de liaison :


```python
liste = ['Lycée Saint Sauveur', 'Redon']
' - '.join(liste)
```

## Majuscule et minuscule

Deux autres méthodes standards peuvent être utiles:

***lower()*** et ***upper()*** permettant respectivement de convertir les caractères d'une chaîne en minuscules ou en majuscules.  
Attention, bien que parlant de *conversion*, ces méthodes ne modifient pas la chaîne de départ mais renvoient une nouvelle chaîne :


```python
chaine.upper()
```


```python
chaine.lower()
```

La fonction ***capitalize()*** permet de ne mettre en majuscule que la première lettre d'une chaîne :


```python
chaine.capitalize()
```

## rechercher un caractère, une position etc... dans une chaîne.

- La fonction ***len()*** permet, comme pour les listes, de connaîntre la longueur de la chaîne, c'est à dire compter le nombre de caractères.


```python
chaine = "Lycée Saint Sauveur"
len(chaine)
```

- La méthode ***count()*** permet de compter le nombre d'occurrences d'une sous chaîne dans une chaîne de caractères.   
Le premier paramètre est la chaîne dans laquelle effectuer la recherche et le second paramètre est la sous chaîne :


```python
chaine.count('a')
```

- La méthode ***find()*** permet de trouver l'indice de la première occurrence d'une sous chaîne. Les paramètres sont les mêmes que pour la fonction ***count()***  
En cas d'échec, ***find()*** renvoie la valeur -1 ( 0 correspond à l'indice du premier caractère):
On utilisera ***rfind()*** pour la dernière ocurrence.


```python
chaine.find('a')
```


```python
chaine.find('b')
```


```python
chaine.rfind('a')
```

- index() est identique à find() mais retourne une erreur en cas d'échec


```python
chaine.index('a')
```


```python
chaine.index('b')
```

- La fonction ***replace()*** permet, comme son nom l'indique, de remplacer une sous chaîne par une autre à l'intérieur d'une chaîne de caractères.  
Les paramètres sont, dans l'ordre : la chaîne de caractères à modifier, la sous chaîne à remplacer, la sous chaîne de remplacement,et, éventuellement, le nombre maximum d'occurrences à remplacer (si non spécifié, toutes les occurrences seront remplacées).


```python
chaine.replace('a','@')
```

et bien sûr, la variable *chaine* n'est pas modifiée, c'est une nouvelle chaine qui est renvoyée par cette méthode !


```python
chaine
```

## Conversion chaîne <-> nombres

Il ne faut pas confondre les objets 12 et "12". Le premier désigne un nombre, le second est une chaîne de caractère. Les comportements et les opérations sont différents.


```python
12 == "12"
```


```python
12+1
```


```python
"12"+"1"
```

Il peut être néanmoins possible de convertir un nombre en chaîne et réciproquement comme on va le voir sur les exemples ci-dessous


```python
int("12")
```


```python
str(12)
```

## Comparaison de chaînes de caractères
De même qu'il est possible de comparer deux nombres, on peut aussi comparer des chaines par rapport à l'ordre lexicographique :


```python
"a"<"b"
```


```python
"a"<="r"<="z"
```


```python
"a"<="R"<="z"
```


```python
"toto"<"titi"
```

## Tranches de chaînes

Le tranchage (*slicing*) fonctionne exactement comme pour les listes. Observez les exemples suivants.


```python
chaine = "Lycée Saint Sauveur"
# obtenir la fin d'une chaîne
chaine[6:]
```


```python
# obtenir le début d'une chaîne
chaine[:5]
```


```python
# Un intervalle
chaine[6:14]
```

Et avec des index négatifs ...


```python
chaine[-1]
```


```python
chaine[:-1]
```


```python
# ce dernier exemple est très pratique pour renverser un itérable
chaine[::-1]
```

## Parcourir une chaîne de caractères

Une chaîne de raractère en Python rentre dans la catégorie des *itérables* au même titre que les listes. On retrouve donc les deux modes de parcours déjà rencontrés sur les listes, à savoir :


```python
# Le parcours caractères par caractères :
chaine = "NSI"
for c in chaine:
    print(c)
```


```python
# Le parcours par indice
chaine = "NSI"
for i in range(len(chaine)):
    print(chaine[i])
```