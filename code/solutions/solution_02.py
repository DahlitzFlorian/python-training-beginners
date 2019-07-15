# This is a possible solution for exercise_02.py

# Explanation: In line 7 the variable state gets assigned a string
# based on the evaluation result of 'number % 2'.
# If the number is odd, then 'number % 2' is 1, hence True.
# If the number is even, then 'number % 2' is 0, hence False.
# 0 = False, all other numbers = True

number = int(input("Enter a number: "))
state = "odd" if number % 2 else "even"

print(f"The number you entered is {state}.")
