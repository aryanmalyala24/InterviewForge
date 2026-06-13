INTERVIEW_ROLES = {
    "software_engineer": {
        "keywords": ["oop", "dsa", "data structures", "algorithms", "operating", "networks"],
        "difficulty": "hard"
    },
    "data_analyst": {
        "keywords": ["sql", "excel", "statistics", "python", "visualization"],
        "difficulty": "medium"
    },
    "web_developer": {
        "keywords": ["html", "css", "javascript", "react", "api"],
        "difficulty": "medium"
    },
    "app_developer": {
        "keywords": ["android", "ios", "flutter", "firebase", "api"],
        "difficulty": "medium"
    },
    "cybersecurity_analyst": {
        "keywords": ["cybersecurity", "networking", "linux", "owasp", "cryptography"],
        "difficulty": "hard"
    },
    "cloud_engineer": {
        "keywords": ["aws", "docker", "kubernetes", "networking", "ci", "cd"],
        "difficulty": "hard"
    },
    "full_stack_developer": {
        "keywords": ["frontend", "backend", "databases", "api", "cloud"],
        "difficulty": "hard"
    },
    "data_scientist": {
        "keywords": ["python", "statistics", "machine learning", "sql", "analytics"],
        "difficulty": "hard"
    },
    "ai_engineer": {
        "keywords": ["llm", "rag", "ai agents", "prompt", "mlops"],
        "difficulty": "godlevel"
    },
    "database_engineer": {
        "keywords": ["sql", "database", "design", "indexing", "transactions", "nosql"],
        "difficulty": "medium"
    }
}


def choose_role():
    print("\nwelcome to the AI Interview Coach")
    print("Please choose a role from the following options:")

    roles=list(INTERVIEW_ROLES.keys())

    for i, r in enumerate(roles, start=1):
        print(f"{i}. {r.title()}")
    
    choice = int(input("Enter the number corresponding to your choice: "))
    role = roles[choice - 1]

    print(f"\nYou have chosen the role: {role.title()}")
    return role, INTERVIEW_ROLES[role]