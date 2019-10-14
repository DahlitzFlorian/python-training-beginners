# This is a possible solution for exercise_02.py

# Explanation: In line 7 the variable state gets assigned a string
# based on the evaluation result of 'number & 1'.
# If the number is odd, then 'number &1' is True.
# If the number is even, then 'number & 1' is False.
# ANDing with 1 is useful for large numbers

number = int(input("Enter a number: "))
state = "odd" if number & 1 else "even"

print(f"The number you entered is {state}.")
