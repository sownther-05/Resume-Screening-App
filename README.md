# Resume Screening App

A web-based **Resume Screening System** designed to automate the process of reviewing resumes by matching keywords to the job description. Built using **Flask**, this application allows users to upload resumes in PDF or DOCX format and matches them against a job description to generate a score based on keyword relevance.

## Features

- **Upload Resumes**: Upload resumes in **PDF** or **DOCX** format for screening.
- **Job Description Matching**: Enter the job description and compare it with the resumes.
- **Keyword Matching**: Matches the content of the resumes with keywords from the job description.
- **Results Display**: Shows the percentage of match based on keyword relevance.

## Installation

To run this project locally, follow these steps:

### 1. Clone the repository


git clone https://github.com/sownther-05/Resume-Screening-App.git


### 2. Navigate to the project directory

Copy code
cd Resume-Screening-App

### 3. Create a virtual environment (optional but recommended)

Copy code
python3 -m venv venv

### 4. Activate the virtual environment

On Windows:
Copy code: venv\Scripts\activate

On Mac/Linux:
Copy code: source venv/bin/activate

### 5. Install the required dependencies

Copy code: pip install -r requirements.txt
__________________________________________

### Usage

### 1. Run the Flask application

Copy code:
python app.py

### 2. Open your web browser and navigate to:

Copy code: http://127.0.0.1:5000/

### 3. Upload a resume and enter a job description to see the keyword matching result.
Project Structure

Copy code
Resume-Screening-App/
├── app.py             # Main application file
├── requirements.txt   # List of dependencies
├── README.md          # Project documentation
├── templates/         
│   ├── index.html     # Home page template
│   ├── result.html    # Result page template
├── static/
│   ├── style.css      # CSS for styling
├── uploads/           # Directory to store uploaded resumes
└── .gitignore         # Git ignore file to exclude unnecessary files


### Technologies Used

Flask: Web framework for building the application.
PyPDF2: Library to extract text from PDF files.
python-docx: Library to extract text from DOCX files.
HTML/CSS: For structuring and styling the web pages.

### Contributing
Feel free to fork this project and submit pull requests. If you have any suggestions or issues, please open an issue in the GitHub repository.


### Output

![image](https://github.com/user-attachments/assets/ebe2fb13-caa5-471d-85c3-483b3e701993)

