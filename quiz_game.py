print("Welcome To My Computer Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is the capital of Bangladesh? ")
if answer.lower() == "dhaka":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the founder of Microsoft? ")
if answer.lower() == "bill gatesyes":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is H2O commonly known as? ")
if answer.lower() == "water":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does MHS stand for? ")
if answer.lower() == "mehedi hasan shihab":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")