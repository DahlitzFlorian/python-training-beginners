# This is a possible solution for exercise_01.py
import datetime


def get_year_100(age):
    current_year = datetime.datetime.now().year
    had_birthday = input("Did you already have birthday (y/n): ")
    additional_year = 0 if had_birthday == "y" else 1
    year_of_birth = current_year - age - additional_year

    return year_of_birth + 100


name = input("What is your name: ")
age = int(input("How old are you: "))
year = get_year_100(age)

print(f"Hello {name}! You'll turn 100 in {year}.")
