# This is a possible solution for exercise_04.py
word = input("Enter a word (possible palindrom): ")
reversed_word = word[::-1]

if word == reversed_word:
    print("Your submitted word is a palindrom.")
else:
    print("Your submitted word is not a palindrom.")
