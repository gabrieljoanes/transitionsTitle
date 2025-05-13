
import streamlit as st
import openai
import re
from title_blurb import generate_title_and_blurb
from transition_logic import insert_transitions

st.set_page_config(page_title="Générateur de transitions + Titre/Chapô structuré (v12)")

st.title("🧠 Générateur de transitions + Titre/Chapô structuré (v12)")
st.markdown("Collez un texte avec plusieurs TRANSITION. L'app générera un titre, un chapô et intégrera les transitions en respectant la structure demandée.")

openai.api_key = st.secrets["OPENAI_API_KEY"]

user_input = st.text_area("✍️ Texte de l'article (avec TRANSITION)", height=500)

if st.button("Générer"):
    if user_input:
        title, blurb = generate_title_and_blurb(user_input)
        full_output, transitions_used = insert_transitions(user_input)

 st.markdown(f"""### 📰 Titre
{title}""")

st.markdown(f"""### ✍️ Chapô
{blurb}""")

        st.markdown("### 🧾 Article final")
        st.markdown(full_output)

        st.markdown("### 🔄 Transitions insérées")
        for i, t in enumerate(transitions_used, 1):
            st.markdown(f"**{i}.** {t}")
    else:
        st.warning("Veuillez coller un texte pour générer la sortie.")
