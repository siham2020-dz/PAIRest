# POEI_Inetum_Safran_G1_EndProject

## Pré-requis

* Python 3
* https://wkhtmltopdf.org/downloads.html

## Installation

* Clonez le repository sur votre machine locale
* Ouvrez une console de commande et naviguez jusqu'à ce dossier
* Executez ```pip install -r requirements.txt```

## Fonctionnement

### Lancement de l'API
* Ouvrez une console de commande et naviguez jusqu'à ce dossier
* Executez ```python app.py```
* Attendez que le serveur se lance
* Dans votre navigateur, allez sur ```http://127.0.0.1:5000/get_summary/{id}``` en remplacant {id} par l'id du véhicule recherché

### Lancement du client
* Ouvrez une console de commande et naviguez jusqu'au dossier ```client```
* Executez ```python -m http.server 8000```
* Attendez que le serveur se lance
* Dans votre navigateur, allez sur ```http://127.0.0.1:8000```