import random

random_number = random.randint(1, 99)
max_attempt = 5


for attemp in range(1, max_attempt + 1):
    guess_number = int(input(f"Guess a number from 1 to 99: "))
    
    if guess_number == random_number:
        print(f"Selamat! Tebakan Anda benar yaitu angka {guess_number}")
    elif guess_number > random_number:
        print("Terlalu besar!")
    else:
        print("Terlalu kecil!")
else:
    print(f"Sayang sekali, kesempatan habis! Angka yang benar adalah {random_number}.")