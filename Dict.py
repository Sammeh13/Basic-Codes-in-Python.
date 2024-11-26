#'di ko gets 'tong part na 'to potah
data = {"Name": "Sam", "Address": "Mnl", "Age": 18, "Student": True}
print(data["Name"])

info = (({"Name": "Soph", "Address": "Laguna", "Age": 19, "Student": True},
        {"Name": "Sam", "Address": "Mnl", "Age": 18, "Student": True}),
        {"Name": "Kades", "Address": "Maribel", "Age": 5, "Student": False})

print(info[1]["Name"])

#dict and loops
names = {
        "Peppa": "Pig",
        "Mickey": "Mouse",
        "Hello": "Kitty",
        "Winnie": "the Poohtah",
}

for i in names:
        print(i, names[i], sep=', ')


#reading dict vals
print(names.get("Peppa"))

profile = {
        "name": "Sam",
        "age": "18",
        "gender": "F",
        "address": "Binan City"
}

print(profile.get("name"))

#another method using [] to get keys of name
print(profile["name"])

# Unavailable key: .get -> returns None, [] -> raises KeyError

#modify dict vals
profile.update({"name": "Sammeh",
                "address": "Muntinlupa City"})
print(profile["name"])

#another method to  modify vals using []
profile["name"] = "Samuu"
print(profile["name"])

#.update - modify multiple vals in one operation, [] - two calls to the func

# add and remove keys
profile["hobbies"] = "sports"
profile["alma matter"] = "MunSci"

print("--------------------------")

for ii in profile:
        print(ii, profile[ii], sep=" - ")

print("--------------------------")

profile.pop("alma matter")

for ii in profile:
        print(ii, profile[ii], sep=" - ")

print("--------------------------")

#complex data types

profile["favs"] = {
        "fav movie": "The Book of life",
        "fav tv series": "Big Bang Theory",
        "fav book": "Everyday by David Levithan"
}
print(profile["favs"])

for ii in profile:
        print(ii, profile[ii], sep=" - ")

print(f"{profile["name"]} fav book: {profile["favs"]["fav book"]}")

print("-------------------------")

planet = {
    "name": "Mars",
    "moons": 2
}

print(f'{planet["name"]} has {planet["moons"]} moon(s)')

planet["circumference (km)"] = {
    "polar": 6752,
    "equatorial": 6792
}

print(f'The polar circumference of planet {planet["name"]} is {planet["circumference (km)"]["polar"]}')

#Tanginahh

#Retrieve keys and vals

plant_growth = {
        "day 1": 1,
        "day 2": 1.5,
        "day 3": 1,
        "day 4": 0.5
}

for g in plant_growth:
        print(g, plant_growth[g], sep=" - ")

for gg in plant_growth.keys():
        print(f"{gg}: {plant_growth[gg]} cm")

total = 0
for _ in plant_growth.values():
        total += _

print(f"There was a total of {total}cm growth of the plant in a span of 4 days.")

print("------------------------------")

planet_moons = {
    "Mercury": 0,
    "Venus": 0,
    "Earth": 1,
    "Mars": 2,
    "Jupiter": 79,
    "Saturn": 82,
    "Uranus": 27,
    "Neptune": 14,
    "Pluto": 5,
    "Haumea": 2,
    "Makemake": 1,
    "Erics": 1
}

moons = planet_moons.values()
total_planets = len(planet_moons.keys())

total_moons = 0
for i in moons:
    total_moons += i

average = total_moons / total_planets

print(f"The average of moon in our solar system is {average}")


