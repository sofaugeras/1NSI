# Mini Projet : Analyse de données

!!! note "Projet exemple"

    sources : [les monuments de Paris](data/monuments_paris.zip)

    Installation de la bibliothèque FOLIUM :
    Lancer Anaconda. Puis aller dans les applications Windows pour lancer la console Anaconda Prompt.<br />
    Taper la commande suivante : `pip install folium`<br />
    Vérifier qu’il n’y a pas d’erreur dans la console. <br />

    **A faire :**<br />
    Ouvrir dans Spyder le programme `monuments_paris.py`et le lancer.<br />
    ⚠️ les deux fichiers `monuments_paris.py` et `monuments_GPS.csv` doivent se trouver le même répertoire. <br />
    Cela génère un fichier `maCarte4.html` qui devrait se trouver dans le même répertoire que votre programme.<br />
    **Analyse :**
    Analyser les différentes fonctions qui vous sont fourni. 

!!! info "Consignes"
    Il s’agit ici de prendre en charge un jeu de données (open DataSet), de l’exploiter et d’en faire une restitution graphique.
    Nous allons partir sur un mini-projet, à rendre après les vacances le <mark>Vendredi 25 Mars 2024</mark> et réalisé en BINOME.

    **Consignes générales :**<br />
    A partir d’une source de données choisies ou créées par vous, créer un programme Python d’acquisition (à partir d’un fichier CSV) et de restitution de données. La restitution pourra être source forme de tableaux (bibliothèque panda), de graphique (bibliothèque matplotlib) ou de carte (bibliothèque folium)
 
## Les données : 
Bibliothèques de données (la liste est donnée à titre indicative, il existe d’autres sources de données) :<br />
▶️ [openData Gouv](https://www.data.gouv.fr/fr/datasets/)<br />
▶️ [openData Bretagne](https://data.bretagne.bzh/explore/?sort=modified)<br />
▶️ [Kaggle](https://www.kaggle.com/datasets)<br />
▶️ [onisep](https://opendata.onisep.fr/34-recherche.htm?idtf=34&idPage=34&q=csv&from=0&type=dataset)

## AIDE : 
Tutoriel bibliothèque Panda : <br />
- [cours](T6_Traitement_de_donnees/6.3_Pandas/cours.md)<br />
- [tuto d initiation panda et matplotlib](https://www.actuia.com/tutoriel/tutoriel-dinitiation-a-lia-python-pandas-et-matplotlib-partie-2/)

## IDEE de PROJET : 
:bulb: Evolution du nombre de morts par épisodes dans Games of Thrones<br />
:bulb: Origines géographiques des passagers du Titanic<br />
:bulb: Cartographies des monuments remarquables en Bretagne<br />
:bulb: Analyse des l’origine des TOP1 de Spotify sur les 5 dernières années<br />
:bulb: ….

## Evaluation :
Vous trouverez la fiche d'évaluation [ici](data/FicheEvaluationCSV.pdf)<br />
📖 Vous veillerez à documenter vos fonctions et différents programmes.<br />
📁 Vous devrez également fournir un document accompagnateur expliquant votre projet et votre démarche. Le document accompagnateur pourra être un site web, une présentation sous forme de slide, ou un rapport.


## Coup de pouce 

Un besoin recurrent sur ces projets est de pouvoir associer un dataset contenant une ville ou la capitale d'un pays avec ses coordonnées latitude/longitude pour pouvoir positionner un marqueur folium.<br />
Voici un petit bout de code, qui à partir d'un fichier CSV contenant une ville, recréer un nouveau fichier CSV contenant la latitude et la longitude.

```python
import pandas as pd
import requests

# Charger le fichier CSV contenant les noms des pays avec les noms de leurs capitales
df = pd.read_csv('pays2.csv', encoding = 'utf-8')

# Fonction pour obtenir les coordonnées géographiques d'une capitale donnée
def get_coordinates_city(city):
    # Utilisation de l'API openstreetmap 
    url = f"https://nominatim.openstreetmap.org/search?city={city}&format=json"
    response = requests.get(url)
    data = response.json()
    if data:
        return data[0]['lat'], data[0]['lon']
    else:
        # Si on ne trouve pas la ville, renvoie None
        return None, None

def get_coordinates_country(country):
     # Utilisation de l'API openstreetmap 
    url = f"https://nominatim.openstreetmap.org/search?country={country}&format=json"
    response = requests.get(url)
    data = response.json()
    if data:
        return data[0]['lat'], data[0]['lon']
    else:
        # Si on ne trouve pas le pays, renvoie None
        return None, None

# Obtenir les coordonnées géographiques pour chaque capitale
for index, row in df2.iterrows():
    # Un petit rpint pour vérifier que le traitement avance ...
    print(row['Capital'])
    # Récupération des coordonnées en fonction d'une ville
    latitude, longitude = get_coordinates_city(row['Capital'])
    df.at[index, 'Latitude'] = latitude
    df.at[index, 'Longitude'] = longitude
    # Récupération des coordonnées en fonction d'un pays, coordonnées de la capitale
    latitude2, longitude2 = get_coordinates_country(row['pays'])
    df.at[index, 'Latitude2'] = latitude2
    df.at[index, 'Longitude2'] = longitude2

# Enregistrer le nouveau dataset avec les coordonnées géographiques
df.to_csv("nouveau_dataset.csv", index=False)
```