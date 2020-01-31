def mean(myList):
    if type(myList) == dict:
        the_mean = sum(myList.values()) / len(myList)
        return the_mean
    else:
        the_mean = sum(myList) / len(myList)
        return the_mean


studentGrages = {"bill": 10, "joe": 7, "will": 9.5}

def weather(temp):
    if temp > 32:
        return "warm"
    else:
        return "cold"
userInput = float(input("Enter temp: "))
# print(weather(userInput))

name = input("Enter your name: ")
message = f"Hello {name}"
print(message)