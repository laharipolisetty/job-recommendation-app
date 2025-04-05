def match_jobs(user_skills):
    job_database = {
        "Data Scientist": ["Python", "Machine Learning", "Data Analysis"],
        "ML Engineer": ["Python", "Deep Learning", "SQL"],
        "Data Analyst": ["SQL", "Data Analysis", "Python"],
        "AI Researcher": ["Deep Learning", "Machine Learning", "Python"]
    }

    matched_jobs = []
    for job, skills_required in job_database.items():
        if any(skill in user_skills for skill in skills_required):
            matched_jobs.append(job)

    return matched_jobs
