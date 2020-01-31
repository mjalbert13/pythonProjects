def mean(myList):
    if type(myList) == dict:
        the_mean = sum(myList.values()) / len(myList)
        return the_mean
    else:
        the_mean = sum(myList) / len(myList)
        return the_mean


studentGrages = {"bill": 10, "joe": 7, "will": 9.5}
print(mean(studentGrages))