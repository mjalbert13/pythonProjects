import os
import collections

iran = open("trump.txt",'r')


def speach(text):
    li =list(text.split(" "))
    counter = collections.Counter(li)
    print(counter.most_common())

speach(iran.read().lower())