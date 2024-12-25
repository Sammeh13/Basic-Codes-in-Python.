import string

#converting str of letters to list
alphabet = (list(string.ascii_letters))

#printing out
print(alphabet)

#Encryption

#Getting input from the user
number = 16
userInput = input("Input the message you want to encrypt: ")

encryptedOutput = ""

#Getting total number of charac
maxNumber = len(alphabet)
# print(maxNumber)


#Printing out each character and getting the index
for charac in userInput:
    #prints the charac
   # print(charac)
    #prints the index of charac
   # print(alphabet.index(charac))
    #modifies the index of charac (encryption)
    indexEncryptChar = alphabet.index(charac) + number
    if indexEncryptChar > 51:
        indexEncryptChar -= 52
    encryptChar = alphabet[indexEncryptChar]
   # print(encryptChar)

    encryptedOutput += encryptChar

print("Input message: " + userInput)
print("Encyrpted output is: " + encryptedOutput)






#Decryption







