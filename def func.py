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

#keyword arguments - must be defined in the function themselves

from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H %M")

print("-----------------")

print(arrival_time())
print(arrival_time(hours=0))

#variable arguments

def seq_time(*args):
    total_mins = sum(args)
    if total_mins < 60:
        return f"Total time to launch is {total_mins} minutes."
    else:
        return f"Total time to launch is {total_mins/60} minutes."

print(seq_time(4, 14, 18))
print(seq_time(4, 14, 48))






