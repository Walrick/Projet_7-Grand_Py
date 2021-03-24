# Projet 7 - GrandPy Bot, le papy-robot 🤖 👴

--------------------------------------------------

## Utilisation 

Aller sur le lien suivant : http://grandpy.jeremycombes.fr/

Papy t'abordera :

> Bonjour mon poussin, que voudrais-tu savoir aujourd'hui ?

Poser lui une question pour connaitre l'adresse d'un lieu :

> Salut Papy ! tu connais l'adresse d'Openclassrooms ?

Et il repondra :

> J'ai trouvé mon agneau, Openclassrooms se situe au 10 Quai de la Charente, 75019 Paris, France, regarde la carte.

il proposera une autre réponse avec la carte et aussi une info sur une zone proche :

> Il me semble que dans la zone il se trouve Quai de la Gironde, a peu pres à 114.2 m, Il fait face au quai de la Charente, commence au quai de l'Oise et se termine avenue Corentin-Cariou. La ligne 3b du tramway passe sur ce quai.

## Utilisation en local

Crée un fichier .env et ajouter une clé google API :

> API_GOOGLE = ""

Modifier app.py et ajouter une ligne de code apres la fonction <setup_local()> ajouter :

> setup_local() 

pour pouvoir lancer la fonction.

Utiliser python 3.9 et pip install -r requirements.txt

## API utilisée

Cette application utilise :
- Google Maps et Google Place de Google
- MediaWiki de wikipedia

