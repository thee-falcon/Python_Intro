case_single_quot = "Omar's Book"
case_double_quot = ' is "Awesome". '
print(case_single_quot + case_double_quot)

email_message = '''
Hello Omar,

Here is our first email to you.

Thank you,
The support team.
'''
print(email_message)

course = 'Python'

print("the first Character in course variable is => " + course[0] + " ,and the last Character is => " + course[-1])

print("Let's print multi Characters => " + course[0:3])

another = course[:]
print("Well copy all the Characters of variable course to the another Variable => " + another)

name = 'Omar'
print(name[1:-1])