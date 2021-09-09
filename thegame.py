import sys

print ("----------------------------------------------------------------")
Username = input("Please choose a username. ")
print("----------------------------------------------------------------")
print("Welcome to my game " + Username + " I hope you will enjoy your experience. ")
start = input("Please type R to start or N to end the game. ")
print("----------------------------------------------------------------")

if start == "N":
  print("Game ended successfully.")
  sys.exit()

if start == "R":
    choose1 = input("You wake up in a strange city with weird looking people do you (approche) them or (wait?) ")
if choose1 == "wait":
    print("you died of starvation. ")
    sys.exit()
if choose1 == "approche":
    print("The people are very kind and get you food and shelter.")
    choose2 = input("The people ask where you are from do you (answer) or do you (lie?) ")
if choose2 == "lie":
    print("The people can sens when u lie and they kill you instanly. ")
    sys.exit()
if choose2 == "answer":
    choose3 = input("The people ask for your name do you (tell them) or (lie) to them? ")
if choose3 == "lie":
    print("The people can sens when u lie and they kill you instanly. ")
    sys.exit()
if choose3 == "tell them":
    print("They tell you that you have pretty name. ")
    choose3 = input("Do you (ask) their name or (not?) ")
if choose3 == "not":
    print("They find you mean and kill you. ")
    sys.exit()
if choose3 == "ask":
    print("They tell you their name. ")
    choose4 = input("They ask if you need a help finding where you came from. ")
if choose4 == "no":
    print("They get angry you don't want their help and kill you. ")
    sys.exit()
if choose4 == "yes":
    print("They take you to a place where you can stay will they get some stuff ready. ")
    choose4 = input("Do you (stay) or try to (runaway.) ")
if choose4 == "runaway":
    print("You died of starvation. ")
    sys.exit()
if choose4 == "stay":
    print("They come back with a device that can help you get your memory back. ")
    choose4 = input("Do use the device or not? ")
if choose4 == "no":
    print("They get angry you waste there time and kill you. ")
    sys.exit()
if choose4 == "yes":
    print("They are happy you will use the device. ")
    choose5 = input("Does the device help you get your memory back. ")
if choose5 == "no":
    print("They get angry you waste there time and kill you. ")
    sys.exit()
if choose5 == "yes":
    print("They are happy there invention worked.")
    choose6 = input("They ask if you need any help getting back to where you are from. ")
if choose6 == "no":
    print("They leave you alone and you died of starvation. ")
    sys.exit()
if choose6 == "yes":
    print("They say they will leave in one week. ")
    choose7 = input("They ask if you want a tour of there city? ")
if choose7 == "no":
    print("They seem angry and leave alone to let you died. ")
    sys.exit()
if choose7 == "yes":
    print("They get happy and excited that you have interested in there city. ")
    choose8 = input("after the tour they ask if you want to go eat one of there specialty. ")
if choose8 == "no":
    print("they get mad they leave you alone and you will died of starvation. ")
    sys.exit()
if choose8 == "yes":
    print("They get happy and treat you to the best food, after the food they tell you they leave tomrrow at 8:00. ")
    choose9 = input("Do you wake up on time. ")
if choose9 == "no":
    print("They leave with out you. ")
    sys.exit()
if choose9 == "yes":
    print("They take you to the place you come from. ")
    choose10 = input("They ask if you remember the city. ")
if choose10 == "no":
    print("They get mad and leave you there to died.")
    sys.exit()
if choose10 == "yes":
    print("They are happy for you and wise you a great rest of your week and leave you there. ")

print("----------------------------------------------------------------")
print("Congratulations you beat my game. ")
print("I hope you a fun time playing my game. ")
print("I hope to see you next time " + Username )
print("----------------------------------------------------------------")
sys.exit()