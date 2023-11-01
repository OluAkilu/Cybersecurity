"""
Initial Purpose/Goal: 
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
class Encrypt:
    def __init__(self):
        self.__p_t_s = set() # private hashset that only holds the passwords stored
        self.__s_t_p = {} # private hashmap that holds key, value pairs of the scrambled keys and passwords {scrambled, password}
        
    def __add(self, key, value): # helper method to add a given key value pair to a given hashmap
        if key in self.__s_t_p:
            if value != self.__s_t_p[key]: 
                return "there is a problem with the hash function, same key yet different scramble"
        else:
            self.__s_t_p[key] = value

    def __store(self, key, value): # method to add passwords to hashset, the "add()" method here is the one for sets 
        if key in self.__p_t_s:
            return False
        else:
            self.__p_t_s.add(key)
        
    def scramble(self, password: str) -> str: # takes a string (ENFORCE TYPE CHECKING, python does not do it)
        scrambled = hash(password) # scrambles given string
        if self.__store(password, scrambled) != False: # stores the password with its scrambled version as a value
            self.__add(scrambled, password) # stores the scrambled password with its original self as a value
        else:
            print('It looks like that password already exists. Try another!')
            return None
        print(f"Here's your encrypted key: {scrambled}. Make sure to write it down!")
    
    def unscramble(self):
        key = int(input("Please enter in your scrambled: "))
        if key in self.__s_t_p:
            print(f"Here is your password: {self.__s_t_p[key]}, be sure not to tell anyone.")
        else:
            return "Sorry, this scramble is not recognized."
    '''
    def unscramble(self, scrambled: int): # first iteration of scramble method
        if scrambled not in scramble_to_password:
            return "The given scramble is not accounted for."
        else:
            return scramble_to_password[scrambled]


    def get(self): # unnecessary method, used to test  code
        return self.__p_t_s, self.__s_t_p
    '''
    
x = Encrypt()
x.scramble('1234')