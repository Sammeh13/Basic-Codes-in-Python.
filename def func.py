# def func and loops
def main():
    number = get_number()
    laugh(number)

def get_number():
    while True:
        n = int(input("How many times should I laugh? "))
        if n > 0:
            return n #breaks the loop and return the val

def laugh(n):
    for _ in range(n):
        print("ha")

main()


print("------------------------")

def distance(destination):
    if destination == "Moon":
        return "12345"
    else:
        return "Unable to compute"

planet_distance = distance("Mars")

print(planet_distance)

def days(distance, speed):
    hours = distance/speed
    return hours/24

data = round(days(238855, 75))


print(data)


print("-------------------")

def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank}
    """
    print(output)


generate_report(80, 70, 75)



