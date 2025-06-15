import pdfplumber
import spacy
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Read the resume content
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Extract sections using regex keywords
def extract_sections(text):
    sections = {
        "contact_info": "",
        "education": "",
        "experience": "",
        "skills": ""
    }

    lower_text = text.lower()
    
    # Simple regex to grab emails and phone numbers
    sections["contact_info"] = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    sections["contact_info"] += re.findall(r"\+?\d[\d -]{8,12}\d", text)

    # Extract key sections
    education_match = re.search(r"(education|academic background)(.*?)(experience|projects|skills)", lower_text, re.DOTALL)
    experience_match = re.search(r"(experience|work history)(.*?)(projects|skills|education)", lower_text, re.DOTALL)
    skills_match = re.search(r"(skills|technical skills)(.*?)(experience|projects|education)", lower_text, re.DOTALL)

    sections["education"] = education_match.group(2).strip() if education_match else ""
    sections["experience"] = experience_match.group(2).strip() if experience_match else ""
    sections["skills"] = skills_match.group(2).strip() if skills_match else ""

    return sections

# Scoring logic
def score_resume(sections):
    score = 0
    feedback = []

    # Contact info
    if len(sections["contact_info"]) >= 2:
        score += 10
    else:
        feedback.append("Add email and phone number in contact info.")

    # Education
    if sections["education"]:
        score += 20
    else:
        feedback.append("Add an 'Education' section with degrees and universities.")

    # Experience
    if sections["experience"]:
        score += 30
    else:
        feedback.append("Include a detailed 'Experience' section with job titles and dates.")

    # Skills
    if sections["skills"]:
        score += 20
    else:
        feedback.append("List out relevant skills, ideally in bullet points.")

    # Formatting and keyword check
    keywords = ["Python", "SQL", "project", "team", "developed", "managed"]
    keyword_count = sum(1 for word in keywords if word.lower() in sections["experience"].lower())
    score += min(20, keyword_count * 2)
    if keyword_count < 5:
        feedback.append("Include more job-relevant keywords in your experience section.")

    return min(score, 100), feedback

# Run the tool
pdf_path = "/mnt/data/file-1bFWh1xHW2QSszT7ZdNYJk"
text = extract_text_from_pdf(pdf_path)
sections = extract_sections(text)
score, feedback = score_resume(sections)

# Output result
print(f"Resume Score: {score}/100")
print("Feedback:")
for tip in feedback:
    print(f"- {tip}")