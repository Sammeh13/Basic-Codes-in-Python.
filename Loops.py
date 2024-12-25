x = 3
while x != 0:
    print("arf")
    x -= 1

y = 0
while y != 4:
    print("ho")
    y += 1

i = 0
while i < 3: # i<=3 would result to 4x
    print("ha")
    i += 1

for i in [0, 1, 2]: #not practical
    print("luh")

for _ in range (2):
    print("moew")


print("meeowe\n" * 2, end="") #removes extra new line at the end

print("---------------")
print("hhshshshshhs")

print("Before the loop")

for x in range(10, 0, -1):
    print("Code Block: " + str(x))

print("---------------")

for x in range(5, 15, 2):
    print("Code Block: " + str(x))

print("After the loop")

print("---------------")




''''
while True:
    aa = int(input("How many times should I bark? "))
    if aa < 0:
        continue
    else:
        break

for _ in range(aa):
    print("arf")
'''''

while True: #shortened ver of the code above
    nn = int(input("How many times should I meow? "))
    if nn > 0:
        break

for _ in range(nn):
    print("meowiee")


new_names = ''
sector_2 = []

while new_names.lower() != 'done':
    if new_names:
        sector_2.append(new_names)
    new_names = input('Enter your names or type done if done')

for i in sector_2:
    print(i)



print("-------------------NEW------------------------")

for x in range(9, 0, -1):
    print("x -> "  + str(x))

fruits = ["apple", "banana", "orange", "pineapple", "grapes"]

for i in fruits:
    print(f"I love {i}")
    for ii in range(3):
        print("codeblock: " + str(ii))


a = 0
while a != 5:
    print("HA" + str(a))
    a+=1

print("-------------------------")

b = 5
while b != -1:
    print("Ho" + str(b))
    b-=1

name = ["Sam", "Erics", "Lads", "Carly", "Mish", "Gela", "Geliks", "Tons", "Ems"]
c = 0
nn = ""

while nn != "Gela":
    print(name[c])
    nn = name[c]
    c += 1

print("///////////////////////")

c = 0
nn = ""

while nn != "Gela":
    if name[c] != "Gela":
        print(name[c])
    nn = name[c]
    c += 1

print("Start of first loop")
for m in range(7):
    print("Start of second loop")
    for n in range(3):
        print(f"Set m: {m} - set n: {n} ")
    print("Exit of second loop")
print("Exit of first loop")


print("---------------------------")

for p in range(4):
    for q in range(2):
        print(f"Set m: {p} - set n: {q} ")
        break


print("-------------------------")

for g in range(4):
    for h in range(2):
        print(f"Set m: {g} - set n: {h} ")
    break

print("----------------------")

for xy in range(10):
    print(xy)
    if xy % 3 == 0 and xy != 0:
        break





