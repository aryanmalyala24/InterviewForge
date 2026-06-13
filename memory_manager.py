import json
import os

MEMORY_FILE = "interview_memory.json"

if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump({"history": [], "strengths": [], "weaknesses": []}, f)

def save_to_memory(role, question, answer, feedback):
    with open(MEMORY_FILE, "r") as f:
        memory=json.load(f)
    
    memory["history"].append({
        "role": role,
        "question": question,
        "answer": answer,
        "feedback": feedback
    })

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def get_memory():
    with open(MEMORY_FILE, "r") as f:
        memory=json.load(f)
    return memory