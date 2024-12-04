# a program that will ask the year that we were born in, an then it will calculate our age and print it on the terminal
from datetime import date

year_birthday = input('Please Enter your Birth Year: ')
current_date = date.today().year
age = current_date - int(year_birthday)

print(type(age))
print("Your Age is: " + str(age))