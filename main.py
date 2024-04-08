# Imports
import random

# Global Variables
question_types = ["+", "-", "x", "/"]
pirate = False
correct_question = 0
attempt_counter = 0
question_history = []
# Methods / Functions

# Check_int() method
def check_int(question):
    while True:
        try:
            return float(input(question))
        except:
            if pirate:
                print("Enter a valid number ye scallywag")
            else:
                print("Enter a valid number")

# One_question() method
def one_question():
    global pirate
    global correct_question
    global attempt_counter
    first_number = random.randrange(1, 50)
    second_number = random.randrange(1, 50)
    question_type = random.choice(question_types)
    correct_answer = 0
    question = ""
    if pirate:
        question = "What be {} {} {} rounded to ye first decimal place?\n".format(first_number, question_type, second_number)

    else:
        question = "What is {} {} {} rounded to the first decimal place?\n".format(first_number, question_type, second_number)
    main = check_int(question)

    if question_type == "+":
        correct_answer = first_number + second_number
    elif question_type == "-":
        correct_answer = first_number - second_number
    elif question_type == "x":
        correct_answer = first_number * second_number
    elif question_type == "/":
        correct_answer = first_number / second_number
        correct_answer = round(correct_answer, 1)

    if pirate:
        if main == correct_answer:
            print("Correct, you clearly be having good plunders")
            correct_question += 1
            attempt_counter += 1
        elif main != correct_answer:
            print("Incorrect, the answer was {} ye ship is drowning".format(correct_answer))
            attempt_counter += 1
    else:
        if main == correct_answer:
            print("Correct, good job!")
            correct_question += 1
            attempt_counter += 1
        elif main != correct_answer:
            print("Incorrect, the answer was {} Try again next time...".format(correct_answer))
            attempt_counter += 1

    history = "{}Correct answer: {}, User answer: {}\n".format(question, correct_answer, main)
    question_history.append(history)


# Main Function

# Title for the code
print("--------------------")
print(" MATH QUESTIONNAIRE")
print("--------------------\n")

# Pirate mode code
pirate = (input("Would you like a pirate mode, Yes or No?\n").upper()) == "YES"
if pirate:
    print("--------------------------------------")
    print("ARRRRRR, Pirate mode be active ye hear?")

else:
    print("------------------------------")
    print("Pirate mode is not activated")

if pirate:
    username = input("What be yer name?\n").capitalize()
else:
    username = input("What is your name?\n").capitalize()

# Main Code for "Math Questionnaire

print("----------Math Questionnaire----------\n")
print("Hello {}, welcome to 'Math Questionnaire'".format(username))


while True:
    if pirate:
        game = input("Would ye like to play, Aye or Nay?\n").capitalize()
        if game == "Aye":
            print("\nGame starting...")
            break

        elif game == "Nay":
            print("Ye be a fool, may your ship sink in the big drink.")
            exit()

        else:
            print("Command an answer ye landlubber")
    else:
        game = input("Would you like to play, Yes or No?\n").capitalize()
        if game == "Yes":
            print("Game starting...")
            break

        elif game == "No":
            print("Goodbye... :(")
            exit()

        else:
            print("Type a proper answer")
round_count = 1
if pirate:
    round_count = int(input("How many stories would ye like?\n"))
    print("Ye selected {} stories, that be {} questions for ye\n".format(round_count, round_count))

else:
    round_count = int(input("How many questions would you like?\n"))
    print("The amount of questions you will be asked is {}".format(round_count))

for round_number in range(round_count):
    one_question()

print("\n--------------------")
print("MATH QUIZ EVALUATION")
print("--------------------")
print("\n--------------------------------------------------------")

percentage = round(correct_question / attempt_counter * 100, 1)

print("You got {} correct questions out of {} questions in total".format(correct_question, round_count))
print("With a percentage total of {}%".format(percentage))
print("----------------------------------------------------------")

print("\n------------------")
print("QUESTION HISTORY")
print("------------------\n")


for previous_question in question_history:
    print(previous_question)

if pirate:
    if correct_question < 5:
        print("\nScallywag behaviour, ye can do better next time!")

    elif correct_question >= 5:
        print("\nYe be worthy of a captain, keep it up sailor!")

else:
    if correct_question < 5:
        print("\nGood job, but you can do better!")

    elif correct_question >= 5:
        print("\nGood job, Smiley face sticker for you!")

