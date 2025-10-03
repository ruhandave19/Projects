import string
import random
import secrets
import time
start_time = time.perf_counter()
s = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(30))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in s for c in password)):
        break
print(password)
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")