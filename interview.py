from roles import choose_role
from tools import strengths_of_user, ask_questions, weaknesses_of_user

def run_interview():
    print("\n==============WELCOME TO THE INTERVIEW==============\n")
    role, role_info = choose_role()
    user_skills = input("\nEnter your skills (comma separated): ")
    strengths = strengths_of_user(user_skills, role)
    weaknesses = weaknesses_of_user(strengths, role)
    ask_questions(role, strengths, weaknesses)
    