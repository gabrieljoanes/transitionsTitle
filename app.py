
import streamlit as st
import openai
import re
import random
import json

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🧠 Générateur de transitions – Version 10")

@st.cache_data
def load_examples():
    with open("examples.jsonl", "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]

examples_data = load_examples()

input_text = st.text_area("✍️ Texte de l'article (avec TRANSITION)", height=350)

if st.button("✨ Générer les transitions et structurer l'article"):
    if "TRANSITION" not in input_text:
        st.warning("Aucun mot-clé TRANSITION trouvé dans votre texte.")
    else:
        first_split = re.split(r"\n\s*À savoir également dans votre département\s*\n", input_text, maxsplit=1)
        if len(first_split) != 2:
            st.error("Le texte doit contenir une seule fois 'À savoir également dans votre département'.")
        else:
            intro_text = first_split[0].strip()
            rest_text = first_split[1].strip()

            segments = re.split(r'\bTRANSITION\b', rest_text)
            transitions = []

            for i in range(len(segments) - 1):
                para_a = segments[i].strip()
                para_b = segments[i + 1].strip()
                prompt = f"{para_a}\nTRANSITION\n{para_b}"

                shots = random.sample(examples_data, k=3)
                messages = [
                    {"role": "system", "content": "You are a French news assistant that replaces TRANSITION with a short, natural, context-aware phrase (5–10 words) that logically connects two news paragraphs."}
                ]
                for s in shots:
                    messages.extend(s["messages"])
                messages.append({"role": "user", "content": prompt})

                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=messages,
                        temperature=0.7,
                        max_tokens=20
                    )
                    transition = response.choices[0].message.content.strip()
                except Exception as e:
                    transition = f"[ERROR: {e}]"

                transitions.append(transition)

            st.markdown("### 📰 Titre")
            st.markdown(intro_text.split(".")[0] + "...")

            st.markdown("### ✍️ Chapô")
            st.markdown(intro_text)

            st.markdown("### 🔁 Transitions insérées dans l'article")

            final_article = intro_text + "\n\nÀ savoir également dans votre département\n\n" + segments[0].strip()
            for i in range(len(transitions)):
                final_article += " " + transitions[i].strip() + " " + segments[i + 1].strip()

            st.markdown(final_article)

            st.markdown("### 🧩 Transitions générées individuellement")
            for i, t in enumerate(transitions, 1):
                st.markdown(f"**Transition {i}** : {t}")
