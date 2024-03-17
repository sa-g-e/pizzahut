import random

def generate_number():
    while True:
        number = random.randint(1000, 9999)
        if number % 3 == 0:
            return str(2) + str(number + 1)

print(generate_number())
            



