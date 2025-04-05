def identify_skill_gaps(user_skills):
    ideal_skills = ["Python", "Machine Learning", "Deep Learning", "SQL", "Data Analysis", "Streamlit"]
    missing_skills = list(set(ideal_skills) - set(user_skills))
    return missing_skills
