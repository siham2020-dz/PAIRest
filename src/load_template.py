from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from PyPDF2 import PdfReader

import pdfkit
import os

# Nettoie et formate une chaîne de caractères
def clean_string(s):
    return ' '.join(s.split())

def get_pages_for_section(pdf_path, section_title):
    """
    Récupère les numéros des pages d'un fichier PDF où un titre de section spécifique est mentionné.

    Paramètres:
    - pdf_path (str) : Chemin vers le fichier PDF.
    - section_title (str) : Titre de la section à rechercher dans le PDF.

    Retour:
    Une liste de numéros de pages où le titre de la section est mentionné.
    """
    
    pages = []
    
    clean_title = clean_string(section_title)
    
    with open(pdf_path, "rb") as file:
        # Création d'un lecteur de PDF pour parcourir les pages
        reader = PdfReader(file)
        # Parcours de chaque page du PDF
        for page_num, page in enumerate(reader.pages):
            # Si le titre nettoyé est trouvé dans le texte nettoyé de la page
            if clean_title in clean_string(page.extract_text()):
                pages.append(page_num + 1)

    return pages


def get_poste_pages(pdf_path, posts):
    """
    Récupère les pages des postes spécifiés dans le fichier PDF donné.

    Paramètres:
    - pdf_path (str) : Le chemin vers le fichier PDF.
    - posts (list) : Une liste de postes.

    Retour:
    Un dictionnaire où les clés sont les noms des postes et les valeurs sont les pages associées dans le PDF.
    """
    
    poste_pages = {}
    for post in posts:
        poste_name = post[1]
        search_string = f"déclarés sur le poste de travail {poste_name}"
        pages_for_poste = get_pages_for_section(pdf_path, search_string)
        poste_pages[poste_name] = pages_for_poste[0]
    
    return poste_pages

# Crée un PDF basé sur un template HTML et des données
def create_pdf(data):
    templateLoader = FileSystemLoader(searchpath="./")
    templateEnv = Environment(loader=templateLoader)
    
    template = templateEnv.get_template("./template/template.html")

    # Génère un PDF préliminaire pour analyse
    outputText = template.render(vehicule=data, pages_per_post={})
    filename = f"{data['desc']}-{datetime.now().date()}".replace('\n', '')
    pdfPath = f'./output/{filename}_temp.pdf'
    
    options = {
        'header-html': './template/header.html',
        'footer-right': '[page]',
        'margin-top': '50mm',
        'margin-bottom': '20mm',
        'allow': ['./template/assets/logo.jpg',],
    }

    pdfkit.from_string(outputText, pdfPath, options=options)

    # Obtenir les numéros de page pour chaque section et poste
    pages_per_post = get_poste_pages(pdfPath, data['posts_distinct'])
    print(pages_per_post)

    outputText = template.render(
        vehicule=data, 
        # Données pour table des matières
        resume_page=get_pages_for_section(pdfPath, "Ce rapport a pour but d’informer")[0],
        incidents_page=get_pages_for_section(pdfPath, "Le tableau ci-dessous montre la liste des incidents pour le véhicule")[0], 
        incidents_details_page=get_pages_for_section(pdfPath, "Liste détaillé des incidents")[0],
        pages_per_post=pages_per_post
    )

    # Génère le PDF final et supprime les fichiers temporaires
    pdfkit.from_string(outputText, f'./output/{filename}.pdf', options=options)
    os.remove(pdfPath)
    
    return f'/download/{filename}'
