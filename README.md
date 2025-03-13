🌟 Smart Resume Generator - Customized Resume For Every Opportunity
[🚀 View Repository on GitHub🔗](https://github.com/mallikamudraboina/Smart-Resume-Generator-Customized-Resume-For-Every-Opportunity-main)


📌 Project Overview
The Smart Resume Generator is a web application that allows users to generate professional resumes effortlessly. Users can enter their personal details, work experience, skills, education, and projects, and the system will generate a well-structured resume in PDF format using Google Gemini AI.

🛠 Features
✔️ Simple & user-friendly resume form
✔️ Dynamic sections for education, projects, and experience
✔️ Automatically formats the resume in a clean structure
✔️ Exports resume as a PDF
✔️ Uses Google Gemini AI for smart resume generation

📂 Folder Structure
php
Copy
Edit
smart-resume/
│── templates/
│   ├── index.html   # Resume input form
│── static/          # CSS & JS files (if needed)
│── app.py           # Main backend logic (Flask)
│── requirements.txt  # List of required dependencies
│── .gitignore       # To prevent sensitive files from being pushed
│── README.md        # Documentation (this file)
🚀 Installation Guide
🔹 Step 1: Clone the Repository
sh
Copy
Edit
git clone https://github.com/mallikamudraboina/Smart-Resume-Generator-Customized-Resume-For-Every-Opportunity-main.git
cd Smart-Resume-Generator-Customized-Resume-For-Every-Opportunity-main
🔹 Step 2: Create a Virtual Environment
sh
Copy
Edit
python -m venv venv
Activate it:

Windows (CMD): venv\Scripts\activate
Windows (PowerShell): venv\Scripts\Activate.ps1
Mac/Linux: source venv/bin/activate
🔹 Step 3: Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
🔹 Step 4: Configure Environment Variables (.env)
To use Google Gemini AI, you need an API key.

📌 How to Get a Google Gemini API Key?
Go to Google AI Platform
Navigate to API Keys → Click Create API Key
Copy the API Key
📌 Create a .env file and Add Your API Key
sh
Copy
Edit
GEMINI_API_KEY=your-api-key-here
▶️ How to Run the Project?
After setting up everything, start the Flask server:

sh
Copy
Edit
python app.py
Then, open http://127.0.0.1:5000/ in your browser.

📄 Sample Resume Output
When you enter your details, the system will generate a PDF resume like this:

yaml
Copy
Edit
MUDRABOINA MALLIKA
Email: malikasivarao@gmail.com | Phone: 8555986385
LinkedIn: https://www.linkedin.com/in/mallika-profile
GitHub: https://github.com/Mallika-Dev

Summary:
Enthusiastic entry-level software engineer with a strong background in Python and a passion for software development.

Skills:
✔ Python
✔ Web Development
✔ AI & Machine Learning

Experience:
✔ Software Developer, XYZ Company
✔ x Years of experience

Education:
✔ B.Tech in Computer Science, ABC University, 2023

Projects:
✔ Smart Resume Generator - An AI-powered resume builder
✔ AI Chatbot - A chatbot using NLP and ML

Certifications:
✔ Python for Data Science - Coursera
✔ AWS Cloud Practitioner - AWS
