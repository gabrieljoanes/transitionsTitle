
import re

TRANSITIONS = [
    "Cependant, dans un autre coin de la Bretagne,",
    "En parallèle, dans les communes voisines,",
    "En changeant de sujet pour se concentrer sur l'histoire locale,"
]

def insert_transitions(text):
    banner = "À savoir également dans votre département"
    if banner not in text:
        return text, []

    before, after = text.split(banner, 1)
    after = after.replace(banner, "")  # remove accidental duplicate

    segments = after.split("TRANSITION")
    output = before.strip() + "\n\n" + banner + "\n\n"

    transitions_used = []

    for i, seg in enumerate(segments):
        seg = seg.strip()
        if not seg:
            continue
        if i == 0:
            # First paragraph after banner: no transition
            output += seg
        else:
            transition = TRANSITIONS[i - 1] if i - 1 < len(TRANSITIONS) else "[...]"
            transitions_used.append(transition)
            output += "\n" + transition + "\n" + seg

    return output.strip(), transitions_used
