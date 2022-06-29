questions = [
    "Who is the developer of python language?",
    "When did India get independence?",
    "What is the currency of India?",
    "Which state does Banglore belong to?",
    "Which is the latest IPhone?"
]
answers = [
    "Guido Van",
    "1947",
    "INR",
    "Karnataka",
    "IPhone 12"
]
options = [
    ["Dennis Ritchie", "Alan Frank", "Guido Van", "Albert"],
    ["1947", "1995", "2000", "1950"],
    ["Pounds", "Dollars", "Euros", "INR"],
    ["Karnataka", "Rajasthan", "West Bengal", "Assam"],
    ["IPhone SE", "IPhone 13", "IPhone 11", "IPhone 12"]
]
def playgame(username, questions, answers, options):
    print("Hello",username)
    print("Welcome to the KBC game.")
    score = 0
    for i in range(len(questions)):
        current_question = questions[i]
        correct_answer = answers[i]
        current_question_options = options[i]
        print("Question : ", current_question)
        for index, each_options in enumerate(current_question_options):
            print(index + 1,") ",each_options, sep="")
        user_answer_index = int(input("Enter your choice (1, 2, 3 or 4):"))
        user_answer = current_question_options[user_answer_index - 1]
        if user_answer == correct_answer:
            print("Correct answer")
            score = score + 100
        else:
            print("Wrong answer")
            break
    print("Your final score is:", score)
    return username, score


def viewscores(names_and_scores):
    for names, scores in names_and_scores.items():
        print(names,"has scored", scores, "points")




def KBC(questions, answers, options):
    names_and_scores = {}
    while True:
        print("Welcome to the KBC game!")
        print("1. Play Game\n2. View Scores\n3. Exit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            username = input("Enter your name:")
            username, score = playgame(username, questions, answers, options)
            names_and_scores[username] = score
        elif choice == 2:
            viewscores(names_and_scores)
        elif choice == 3:
            break
        else:
            print("Your choice selection is not valid.")
KBC(questions, answers, options)
