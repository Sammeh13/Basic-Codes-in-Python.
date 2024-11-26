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







