
import openai

def generate_title_and_blurb(full_text):
    prompt = f"Voici un article de presse :\n\n{full_text}\n\nDonne-moi un titre court et un chapô (blurb) de 2 à 3 lignes maximum, en français."
    messages = [
        {"role": "system", "content": "Tu es un journaliste expert en presse locale."},
        {"role": "user", "content": prompt}
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Erreur lors de la génération du titre et du chapô : {e}]"
