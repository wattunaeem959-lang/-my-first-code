import random

secret = random.randint(1, 20)
print("Maine 1 se 20 tak ek number socha hai!")

for chance in range(3):
    guess = int(input("Tera guess: "))
    if guess == secret:
        print("WOW! Sahi jawab! Tu jeet gaya!")
        break
    elif guess > secret:
        print("Thoda chhota soch")
    else:
        print("Thoda bada soch")
else:
    print("Khatam! Number tha:", secret)