from roles import INTERVIEW_ROLES
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.0-pro")

def strengths_of_user(user_skills, role):
    keywords = INTERVIEW_ROLES[role]["keywords"]
    STRENGTHS = []
    for k in user_skills.lower().split(","):
        if(k in keywords):
            STRENGTHS.append(k)
    with open("strengths.json", "w") as f:
        json.dump({"strengths": STRENGTHS}, f, indent=4)
    return STRENGTHS

def weaknesses_of_user(strengths, role):
    keywords = INTERVIEW_ROLES[role]["keywords"]
    WEAKNESSES = []
    for k in keywords:
        if(k not in strengths):
            WEAKNESSES.append(k)
    with open("weaknesses.json", "w") as f:
        json.dump({"weaknesses": WEAKNESSES}, f, indent=4)
    return WEAKNESSES


def ask_questions(role, strengths, weaknesses):
    prompt = f"""
    You are an experienced interviewer.
    Generate exactly 3 interview questions for the role of {role.title()} 
    topics to cover in the questions should be based on the keywords associated with the role: {', '.join(INTERVIEW_ROLES[role]['keywords'])}.
    Candidate strengths: {', '.join(strengths)}
    Candidate weaknesses: {', '.join(weaknesses)}
    Focus more on the weak areas while still assessing the strengths. Do not provide answers.
    if the Candidate has no strengths ask little bit easier questions, if the Candidate has no weaknesses ask little bit harder questions,
    else ask a mix of easy, medium, and hard questions.
    at the end of each question put a .
    Don't use . in the middle of the question, only at the end.(IMPORTANT)
    try to cover all the topics in the keywords across the 3 questions."""

    response = model.generate_content(prompt)
    questions = response.text.strip().split(".")
    for(i, q) in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q.strip()}.")
        answer = input("Your answer: ")
        feedback = generate_feedback_for_answer(role, q.strip(), answer)
        print(feedback)
        if(i != len(questions)):
            print("\nMoving to the next question:\n")
        else:
            print("\nThank you for answering all the questions. The interview is now moving to the evaluation stage.\n")

def generate_feedback_for_answer(role, question, answer):
    prompt = f"""
    You are an experienced interviewer evaluating a candidate for the role of {role.replace('_', ' ')}.

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

    prompt = f"""
    this is the response from the model: {response.text.strip()}
    now give the rating just in the format of 0-10, don't provide any explanation or anything else, just the rating.
    """

    resp= model.generate_content(prompt)
    with open("answer_rating.json", "w") as f:
        json.dump({"rating": resp.text.strip()}, f, indent=4)

    return response.text.strip()

def evaluate_candidate(role, strengths, weaknesses):
    prompt = f"""
    You are an experienced interviewer evaluating a candidate for the role of {role.replace('_', ' ')}.
    Strengths: {', '.join(strengths)}
    Weaknesses: {', '.join(weaknesses)}
    Based on the interview, evaluate the candidate and return:

    Score: <0-10>
    Strengths:
    Areas for Improvement:
    Interviewer Feedback:
    """

    response = model.generate_content(prompt)
    return response.text