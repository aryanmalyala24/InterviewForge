# InterviewForge

An AI powered interview preparation platform that conducts adaptive technical interviews, evaluates candidate responses, and provides personalized feedback using the Gemini API.

## Features

- Conducts role specific technical interviews across multiple software domains
- Analyzes candidate strengths and weaknesses from interview responses
- Generates adaptive interview questions based on candidate performance
- Provides real time feedback, ratings, and improvement suggestions
- Maintains interview history and performance records using JSON based memory management
- Simulates a realistic interview experience with dynamic question flow

## Tech Stack

- Python
- Gemini API
- JSON
- dotenv

## Project Structure

```
InterviewForge/
│── app.py
│── interview.py
│── tools.py
│── roles.py
│── memory_manager.py
│── gemini_client.py
│── interview_memory.json
│── .env
│── requirements.txt
└── README.md
```

## Workflow

1. Select a target software role.
2. The AI begins a technical interview tailored to that role.
3. Candidate responses are analyzed for strengths and weaknesses.
4. Follow up questions are generated dynamically based on previous answers.
5. The platform provides ratings, detailed feedback, and improvement suggestions.
6. Interview history is stored for future evaluations.

## Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/InterviewForge.git
cd InterviewForge
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application

```bash
python app.py
```

## Future Improvements

- User authentication
- Database integration (SQLite/PostgreSQL)
- Web interface using FastAPI and React
- Progress dashboard with interview analytics
- Support for code execution and evaluation
- Resume based interview generation

## Demo

Add screenshots or a short demo video here.

## License

This project is for educational and learning purposes.
