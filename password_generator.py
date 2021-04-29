#!/usr/bin/env python3

import random
import string

character_pool = ""
character_pool += string.ascii_letters
character_pool += string.digits
character_pool += string.punctuation
# character_pool += "_&-#@"
password_length = 12
# password_length = 16

password = "".join(random.choice(character_pool) for x in range(password_length))

print(password)
