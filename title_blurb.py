def generate_title_blurb(text):
    first_paragraph = text.split("TRANSITION")[0].strip().split("\n")[0].strip()
    title = first_paragraph[:80] + ("…" if len(first_paragraph) > 80 else "")
    blurb = first_paragraph
    return title, blurb