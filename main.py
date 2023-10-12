# read words
f = open("words.txt", "r")
words = f.readlines()
f.close()
#define stuff
table = {}
nine_table = {}
score = 0
submissions= {}
response = " "
#get stuff i want
import random
import itertools
import os

#determine all possible words in dict, and 9 letter words in other dict
for i in range(len(words)):
    words[i] = words[i].strip()
    table[words[i]] = True
    if len(words[i]) == 9:
        nine_table[words[i]] = True

def randScramble(someTable):
    chosen_word = random.choice(list((someTable.keys())))
    randomLetters= "".join(random.sample(chosen_word, len(chosen_word)))
    return randomLetters

#solution time!!! find all combos
def generatePowerset(someString):
    combinations= []
    for i in range(1, len(someString)+1):
        for subset in itertools.permutations(someString, i):
            combinations.append("".join(subset))
    return combinations

def findRealWords(someList):
    realAnswers= {}
    for word in someList:
        if word in table:
            realAnswers[word] = True
    return realAnswers

def remainingAnswers(possible, submit):
    answer = []
    for key in possible:
        if key not in submit:
            answer.append(key)
    return answer

given = randScramble(nine_table)
solution = findRealWords(generatePowerset(given))

#start printing in terminal: display 9 random letters, input words
while True:
    os.system("clear")
    print("Make as many words as you can with the following:")
    print(given)
    print("When you're done, or give up, enter -1")
    print("Score:", score)
    print(response)
    x = input()
    x = x.lower().strip()
    if x == "-1":
        break
    if x not in solution:
        response = "Invalid word :("
    elif x in submissions:
        response = "Already attempted :("
    else:
        submissions[x] = True
        score += len(x)
        response = "Accepted :D"

os.system("clear")
if score > 9:
    print(f"Great job! Your final score is {score}!")
else:
    print(f"Better luck next time, your final score is {score}!")

print(f"The remaining words are: {remainingAnswers(solution, submissions)}")
print(f"The words you input are: {list(submissions.keys())}")

with open("leaderboard.txt", "r") as g:
    lines = g.readlines()
    # for i in range(len(lines)):
    #     lines[i] = lines [i].strip()
    top = []
    for line in lines:
        components = line.split(":")
        name = components[0]
        topscore = int(components[1])
        rec = {"name": name, "topscore": topscore}
        top.append(rec)
scoreboard = sorted(top, key=lambda x: x["topscore"], reverse = True)
if score >= scoreboard[-1]["topscore"]:
    name = input("OMG! Congrats, you made it on the leaderboard, please enter your name:")
    scoreboard[-1]["name"] = name
    scoreboard[-1]["topscore"] = score
    scoreboard = sorted(scoreboard, key=lambda x: x["topscore"], reverse=True)
    with open("leaderboard.txt", "w") as g:
        for thing in scoreboard:
            g.write(f"{thing['name']}: {thing['topscore']}\n")

with open("leaderboard.txt", "r") as h:
    lines = h.readlines()
    leaderboard = [line.strip() for line in lines]
    print("Leaderboard:")
    for i, line in enumerate(leaderboard):
        print(f"{i+1}. {line}")
