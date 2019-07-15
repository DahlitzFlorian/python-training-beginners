# This is a possible solution for exercise_09.py
lower_bound = 5
upper_bound = 20

number = int(input("Enter a number: "))

result = "" if lower_bound <= number <= upper_bound else "NOT"
print(f"Your number is {result} between {lower_bound} and {upper_bound}")
