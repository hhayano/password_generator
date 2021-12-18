#!/usr/bin/env python3

import random
import string

character_pool = ""
character_pool += string.ascii_lowercase
character_pool += string.ascii_uppercase
character_pool += string.digits
character_pool += string.punctuation
# character_pool += "_&-#@"
password_length = 16

lowercase_letter = random.choice(string.ascii_lowercase)
uppercase_letter = random.choice(string.ascii_uppercase)
digit = random.choice(string.digits) 
punctuation = random.choice(string.punctuation)

password_requirements = lowercase_letter + uppercase_letter + digit + punctuation
random_string = "".join(random.choice(character_pool) for x in range(password_length - len(password_requirements)))
password = password_requirements + random_string

# shuffle the requirement characters to a random part of the string
list_of_password_characters = list(password)
random.shuffle(list_of_password_characters)
shuffled_password = "".join(list_of_password_characters)

print(shuffled_password)
