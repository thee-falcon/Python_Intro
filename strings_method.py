course = "Python"

len_course = len(course)
print("lenght of this string is: " + str(len_course))

to_upper = course.upper()
print("Convert the string to Upper case: " + to_upper)

title = course.title()
print("Titlecased: " + title)

find_index = course.find('t')
print("Return index when it found: " + str(find_index))

replace = course.replace("P", "J")
print("Replace P with J: " + replace)

print('Python' in course)