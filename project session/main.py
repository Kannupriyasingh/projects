'''from datetime import datetime
odds = [25,2,36]
rigth = datetime.today().minute
left = datetime.today().hour
print(left)
print(rigth)
lefts = str(left)
rights = str(rigth)
if rigth < 10:
    print("time is " + lefts + ":0" + rights)
else:
    print("time is " + lefts + ":" + rights)
if rigth in odds:
    print("yes")
else:
    print("no")
'''
while True:
    a = input("write any message: ")
    if "lol" in a:
        print("\U0001F602")
    elif "hehe" in a:
        print("\U0001F92A")
    elif "shut up" in a:
        print("\U0001F92B")
    elif "shy" in a:
        print("\U0001F605")
    elif "love" in a:
        print("\U0001F60D")
