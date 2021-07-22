# My class
class Question:
     def __init__(self, userinput, answer):
          self.userinput = userinput
          self.answer = answer

#My list
question_prompts = [
    "\n In Back to the Future, what year does Marty McFly travel back in time to? \n (a) 1945 \n (b) 1950 \n (c) 1955 \n (d) 1960 \n" "\n Select One: ",
    "\n What is the name of the villainous teddy bear in Toy Story 3? \n (a) Hugs-A-Lot \n (b) Paddy \n (c) Lotso \n (d) Fitz-O \n" "\n Select One: ",
    "\n In Tangled, what is Flynn Rider's real name? \n (a) Eugene Fitzherbert \n (b) Herbert Barney \n (c) Melvin Orvillert \n (d) Morris Mortimer \n" "\n Select One: ",
    "\n In Black Panther, T'Challa, Okoye, and Nakia travel to which country in search of vibranium being sold on the black market? \n (a) Japon \n (b) Brazil \n (c) South Korea \n (d) England \n" "\n Select One: ",
    "\n In Forrest Gump, which Oscar-winning actor played Forrest's mom? \n (a) Sally Field \n (b) Jane Fonda \n (c) Meryl Streep \n (d) Diane Keaton \n" "\n Select One: ",
]

#My Object
questions = [
     Question(question_prompts[0], "c"),
     Question(question_prompts[1], "c"),
     Question(question_prompts[2], "a"),
     Question(question_prompts[3], "c"),
     Question(question_prompts[3], "a"),
]

def run_quiz(questions):
     print(" \n Hello, welcome to my baby quiz! \n")
     score = 0
     for question in questions:
          answer = input(question.userinput)
          if answer == question.answer:
               score += 1
          else:
               score += 0
     print("you got", score, "out of", len(questions))

run_quiz(questions)

