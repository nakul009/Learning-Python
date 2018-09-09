'# This File contains some of List Functions and its implementation #'

shoppingList = "milk,eggs,oreo,oil,vegetables"
print(shoppingList)
'# This is not a list just a variable #'
shoppingList1 = ["milk", "eggs", "oreo", "oil", "vegetables"]
print(shoppingList1[0])
shoppingList1 = ["milk", "eggs", "oreo", "oil", "vegetables"]
shoppingList1[4] = "Kitkat"
print(shoppingList1)
del shoppingList1[4]
"# it wil deleat 4 th element of array #"
array = [20, 30, 40, 50, 60]
array2 = [10, 20, 30, 40, 50]
array3 = array+array2
'# Array is added to array1 and stored in array3 #'
print(array3)
print(len(array3))
numberArray = [90, 500, 30485, 78903]
print(max(numberArray))
print(min(numberArray))
shoppingList1.append("waffers")
print(shoppingList1)
shoppingList1.append("kitkat")
print(shoppingList1)
shoppingList1.append("kitkat")
print(shoppingList1)
print(shoppingList1.count("kitkat"))
