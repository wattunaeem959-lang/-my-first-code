import random, string
length = int(input("Kitne char ka password? "))
chars = string.ascii_letters + string.digits + "!@#$%"
password = "".join(random.choice(chars) for _ in range(length))
print("Tera Password:", password)