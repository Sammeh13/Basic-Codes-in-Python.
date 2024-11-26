#access list by using index
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Pluto"]
print("The first planet in the solar system is", planets[0])

#modify the list by using the index
planets[2] = "Mother Earth"
print("We also call our planet", planets[2])

#determining the length of the list
print("There are", len(planets), "planets in the solar system.")

#adding value to the list
planets.append("New Planet") #adds at the end of list
print("There are now", len(planets), "planets")

#adding value on specific position
planets.insert(0, "old planet")
print(planets)

#removing value of first occurrence
planets.remove("old planet") #removes first occurrence
print(planets)

#planets.pop(1) - specific position
planets.pop() #removes last value/item from the list
print("There are", len(planets), "planets")

#using negative index: -1 starts at the last item
print("The last planet is", planets[-1])

#finding value in a list
print("Mercury is the", planets.index("Mercury") + 1, "from the sun") # plus 1 since indexing starts at 0

#planets.clear() - removes all values

#numbers in list
planets_g = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.899, 1.12]
bus_weight = 124054 # in Newton, on Earth

print("On Earth, a bus weighs", bus_weight, "N")
print("On Mercury, a bus weighs", bus_weight * planets_g[0], "N")

#min() and max(): returns the smallest and largest value from the list
print("The lightest a bus would be in the solar system: ", bus_weight * min(planets_g), "N")
print("The heaviest a bus would be in the solar system: ", bus_weight * max(planets_g), "N")

#slice list - extract specific portion of a list; creates new list, does not modify the current list
print("The planets before Earth are", planets[0:2]) # index ends before the index ending -> Earth is excluded

print("The planets after Earth are", planets[3:]) # no stop index -> continue until the end of list

#join list: use (+) operator
amalthea = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean = ["Io", "Europa", "Ganymede", "Callisto"]

print(amalthea + galilean, "are the regular satellite moons of Jupiter") #creates new list; does not modify the current

#sort lists alphabetically
#print((amalthea + galilean).sort(), "are the regular moons") = ERROR -> result to str "None"

moon = amalthea + galilean
moon.sort() #case sensitive,
print(moon, "are the moons of Jupiter in alphabetical order")
#.sort(reverse=True) = reverse the order
#moon.sort(key=str.lower) -> arrange in order regardless of casing since str is converted to lower

#sample application on list
"""
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planet_name = input("Enter the name of the planet").title()
planet_index = planets.index(planet_name)
print("The planet", planet_name, "is", planet_index, "planets away from the sun")
print("Here are the planets closer than", planet_name)
print(planets[0:planet_index])
print("Here are the planets further than", planet_name)
print(planets[planet_index+1:])
"""

sample = ["dog", "cat", "bird", "cat", "snail", "chicken"]
print(sample)
print(sample.count("cat")) #number of occurrence


#slice [start included:end excluded]
print(sample[1:4])

print(len(sample)) #number of value in list

print(sample[len(sample)-1])
print(sample.count(sample[len(sample)-1]))
#arranging in descending order: x.sort() then x.reverse()

aa = [[1, 5, 6], [3, '', 4,'']] # list inside a list

#list and loops
MM = ["Sam", "Mish", "Lads", "Erics"]

for _ in MM:
    print(_)

#another method to print vals in list
for name in range(len(MM)): #gets the amount of vals in list
    print(MM[name])

for name in range(len(MM)):
    print(name + 1, MM[name])

















