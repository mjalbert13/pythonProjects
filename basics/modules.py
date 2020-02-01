import time
import os
import pandas

while True:
    if os.path.exists("files/temps-today.csv"):
        data = pandas.read_csv("files/temps-today.csv")
        print(data.mean())
    else:
        print("file does not exist")
    time.sleep(10)