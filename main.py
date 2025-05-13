
import streamlit as st
import openai
from transition_utils import load_examples, generate_transitions
from title_blurb_generator import generate_title_and_blurb
from structured_output_formatter import extract_first_paragraph, build_structured_article

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🧠 Générateur de transitions + Titre/Chapô structuré")
st.markdown("Collez un texte avec plusieurs `TRANSITION`. L'app générera un titre, un chapô et intégrera les transitions en respectant la structure demandée.")

examples_data = load_examples()
input_text = st.text_area("✍️ Texte de l'article (avec TRANSITION)", height=350)

if st.button("✨ Générer l'article structuré"):
    if "TRANSITION" not in input_text:
        st.warning("Le mot-clé TRANSITION est introuvable.")
    else:
        transitions, rebuilt = generate_transitions(input_text, examples_data)
        first_para, rest = extract_first_paragraph(rebuilt)

        st.markdown("### 📝 Transitions suggérées :")
        for i, t in enumerate(transitions, 1):
            st.markdown(f"**Transition {i}:** {t}")

        st.markdown("---")
        title_blurb = generate_title_and_blurb(first_para)

        st.markdown("### 📰 Titre + Chapô :")
        st.text_area("Suggestion automatique :", value=title_blurb, height=150)

        st.markdown("---")
        st.markdown("### 🧾 Article structuré final :")
        formatted = build_structured_article(first_para, rest)
        st.text_area("Article complet", value=formatted, height=500)
