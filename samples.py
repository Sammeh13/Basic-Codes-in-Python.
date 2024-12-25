#unit testing

'''''
a = 2
b = 2

print("start")

assert a==b, "This is an ERROR"
#will result to an AssertionError if it does not satisfy the condition

print("stop")

x = str(input("Enter money value: "))
print(x)

conversion_rate = 50

print(f"You're balance is: {conversion_rate * float(x.split("$")[-1])}")


while True:
    n = (input("What's n? ")).lower().strip()
    if n == "yes":
        print("ok")
        break
    elif n == "no":
        print("aww")
        break
    else:
        print("invalid entry")

'''''

a = ["a", "b", "c", "d", "e", "f", "g"]

print(len(a))

print(5%2)

import string
printables = list(string.printable)

#getting input from the user
userInput = input("Enter message: ")

#assigning number for the indexing
keyNumber = len(userInput)

#initializing variable
encryptedOutput = ""

#getting the total number of characters
maxNumber = len(printables)

#creating loop for encrypting
for characters in userInput:
    print(characters)









