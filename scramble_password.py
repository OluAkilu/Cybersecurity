"""
Purpose/Goal: 
- Scrambler:
    - take a given STRING password (limit of up to 8 chars?)
    - scramble it (in the sense that each char is changed)
    - store the scrambled password and the unscrambled password to be accessed later (return)
- Unscrambler:
    - take a scrambled password
    - return the unscrambled version
    
- Use:
    - Hashmap: stores given passwords and their scrambled versions as well as the opposite (so 2 hashmaps)
    - Hash function: scrambles given password based on w.e
"""
password_to_scramble = {} # pass key, scrambled value
scramble_to_password = {} # scrambled key, pass value
v = 1
def add(key, value, hmap): # helper method to add a given key value pair to a given hashmap
    if key in hmap:
        if value != hmap[key]:
            return "there is a problem with the hash function, same key yet different scramble"
    else:
        hmap[key] = value

def scramble(password: str) -> str: # takes a string (ENFORCE TYPE CHECKING, python does not do it)
    scrambled = hash(password) # scrambles given string
    add(password, scrambled, password_to_scramble) # stores the password with its scrambled version as a value
    add(scrambled, password, scramble_to_password) # stores the scrambled password with its original self as a value
    return f"scrambled ! here's your encrypted key: {scrambled}"

def unscramble(scrambled: int):
    if scrambled not in scramble_to_password:
        return "given scramble is not accounted for"
    else:
        return scramble_to_password[scrambled]
    
    
    
    
