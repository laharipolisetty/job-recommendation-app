import PyPDF2
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ''
    return text

def extract_skills_experience(text):
    doc = nlp(text)
    skills = []
    experience = []

    skill_keywords = ["Python", "Machine Learning", "Deep Learning", "SQL", "Streamlit", "Data Analysis"]
    for token in doc:
        if token.text in skill_keywords:
            skills.append(token.text)

    for sent in doc.sents:
        if "experience" in sent.text.lower():
            experience.append(sent.text.strip())

    return list(set(skills)), " ".join(experience) or "No experience described"
