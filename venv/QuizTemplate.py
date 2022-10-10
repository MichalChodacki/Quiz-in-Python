def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------")
        print(key)
        for i in answers[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D)").upper()
        guesses.append(guess)
        print("correct answer is: " + str(questions.get(key)))
        correct_guesses += check_answer(questions.get(key), guess)
        question_num +=1
    display_score(correct_guesses,guesses)
#------------------------------
def check_answer(answer,guess):

    if answer == guess:
        print("correct!")
        return 1
    else:
        print("Wrong!")
        return 0

#------------------------------
def display_score(correct_guesses,guesses):
    print("---------------------")
    print("Results:")
    print("---------------------")
    print("Answers: ", end="")

    for i in questions:
        print(questions.get(i),end=" ")
    print()

    print("Guesses: ",end="")
    for i in guesses:
        print(i,end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("The score is: "+str(score)+"%")
#------------------------------
def play_again():
    response = input("Wanna try again? (Y/N): ").upper()

    if response == "Y":
        return True
    else:
        return False

#------------------------------

questions = {
    #here you can add/remove questions
    "Who created Python":"A",
    "What year was python created?":"B",
    "To which group is Python tributed":"C",
    "Which programming language is the most frequently used for machine learning?":"D"
}

answers = [
    #type in answers in order
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Jeff Bezos"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2004"],
    ["A. Friends", "B. Lonely Island", "C. Monthy Python", "D. The two old chumps"],
    ["A. Java", "B. Java Script", "C. C++", "D. Python"]
    ]

new_game()

while play_again():
    new_game()

print("See Ya!")