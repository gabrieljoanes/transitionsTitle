import openai
import re
import random
import json

def generate_transitions_and_output(text):
    segments = re.split(r'\bTRANSITION\b', text)
    transitions = []
    output = ""

    for i in range(len(segments)-1):
        para_a = segments[i].strip()
        para_b = segments[i+1].strip()
        prompt = f"{para_a}\nTRANSITION\n{para_b}"

        transition = "Dans une autre actualité,"  # Simulated placeholder
        transitions.append(transition)

    for i in range(len(transitions)):
        output += segments[i].strip() + " " + transitions[i] + " "
    output += segments[-1].strip()

    # Insert À savoir également dans votre département logic
    output_parts = output.split("\n")
    first_part = output_parts[0].strip()
    rest = "\n".join(output_parts[1:]).strip()
    final_output = f"{first_part}\n\nÀ savoir également dans votre département\n\n{rest}"

    return final_output, transitions