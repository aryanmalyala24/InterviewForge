from roles import INTERVIEW_ROLES
import google.generativeai as genai

def strengths_of_user(user_skills, role):
    keywords = INTERVIEW_ROLES[role]["keywords"]
    STRENGTHS = []
    for k in user_skills.lower().split(","):
        if(k in keywords):
            STRENGTHS.append(k)
    return STRENGTHS

def show_weaknesses(strengths, role):
    keywords = INTERVIEW_ROLES[role]["keywords"]
    WEAKNESSES = []
    for k in keywords:
        if(k not in strengths):
            WEAKNESSES.append(k)
    return WEAKNESSES


def ask_questions(role, strengths, weaknesses):
    model = genai.GenerativeModel("models/gemini-2.0-pro")
    prompt = f"""
    You are an experienced interviewer.
    Generate exactly 3 interview questions for the role of {role.title()}.
    Candidate strengths: {', '.join(strengths)}
    Candidate weaknesses: {', '.join(weaknesses)}
    Focus more on the weak areas while still assessing the strengths. Do not provide answers.
    if the Candidate has no strengths ask little bit easier questions, if the Candidate has no weaknesses ask little bit harder questions,
    else ask a mix of easy, medium, and hard questions.
    at the end of each question put a .
    Don't use . in the middle of the question, only at the end."""

    response = model.generate_content(prompt)
    questions = response.text.strip().split(".")
    for(i, q) in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q.strip()}.")
        answer = input("Your answer: ")
        feedback = generate_feedback_for_answer(role, q.strip(), answer)
        print(feedback)
        if(i != len(questions)):
            print("\nMoving to the next question:\n")

def generate_feedback_for_answer(role, question, answer):
    model = genai.GenerativeModel("models/gemini-2.0-pro")
    prompt = prompt = prompt = f"""
    You are an interviewer for a {role.replace('_', ' ')} position.

    Question: {question}
    Answer: {answer}

    Evaluate the answer and return:
    - Score (0-10)
    - Strengths
    - Weaknesses
    - Suggested improvement

    Be concise and constructive.
    Don't provide a detailed explanation, just the evaluation points mentioned above.
    Not too harsh, not too lenient, be fair and honest in your evaluation.
    """

    response = model.generate_content(prompt)
    return response.text