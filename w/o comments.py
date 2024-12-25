#TRIAL AND ERROR SAMPLE

import string
import time

#converting str of printable to list
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
    #modifying the index
    newIndex = printables.index(characters) + keyNumber
    #solving 'index out of range' error
    if newIndex > 297 :
        newIndex -= 300
    elif newIndex > 198:
        newIndex -= 200
    elif newIndex > 99:
        newIndex -= 100

    #using the modified index to form the encrypted message
    newChar = printables[newIndex]

    #adding str value to the variable
    encryptedOutput += newChar

#printing out
print(f'Your message \'{userInput}\' will be encrypted...')

#creating loop for countdown
for _ in range(3, 0, -1):
    print(_)
    time.sleep(1)

#printing out
print("Encrypted message: " + encryptedOutput)

#decryption

#initializing variable
decryptedOutput = ""

#creating loop for decrypting
for characs in encryptedOutput:
    #getting the old index
    oldIndex = (printables.index(characs) - keyNumber) % maxNumber

    #forming the message using the old index
    decryptedChar = printables[oldIndex]

    #adding str value to the variable
    decryptedOutput += decryptedChar

#creating loop to ask for user input
while True:
    user2ndInput = input("Do you want to decrypt the message? ").lower().strip()
    if user2ndInput == "yes":
        print(f"Decrypted message: {decryptedOutput}")
        break
    elif user2ndInput == "no":
        print("The message will not be decrypted. ")
        break
    else:
        print("Invalid entry, type 'yes' or 'no' only. ")
        continue


'''''
#getting user input; using lower and strip to convert to lowerstring and remove space, respectively
userInput2nd = input("Type 'yes' if you want to decrypt the message. ").lower().strip()

#using conditional to display decrypted message
if userInput2nd != "yes":
    print("Message will not be decrypted")
else:
    print("Decrypted message: " + decryptedOutput)
'''