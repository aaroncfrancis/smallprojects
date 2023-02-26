print('Capital cities of canadian provinces quiz')

play = input('Are you ready to begin?')

if play != 'yes':
    print('bye')
    quit()

print("Let's start - make sure all your answeres are in lower case")
score = 0
answerslist = ()

answer = input("What is the capital city of the province of Ontario?")
if answer == "toronto":
    print('Correct!')
    score += 1

else:
    print('Incorrect!')
    answerslist.append('Ontario', answer, '**The correct answer is: toronto')

answer = input("What is the capital city of the province of Quebec?")
if answer == "quebec city":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append('Quebec', answer, '**The correct answer is: quebec city')

answer = input("What is the capital city of the province of Newfoundland?")
if answer == "st john's":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append('NEwfoundland', answer, "**The correct answer is: st john's")

answer = input("What is the capital city of the province of Nova Scotia?")
if answer == "halifax":
    print('Correct')
    score += 1
else:
    print('Incorrect!')
    answerslist.append('Nova Scotia', answer, '**The correct answer is: halifax')

answer = input("What is the capital city of the province of Yukon?")
if answer == "whitehorse":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append('Yukon', answer, '**The correct answer is: whitehorse')

answer = input("What is the capital city of the province of Alberta?")
if answer == "edmonton":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append('Alberta', answer, '**The correct answer is: edmonton')

answer = input("What is the capital city of the province of Saskatchewan?")
if answer == "regina":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append('Saskatchewan', answer, '**The correct answer is: regina')

answer = input("What is the capital city of the province of Manitoba?")
if answer == "winnipeg":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append('Manitoba', answer, '**The correct answer is: winnipeg')

answer = input("What is the capital city of the province of North West Terriroties?")
if answer == "yellowknife":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append('North West Territories', answer, '**The correct answer is: yellowknife')

answer = input("What is the capital city of the province of Print Edward Island?")
if answer == "charlottetown":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append('Prince Edward Island', answer, '**The correct answer is: charlottetown')

answer = input("What is the capital city of the province of Nunavut?")
if answer == "iqaluit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append('Nunavut', answer, '**The correct answer is: iqaluit')

answer = input("What is the capital city of the province of British Columbia?")
if answer == "victoria":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append('British Columbia', answer, '**The correct answer is: victoria')

answer = input("What is the capital city of the province of New Brunswick?")
if answer == "fredericton":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append('New Brunswick', answer, '**The correct answer is: Fredericton')

# Calculate Score
percentage = score/13 * 100
print('The game is now over. Your score is:', percentage, '%')

reply = input('Would you like to see a list of your answers as well as the answer key?')
