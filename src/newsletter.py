from datetime import datetime


def generer_newsletter(programmes):
    date = datetime.now().strftime("%d/%m/%Y")

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Newsletter Cinémas du Quartier latin</title>
    </head>

    <body style="font-family: Arial, sans-serif; color:#222;">

        <h1>🎬 Cette semaine dans les cinémas indépendants du Quartier latin</h1>

        <p>Programmation récupérée le {date}</p>

    """

    for cinema in programmes:
        html += f"""
        <hr>
        <h2>📍 {cinema.get('cinema')}</h2>
        """

        if "erreur" in cinema:
            html += f"""
            <p>Impossible de récupérer le programme :
            {cinema['erreur']}</p>
            """
        else:
            contenu = cinema.get("contenu", "")

            html += f"""
            <p>
            {contenu}
            </p>
            """

    html += """
        <hr>

        <h2>🎞️ Rétrospectives et cycles</h2>
        <p>
        Cette rubrique sera enrichie automatiquement dans une prochaine version.
        </p>

        <h2>🎤 Rencontres, conférences et débats</h2>
        <p>
        Cette rubrique sera enrichie automatiquement dans une prochaine version.
        </p>

    </body>
    </html>
    """

    return html