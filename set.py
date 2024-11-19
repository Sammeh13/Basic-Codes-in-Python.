mySet = {1, 2, 3, 3, 4, 5, 4, 8, 9}
print(mySet) #unique values

#converting list to set
myList = [1, 2, 3, 3, 4, 5, 4, 8, 9]

print(myList)
print(set(myList)) #converts the list to set; no repeating element
print(list(set(myList))) #converts back to list;bracket

#list to set

xx = ["A", "B", "D", "E", "E", "Z"] #list
print(xx)
xx_set = set(xx) #converts list to set
print(xx_set)

#tuple to set
zz = ("A", "B", "D", "E", "E", "Z") #tuple
print(zz)
zz_set = set(zz) #converts tuple to set
print(zz_set)

setA = {1, 2, 3,}
setB = {2, 3, 4}

print(setA.union(setB))
print(setA | setB) #another method to write union

print(setA.intersection(setB))

print(setA.difference(setB))
print(setA - setB) #method for difference

print(setA.symmetric_difference(setB))
print(setA ^ setB ) #another method for symmetric diff



