import streamlit as st
import openai
import re
import random
import json
from title_blurb import generate_title_blurb
from transition_logic import generate_transitions_and_output

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="🧠 Générateur de transitions + Titre/Chapô structuré v10")
st.title("🧠 Générateur de transitions + Titre/Chapô structuré (v10)")
st.markdown("Collez un texte avec plusieurs `TRANSITION`. L'app générera un titre, un chapô et intégrera les transitions en respectant la structure demandée.")

input_text = st.text_area("✍️ Texte de l'article (avec TRANSITION)", height=400)

if st.button("✨ Générer le titre, chapô et transitions"):
    if "TRANSITION" not in input_text:
        st.warning("Aucun mot-clé TRANSITION trouvé dans le texte.")
    else:
        title, blurb = generate_title_blurb(input_text)
        full_output, transitions = generate_transitions_and_output(input_text)

        st.markdown("### 📰 Titre")
        st.markdown(f"{title}")

        st.markdown("### ✍️ Chapô")
        st.markdown(f"{blurb}")

        st.markdown("---")
        st.markdown("### 🔁 Transitions insérées dans l'article")
        st.markdown(full_output)

        st.markdown("---")
        st.markdown("### 🧩 Transitions générées individuellement")
        for i, t in enumerate(transitions, 1):
            st.markdown(f"**Transition {i} :** {t}")