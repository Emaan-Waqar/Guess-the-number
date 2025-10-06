import random
import string
random_num= random.random()
randomUppercase= random.choice(string.ascii_uppercase)
randomLowercase= random.choice(string.ascii_lowercase)
passwordCharacter= randomUppercase + randomLowercase
passwordNumbers= str(random_num)
finalPassword= passwordCharacter + passwordNumbers
print(f"Your password is {finalPassword}")