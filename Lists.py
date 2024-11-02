#access list by using index
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Pluto"]
print("The first planet in the solar system is", planets[0])

#modify the list by using the index
planets[2] = "Mother Earth"
print("We also call our planet", planets[2])

#determining the length of the list
print("There are", len(planets), "planets in the solar system.")

#adding value to the list
planets.append("New Planet")
print("There are now", len(planets), "planets")

#using negative index
print("The last planet is", planets[-1])

#removing the last value/item from the list
planets.pop()
print("There are", len(planets), "planets again")

#using negative index: -1 starts at the last item
print("The last planet is", planets[-1])

#finding value in a list
print("Mercury is the", planets.index("Mercury") + 1, "from the sun") # plus 1 since indexing starts at 0

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

#sort lists






