print('Capital cities of canadian provinces quiz')
print('Only use lowercase when typing answers')

play = input('Are you ready to begin? ("yes" to play)')

if play != 'yes':
    print('bye')
    quit()

print("Let's start -- please make sure all your answeres are in lower case")
score = 0
answerslist = []
row = []
answerKey = [['Ontario','toronto'],['Quebec','quebec city'],["Newfoundland","st john's"],['Nova Scotia','halifax'],['Yukon','whitehorse'],['Alberta','edmonton'],['Saskatchewan','regina'],['Manitoba','winnipeg'],['North West Territories','yellowknife'],['Prince Edward Island','charlottetown'],['British Columbia','victoria'], ['Nunavut','iqaluit']]

answer = input("What is the capital city of the province of Ontario?")
if answer == "toronto":
    print('Correct!')
    score += 1

else:
    print('Incorrect!')
    answerslist.append(answer)

answer = input("What is the capital city of the province of Quebec?")
if answer == "quebec city":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append(answer)

answer = input("What is the capital city of the province of Newfoundland?")
if answer == "st john's":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append(answer)

answer = input("What is the capital city of the province of Nova Scotia?")
if answer == "halifax":
    print('Correct')
    score += 1
else:
    print('Incorrect!')
    answerslist.append(answer)

answer = input("What is the capital city of the province of Yukon?")
if answer == "whitehorse":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append(answer)

answer = input("What is the capital city of the province of Alberta?")
if answer == "edmonton":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append(answer)

answer = input("What is the capital city of the province of Saskatchewan?")
if answer == "regina":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append(answer)

answer = input("What is the capital city of the province of Manitoba?")
if answer == "winnipeg":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append(answer)

answer = input("What is the capital city of the province of North West Terriroties?")
if answer == "yellowknife":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append(answer)

answer = input("What is the capital city of the province of Print Edward Island?")
if answer == "charlottetown":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append(answer)

answer = input("What is the capital city of the province of Nunavut?")
if answer == "iqaluit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append(answer)

answer = input("What is the capital city of the province of British Columbia?")
if answer == "victoria":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append(answer)

answer = input("What is the capital city of the province of New Brunswick?")
if answer == "fredericton":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    answerslist.append(answer)

# Calculate Score
percentage = score/13 * 100
print('The game is now over. Your score is:', percentage, '%')

replyList = input('Would you like to see a list of your incorrect answers? -- If yes, type "yes"')

if replyList != 'yes':
    quit()

print(answerslist)

# Answerkey and verification
replyKey = input('Would you like to see the answer key? -- If yes, type "yes"')

if replyKey == 'yes': 
    if percentage > 0.6:
        print(answerKey)
    else:
        print('Sorry, you need to pass by getting above 60 percent before viewing the answer key')

