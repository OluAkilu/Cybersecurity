"""
Initial Purpose/Goal: take a given number of chars (8-32?) and return a (randomized) password
- Create function:
    - Takes parameter num_chars and returns of string of length num_chars
    - For each position in the string the given char is chosen at random
    (from an array containing certain characters or at complete random) using the chr() function
"""
import random
ascii_choices = [x for x in range(97, 122)] # adds lowercase alphabet

for x in range(65, 90):
    ascii_choices.append(x) # adds uppercase
    
for x in range(33, 57): # adds numbers (0-9) and special characters
    ascii_choices.append(x)

def create(num_chars):
    password = ""
    for x in range(num_chars):
        password += chr(random.choice(ascii_choices)) # this might be too slow, maybe create an array and store choosen items
    return password