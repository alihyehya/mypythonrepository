qa={
    "overview":"The Advanced Python Course is part of the AI Bootcamp roadmap for aspiring AI engineers.\n"
    "It condenses years of professional experience into a practical, structured learning path — helping you move from basic programming to building modern, useful Python applications",
    "prerequisites":"You should already be comfortable with Python basics, including syntax, functions, and data structures.\n"
    "Some familiarity with programming logic and problem-solving will help you get the most out of the course.",
    "topics":"The course covers:"
    "\n*Python Basics (professional coding foundations)"
    "\n*Database & GUI integration"
    "\n*AI Integration into systems"
    "\n*Security (password managers & encryption)"
    "\n*FastAPI services for robust APIs"
    "\n*File handling techniques",
    "projects":"You’ll complete a Capstone Project that brings together all skills learned — from Python fundamentals to AI integration, API development, and security — to create a comprehensive, real-world application.",
    "resources":"The course emphasizes structured Python practices, AI libraries, FastAPI, database connectors, GUI frameworks, and encryption tools.\n"
    "Official documentation, code examples, and hands-on practice form the core of the learning resources.",
    "schedule":"The course runs over 7 sessions, covering 6 topics, plus 1 final capstone project.\n"
    "The course sessions are held every saturday and sunday from 9:00 A.M to 11:00 A.M",
    "support":"Students can collaborate, share progress, and seek help via group discussions, Q&A support, and guided mentorship from the instructor\n"
    "Fostering a community of practice around advanced Python and AI development."
}
numToKeyword={
    "1":"overview",
    "2":"prerequisites",
    "3":"topics",
    "4":"projects",
    "5":"resources",
    "6":"schedule",
    "7":"support"
}
def check_num(a):
    if a.isnumeric():
        try:
           converted=numToKeyword[a]
        except KeyError:
           converted=a
        return converted
    else:
        return a
def generate_answer(a):
    try:
        return qa[a.lower()]
    except KeyError:
        return "Sorry I cannot help you with that"
def header():
    print("***************************************************")
    print("Welcome to Chatbot")
def main_menu():
    print("***************************************************")
    print("What do you want to know about:")
    print("1. **Overview:** What is the Advanced Python Course about? Provide a brief summary.")
    print("2. **Prerequisites:** What knowledge or skills should students have before starting the course?")
    print("3. **Topics:** What are the main topics covered in the course? (e.g., APIs, AI in python, security & encryption, etc.)")
    print("4. **Projects:** What kind of projects or assignments can students expect?")
    print("5. **Resources:** What materials or tools will be used or recommended during the course?")
    print("6. **Schedule:** How long is the course and what is the typical schedule?")
    print("7. **Support:** How can students get help and collaborate during the course?")
    print("***************************************************")
    a=input("Enter your answer (Number or Keyword) (Exit:-1): ")
    return a
def check_proceed():
    a=input("Do you have more questions? (Yes/No): ")
    if a.lower()=="yes":
        return True
    else:
        print ("See you Later!")
        return False






