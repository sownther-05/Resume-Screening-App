from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
import docx
import PyPDF2
import re

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'docx'}

# Job role and keywords mapping
job_roles_keywords = {
    'Software Developer': [
        'python', 'java', 'c++', 'react', 'javascript', 'html', 'css', 'node.js', 'express', 
        'angular', 'sql', 'git', 'typescript', 'ruby', 'api', 'spring', 'django', 'mysql', 'mongodb', 
        'restful', 'vue.js', 'flask', 'web development', 'frontend', 'backend', 'full-stack', 
        'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'typescript', 'graphql', 'microservices', 'html5', 
        'css3', 'redux', 'typescript', 'firebase', 'redux-saga', 'npm', 'webpack', 'babel', 'sass', 'bootstrap'
    ],
    'Data Scientist': [
        'python', 'machine learning', 'pandas', 'data analysis', 'numpy', 'scikit-learn', 'tensorflow', 
        'keras', 'deep learning', 'sql', 'big data', 'statistics', 'data wrangling', 'data mining', 
        'data visualization', 'matplotlib', 'seaborn', 'jupyter', 'r', 'spark', 'hadoop', 'ai', 'predictive modeling',
        'python pandas', 'r studio', 'h2o', 'tableau', 'd3.js', 'bigquery', 'data pipelines', 'tensorflow.js', 
        'nlp', 'apache kafka', 'azure machine learning', 'cloud computing', 'data engineering', 'etl', 
        'docker', 'data architecture', 'model deployment', 'big data analytics', 'aws', 'azure', 'gcp'
    ],
    'System Administrator': [
        'linux', 'windows', 'networking', 'server', 'bash', 'shell scripting', 'cloud', 'aws', 'docker', 
        'kubernetes', 'system monitoring', 'firewall', 'vpn', 'ldap', 'ssh', 'tcp/ip', 'virtualization', 'redhat', 
        'ubuntu', 'unix', 'server management', 'backup solutions', 'automation', 'docker', 'ci/cd', 'iptables', 
        'hyper-v', 'puppet', 'ansible', 'saltstack', 'oracle', 'cloudformation', 'server provisioning', 'syslog', 
        'cloud security', 'active directory', 'server hardening', 'amazon s3', 'gcp', 'azure', 'containers', 
        'aws lambda', 'devops', 'load balancing'
    ],
    'DevOps Engineer': [
        'docker', 'kubernetes', 'jenkins', 'cloud', 'aws', 'azure', 'gcp', 'terraform', 'git', 'ci/cd', 
        'infrastructure as code', 'devops', 'containerization', 'scripting', 'automation', 'ansible', 'chef', 'puppet', 
        'monitoring', 'logging', 'cloud infrastructure', 'microservices', 'deployment pipelines', 'devops tools',
        'vault', 'kafka', 'prometheus', 'grafana', 'splunk', 'gitlab', 'ci/cd pipelines', 'nginx', 'apache', 'cloudwatch',
        'elastic load balancing', 'nginx', 'cloudformation', 'cloud networking', 'web services', 'docker swarm', 
        'continuous integration', 'container orchestration', 'serverless architecture', 'k8s', 'azure devops'
    ],
    'Data Analyst': [
        'excel', 'data visualization', 'sql', 'python', 'pandas', 'power bi', 'tableau', 'data analysis', 
        'r', 'statistical analysis', 'data cleaning', 'data mining', 'reporting', 'data manipulation', 
        'business intelligence', 'machine learning', 'sql queries', 'data warehousing', 'sas', 'google analytics',
        'predictive analysis', 'data governance', 'data modeling', 'etl', 'data quality', 'kpi', 'd3.js', 'bi tools', 
        'big data', 'business analytics', 'data pipelines', 'forecasting', 'hadoop', 'data integration', 'apache hadoop',
        'bigquery', 'data segmentation', 'web analytics', 'excel macros', 'data scraping', 'data integrity', 
        'quantitative analysis', 'spreadsheets', 'cloud analytics', 'cloud platforms', 'etl pipelines', 'analytics'
    ],
    'Business Analyst': [
        'business analysis', 'requirements gathering', 'project management', 'agile', 'scrum', 'stakeholder management', 
        'data analysis', 'product management', 'business process', 'use cases', 'system analysis', 'market research', 
        'budgeting', 'change management', 'lean', 'SWOT analysis', 'user stories', 'business intelligence', 
        'gap analysis', 'uatt testing', 'functional specifications', 'business modeling', 'stakeholder engagement',
        'requirements documentation', 'project lifecycle', 'risk management', 'financial analysis', 'strategic planning',
        'business cases', 'workflow analysis', 'sprint planning', 'sales forecasting', 'competitive analysis', 'branding',
        'customer journey', 'process improvement', 'process mapping', 'CRM', 'business solutions', 'erp systems', 
        'ux/ui', 'cross-functional teams', 'presentations', 'product design', 'customer relationship management',
        'business process modeling', 'lean six sigma'
    ]
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
        return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = ''
    for para in doc.paragraphs:
        text += para.text
    return text

# Normalize the resume text by removing unnecessary characters
def normalize_text(text):
    # Remove non-alphabetic characters except spaces and normalize to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return 'No file part'
    
    file = request.files['resume']
    if file.filename == '':
        return 'No selected file'
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Extract text from the file
        if filename.endswith('.txt'):
            resume_text = extract_text_from_txt(file_path)
        elif filename.endswith('.pdf'):
            resume_text = extract_text_from_pdf(file_path)
        elif filename.endswith('.docx'):
            resume_text = extract_text_from_docx(file_path)

        # Normalize text to improve matching
        resume_text = normalize_text(resume_text)
        
        job_role = request.form['job_role']
        keywords = job_roles_keywords.get(job_role, [])
        
        # Matched skills
        matched_skills = [keyword for keyword in keywords if keyword in resume_text]
        
        # Calculate score based on matched skills
        total_keywords = len(keywords)  # Total number of required skills
        matched_count = len(matched_skills)  # Number of matched skills
        
        # Avoid division by zero if no keywords are defined
        if total_keywords > 0:
            final_score = (matched_count / total_keywords) * 100
        else:
            final_score = 0

        final_score = int(round(final_score))  # Convert to an integer after rounding
        
        # Create feedback message
        message = f"Your resume score for the {job_role} role is {final_score}/100. "
        if final_score < 50:
            message += "Your resume score is low, consider updating it."
        else:
            message += "Your resume looks good for this role!"
        
        return render_template('result.html', message=message, matched_skills=matched_skills)
    
    return 'Invalid file type. Please upload a .txt, .pdf, or .docx file.'


if __name__ == '__main__':
    app.run(debug=True)
