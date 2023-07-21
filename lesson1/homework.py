def ispolindrom(word = str):
    if str(word) == "".join(reversed(word)):
        print(True)
    else:
        print(False)

ispolindrom("dghhgd")