import requests
from bs4 import BeautifulSoup
from cinemas import CINEMAS


def recuperer_programme(cinema):
    """
    Récupère une première version du programme d'un cinéma.
    Cette version prépare la structure :
    chaque cinéma pourra ensuite avoir son extracteur spécifique.
    """

    print(f"Récupération : {cinema['nom']}")

    try:
        response = requests.get(
            cinema["url"],
            timeout=10,
            headers={
                "User-Agent": "Newsletter Cinemas Quartier Latin"
            }
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")

        return {
            "cinema": cinema["nom"],
            "url": cinema["url"],
            "contenu": soup.get_text(" ", strip=True)[:1000]
        }

    except Exception as e:
        return {
            "cinema": cinema["nom"],
            "erreur": str(e)
        }


def recuperer_tous_les_programmes():
    programmes = []

    for cinema in CINEMAS:
        programmes.append(
            recuperer_programme(cinema)
        )

    return programmes


if __name__ == "__main__":
    resultats = recuperer_tous_les_programmes()

    for resultat in resultats:
        print("\n---")
        print(resultat)