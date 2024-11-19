#conditional statements

x = 4
while x != 0:
    print("meow", end="")
    x = x - 1

for i in range(4):
    print("HA")

print("luh\n" * 2)

xx = input("Name: ").lower()
if xx == "lebron":
    print("amazing player")

else:
    print("aww not amazing")


score = int(input("What is you grade? "))

if score >= 90:
    print("purrfect")

elif score >= 80:
    print("slay")

elif score >= 70:
    print("awts gege")

else:
    print("oh no")

if score % 2 == 0:
    print("Your score is an even number")

else:
    print("Your score is an odd number")