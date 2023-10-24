import pandas as pd

def get_datas(cur, id):
    """
    Récupère les données de la base en fonction de l'ID fourni.

    Args:
    - cur : Curseur de la connexion à la base de données
    - id : Identifiant pour lequel récupérer les données

    Returns:
    - Dictionnaire contenant différentes données récupérées
    """
    
    # Récupère les données en utilisant le SQL depuis un fichier
    def fetch_data_from_file(file_path, cur, id):
        with open(file_path, 'r') as file:
            query = file.read()
        res = cur.execute(query, [str(id)])
        return res.fetchall()

    # Récupération des données pour la page de garde
    return_response = {
        "desc": fetch_data_from_file("./sql/return_desc.sql", cur, id)[0][0],
        "incidents": fetch_data_from_file("./sql/return_all_incidents.sql", cur, id),
        "posts": fetch_data_from_file("./sql/get_incidents_on_posts.sql", cur, id)
    }

    # Extraction des postes distincts
    posts = return_response["posts"]
    posts_distinct = {elem[2]: elem[3] for elem in posts}.items()
    return_response["posts_distinct"] = list(posts_distinct)
    
    return return_response
