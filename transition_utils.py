
import openai
import re
import random
import json

def load_examples():
    with open("examples.jsonl", "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]

def generate_transitions(input_text, examples_data):
    banner = "À savoir également dans votre département"
    # Split by banner if present
    if banner in input_text:
        before, after = input_text.split(banner, 1)
    else:
        before, after = input_text, None

    segments = re.split(r'\bTRANSITION\b', before)
    transitions = []

    for i in range(len(segments)-1):
        para_a = segments[i].strip()
        para_b = segments[i+1].strip()
        prompt = f"{para_a}\nTRANSITION\n{para_b}"

        shots = random.sample(examples_data, k=3)
        messages = [
            {"role": "system", "content": "You are a French news assistant that replaces the word TRANSITION with a short, natural and context-aware phrase (5–10 words) that logically connects two paragraphs."}
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

        if para_a and transition:
            last_word = para_a.strip().split()[-1].lower()
            first_word = transition.strip().split()[0].lower()
            if last_word == first_word:
                transition = ' '.join(transition.strip().split()[1:])

        transitions.append(transition)

    rebuilt = ""
    for i in range(len(transitions)):
        rebuilt += segments[i].strip() + f" *{transitions[i]}* "
    rebuilt += segments[-1].strip()

    if after:
        return transitions, f"{rebuilt.strip()}\n\n{banner}\n\n{after.strip()}"
    else:
        return transitions, rebuilt.strip()
