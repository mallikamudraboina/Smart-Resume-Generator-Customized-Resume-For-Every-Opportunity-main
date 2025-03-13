from flask import Flask, render_template, request, send_file
import pdfkit
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API Key not found! Make sure it's in the .env file.")

# Configure Google Gemini AI
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-pro-latest")

app = Flask(__name__)

def generate_resume(name, email, phone, linkedin, github, summary, exp_type, experience, job_role, company, skills, education, projects, certifications):
    """Generates a structured resume in HTML format."""
    
    education_html = "".join(f"<li>{deg}, {uni} - {year}</li>" for deg, uni, year in zip(education['degree'], education['university'], education['grad_year']))
    projects_html = "".join(f"<li><b>{name}:</b> {desc}</li>" for name, desc in zip(projects['name'], projects['desc']))
    certifications_html = "".join(f"<li>{cert}</li>" for cert in certifications)

    experience_html = ""
    if exp_type == "experienced":
        experience_html = f"""
        <div class="section-title">Experience</div>
        <div class="content">
            <b>{job_role}</b> at <b>{company}</b><br>
            {experience} years of experience
        </div>
        """

    resume_html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; padding: 20px; line-height: 1.6; }}
            .header {{ text-align: center; font-size: 24px; font-weight: bold; text-transform: uppercase; }}
            .contact {{ text-align: center; font-size: 14px; }}
            .section-title {{ font-size: 18px; font-weight: bold; margin-top: 20px; border-bottom: 2px solid black; }}
            .content {{ font-size: 14px; margin-bottom: 10px; }}
            ul {{ list-style-type: square; margin-left: 20px; }}
        </style>
    </head>
    <body>
        <div class="header">{name.upper()}</div>
        <div class="contact">
            <b>Email:</b> {email} | <b>Phone:</b> {phone} <br>
            <b>LinkedIn:</b> <a href="{linkedin}">{linkedin}</a> | <b>GitHub:</b> <a href="{github}">{github}</a>
        </div>

        <div class="section-title">Summary</div>
        <div class="content">{summary}</div>

        <div class="section-title">Skills</div>
        <div class="content">{skills}</div>

        {experience_html}

        <div class="section-title">Education</div>
        <ul>{education_html}</ul>

        <div class="section-title">Projects</div>
        <ul>{projects_html}</ul>

        <div class="section-title">Certifications & Achievements</div>
        <ul>{certifications_html}</ul>
    </body>
    </html>
    """

    return resume_html

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        education_data = {
            "degree": request.form.getlist("degree"),
            "university": request.form.getlist("university"),
            "grad_year": request.form.getlist("grad_year")
        }

        projects_data = {
            "name": request.form.getlist("project_name"),
            "desc": request.form.getlist("project_desc")
        }

        certifications = request.form.getlist("certifications")

        exp_type = request.form.get("exp_type")
        experience = request.form.get("experience") if exp_type == "experienced" else None
        job_role = request.form.get("job_role") if exp_type == "experienced" else None
        company = request.form.get("company") if exp_type == "experienced" else None

        resume_html = generate_resume(
            request.form.get("name"), request.form.get("email"), request.form.get("phone"),
            request.form.get("linkedin"), request.form.get("github"), request.form.get("summary"),
            exp_type, experience, job_role, company, request.form.get("skills"),
            education_data, projects_data, certifications
        )

        pdf_file = "resume.pdf"
        pdfkit.from_string(resume_html, pdf_file, options={"enable-local-file-access": ""})
        return send_file(pdf_file, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
