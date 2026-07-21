import os
import resend


def envoyer_newsletter(html):
    """
    Envoie la newsletter via Resend.
    La clé API est récupérée depuis GitHub Secrets.
    """

    resend.api_key = os.environ.get("RESEND_API_KEY")

    if not resend.api_key:
        raise Exception(
            "La clé RESEND_API_KEY est absente."
        )

    email = resend.Emails.send(
        {
            "from": "Newsletter Quartier latin <onboarding@resend.dev>",
            "to": ["madeleine.dechaisemartin@gmail.com"],
            "subject": "🎬 Cette semaine dans les cinémas du Quartier latin",
            "html": html,
        }
    )

    return email