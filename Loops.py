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

for _ in range (5):
    print("moew")


print("meeowe\n" * 2, end="") #removes extra new line at the end
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


new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet or done if done')

for planet in planets:
    print(planet)









