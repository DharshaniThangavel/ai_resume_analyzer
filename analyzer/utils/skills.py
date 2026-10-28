import re

# Comprehensive list of standard tech stack keywords to look for
TECH_KEYWORDS = [
    'python', 'django', 'fastapi', 'flask', 'java', 'c++', 'c', 'javascript', 
    'react', 'node.js', 'sql', 'mysql', 'postgresql', 'mongodb', 'git', 
    'docker', 'kubernetes', 'aws', 'gcp', 'azure', 'machine learning', 
    'nlp', 'pandas', 'numpy', 'scikit-learn', 'tensorflow', 'pytorch', 
    'html', 'css', 'tailwind', 'bootstrap', 'rest api', 'graphql', 'linux'
]

def analyze_skills(resume_text, jd_text):
    """
    Extracts tech keywords from JD and checks presence in the resume.
    Returns matched skills and missing required skills.
    """
    if not resume_text or not jd_text:
        return [], []

    resume_lower = resume_text.lower()
    jd_lower = jd_text.lower()

    found_in_jd = set()
    for skill in TECH_KEYWORDS:
        # Use word boundary regex to avoid partial substring matches (e.g., 'c' matching inside 'code')
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, jd_lower):
            found_in_jd.add(skill)

    matched_skills = []
    missing_skills = []

    for skill in found_in_jd:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, resume_lower):
            matched_skills.append(skill.title())
        else:
            missing_skills.append(skill.title())

    return sorted(list(matched_skills)), sorted(list(missing_skills))