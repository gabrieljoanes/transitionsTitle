
import openai
import re

def extract_first_paragraph(text):
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    return paragraphs[0] if paragraphs else "", "\n".join(paragraphs[1:]) if len(paragraphs) > 1 else ""

def generate_title_and_blurb(first_paragraph):
    prompt = f"Voici le début d’un article de presse local :\n\n{first_paragraph}\n\nDonne-moi un titre court (max 15 mots) et un chapô de 2 à 3 lignes maximum. Le titre doit contenir le lieu et la date si présents."
    messages = [
        {"role": "system", "content": "Tu es un journaliste local expérimenté. Le titre doit être factuel et accrocheur. Le chapô doit résumer l’essentiel."},
        {"role": "user", "content": prompt}
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0.5,
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Erreur lors de la génération du titre et du chapô : {e}]"

def build_structured_article(first_paragraph, rest_with_transitions):
    # Strip any duplicated title
    banner = "À savoir également dans votre département"
    parts = re.split(rf"(?i){banner}", rest_with_transitions)
    body_after_banner = parts[-1].strip() if len(parts) > 1 else rest_with_transitions.strip()
    return f"{first_paragraph.strip()}\n\n{banner}\n\n{body_after_banner}"
