# Import the basic libraries
import json
import random
import string
import os

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
random_names = json.loads(open('random_names.json').read())
random_domains = json.loads(open('random_domains.json').read())

for name in random_names:
    random_email = name.lower() + str(random.randint(2, 99)) + random.choice(random_domains)
    passw_lenght = random.randint(6, 15)
    random_passw = "".join(random.choice(chars) for i in range(passw_lenght))
    print('E-mail: %s and Password: %s' % (random_email, random_passw))
