
def generate_title_and_blurb(text):
    lines = text.strip().split("\n")
    first_para = ""
    for line in lines:
        if line.strip():
            first_para = line.strip()
            break
    title = first_para[:60] + "..." if len(first_para) > 60 else first_para
    return title.strip(), first_para.strip()
