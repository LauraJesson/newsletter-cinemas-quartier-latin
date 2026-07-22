from collecte import recuperer_tous_les_programmes
from newsletter import generer_newsletter
from envoi import envoyer_newsletter


def main():

    print("🎬 Début de la génération de la newsletter")

    programmes = recuperer_tous_les_programmes()

    print("===== PROGRAMMES RÉCUPÉRÉS =====")

    for p in programmes:
        print(
            p.get("cinema"),
            p.get("url")
        )

    print("📝 Création de la newsletter")

    html = generer_newsletter(programmes)

    print("✉️ Envoi de la newsletter")

    envoyer_newsletter(html)

    print("✅ Newsletter envoyée avec succès")


if __name__ == "__main__":
    main()