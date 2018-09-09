"# Use of Directories It is like Map"
students = {"nakul": 20, "dhrumil": 20, "bhautik": 22}
print(students["nakul"])
"# Update the value in dictionaries #"
students["nakul"] = 21
print(students["nakul"])
"# Delete the value in dictionaries #"
del students["dhrumil"]
print(students)
"# Length of dictionaries In this it is 2#"
print(len(students))
"# clear everything in dictionaries #"
students.clear()
del students
students = {"nakul": 20, "dhrumil": 20, "bhautik": 22}
"# To get all the keys of dictionaries #"
print(students.keys())
"# To get all the values of dictionaries #"
print(students.values())
"# Add values of two dictionaries #"
students1 = {"elon": 50, "jeff": 40, "mark": 60}
students.update(students1)
print(students)
