import streamlit as st
from database import init_db, save_user_profile, fetch_profiles
from resume_parser import extract_text_from_pdf, extract_skills_experience
from job_matcher import match_jobs
from skill_gap import identify_skill_gaps

# Initialize database
init_db()

st.set_page_config(page_title="AI Job Recommender", layout="wide")

st.sidebar.title("🧩 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Upload Resume", "View Past Profiles"])

if page == "Home":
    st.title("Welcome to AI Job Recommendation System 🚀")
    st.markdown("Upload your resume to get job recommendations, skill gap analysis, and a personalized learning path!")

elif page == "Upload Resume":
    st.header("📄 Upload Your Resume")
    uploaded_file = st.file_uploader("Choose your resume (PDF)", type="pdf")

    if uploaded_file is not None:
        text = extract_text_from_pdf(uploaded_file)
        user_skills, user_experience = extract_skills_experience(text)

        st.subheader("Extracted Skills")
        st.write(user_skills)

        st.subheader("Extracted Experience")
        st.write(user_experience)

        job_matches = match_jobs(user_skills)
        missing_skills = identify_skill_gaps(user_skills)

        st.subheader("Job Matches")
        st.write(job_matches)

        st.subheader("Skill Gaps")
        st.write(missing_skills)

        user_name = st.text_input("Enter your name to save profile:")
        if st.button("Save Profile"):
            save_user_profile(user_name, user_skills, user_experience, job_matches, missing_skills)
            st.success("Profile saved successfully!")

elif page == "View Past Profiles":
    st.header("📊 Previous Analyses")
    profiles = fetch_profiles()
    for profile in profiles:
        st.write(f"**Name:** {profile[1]}")
        st.write(f"**Skills:** {profile[2]}")
        st.write(f"**Experience:** {profile[3]}")
        st.write(f"**Matches:** {profile[4]}")
        st.write(f"**Gaps:** {profile[5]}")
        st.markdown("---")
