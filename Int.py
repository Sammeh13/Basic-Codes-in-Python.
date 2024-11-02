#operators in Python

#round down/floor division
seconds = 1042
display_minutes = seconds // 60

#remainder -> modulo operator
display_seconds = seconds % 60

print(f'The time is {display_minutes} minutes and {display_seconds} seconds')

#absollute value
print("Absolute value of 4-7 = ", abs(4-7))


#rounding rule
print("rounding up and down: ")
print(round(3.4))
print(round(3.5))

#math lib
print("round up and down")
from math import ceil, floor
print(ceil(7.5))
print(floor(7.5))






