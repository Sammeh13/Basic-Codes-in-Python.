#capitalizations
x = "sam mae de jesus".title()
print(x)

print("sam mae de jesus".upper())
print("sam mae de jesus".lower())

print("------------------------------")

#double and single quotations
print("They said, \"Oh naur\"")

#indentation
print("\towemgee")

print("------------------------------")

#split a str; opp: .join()
temp = "Morning: 260 F \n Night: -280 F"

print("BUG".join(temp.split(" ")))

#another method for the code above
print(temp.replace(" ", "BUG"))

print(temp.split())

print(temp.split('\n'))

print("------------------------------")

#search for a str
print("Samantha" in "Sam Mae De Jesus")
print("Sam" in "Sam Mae De Jesus")

print("------------------------------")

#position of the str
name = "My full legal name is Samantha May Ablay De Jesus"
print(name.find("Sophie")) #return -1 if not found

print(name.find("May"))

print("------------------------------")

#returns the value of number occurrences of a str
nn = "My nickname includes: Sam Sam, Sam, Butam, Butamtam, Sami"
print(nn.count("Sam"))
print(nn.count("SM"))

print("------------------------------")

#position/check for content in str
temperature = "Average temperature in Mars: -60 C".split(':')
print(temperature[-1])

age = "I will be 19 years old next year on May 21"
for _ in age.split():
    if _.isnumeric():
        print(_)
# underscore can be changed to any label(e.g., part, x, y)
# .isdecimal() - checks for str that looks like decimals

print("------------------------------")

#extra validations on str
print("-60".startswith('-'))

if "30 C".endswith('C'):
    print("The given is in Celsius")

print("Samantha May Ablay De Jesus".replace("Ablay", "A."))

print("------------------------------")

# % formatting
#x = int(input("How old are you? "))
x = 5
print("You are %s years old" % x)

print("The first child is %s, the second born child is %s, and the third is %s. " % ("SM", "Sam", "Eman"))

# .format() method
print("you are {} years old".format(x))

y = 4
print("you are {0}, and she is {1}, and he is {0} too ".format(y,x))

#f-strings - no need to assign variable beforehand
print(f"you are {x} years old")

print(f"my favorite number is {round(1.2*3, 1)}")

print("-----------------------")

xxyy = "PUP let me out"
print(len(xxyy))
print(xxyy[2:6:2]) #[start, end, interval]





