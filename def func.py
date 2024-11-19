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


