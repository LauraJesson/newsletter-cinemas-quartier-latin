import requests
from bs4 import BeautifulSoup
from cinemas import CINEMAS


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "Chrome/120 Safari/537.36"
    )
}


def extraire_texte_page(url):
    """
    Récupération simple d'une page HTML.
    Sera remplacée par des extracteurs spécifiques cinéma par cinéma.
    """

    response = requests.get(
        url,
        timeout=15,
        headers=HEADERS
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    texte = soup.get_text(" ", strip=True)

    return texte[:2000]


def recuperer_programme(cinema):
    """
    Lance la récupération pour un cinéma.
    """

    print(f"🎬 Récupération : {cinema['nom']}")

    try:

        contenu = extraire_texte_page(
            cinema["url"]
        )

        return {
            "cinema": cinema["nom"],
            "url": cinema["url"],
            "contenu": contenu
        }


    except requests.exceptions.SSLError as e:

        return {
            "cinema": cinema["nom"],
            "erreur": "Erreur certificat SSL : " + str(e)
        }


    except requests.exceptions.Timeout:

        return {
            "cinema": cinema["nom"],
            "erreur": "Le site ne répond pas (timeout)"
        }


    except Exception as e:

        return {
            "cinema": cinema["nom"],
            "erreur": str(e)
        }



def recuperer_tous_les_programmes():

    programmes = []

    for cinema in CINEMAS:

        programme = recuperer_programme(cinema)

        programmes.append(programme)


    return programmes



if __name__ == "__main__":

    resultats = recuperer_tous_les_programmes()

    for resultat in resultats:

        print("\n----------------")
        print(resultat["cinema"])

        if "erreur" in resultat:
            print("❌", resultat["erreur"])

        else:
            print(resultat["contenu"][:500])