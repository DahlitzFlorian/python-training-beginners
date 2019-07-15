# This is a possible solution for exercise_06.py
import random

allowed_chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password_length = 8
password =  "".join(random.sample(allowed_chars, password_length))

print(password)
