def sentanceMaker(phrase):
    caps = phrase.capitalize()
    inter = ("how","what","why")
    
    if phrase.startswith(inter):
        return "{}?".format(caps)
    else:
        return "{}.".format(caps)

print(sentanceMaker("how are you")) 

userSays =[]

while True:
    userInput = input("Say somthing: ")
    if userInput == "end":
        break
    else:
        userSays.append(sentanceMaker(userInput))

print(" ".join(userSays))