def ispolindrom(word = str):
    if str(word) == "".join(reversed(word)):
        print("Palindrome")
    else:
        print("Not Palindrome")

ispolindrom("dghhgd")