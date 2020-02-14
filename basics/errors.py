def func(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "You are deviding by zero"

print(func(1,0))
