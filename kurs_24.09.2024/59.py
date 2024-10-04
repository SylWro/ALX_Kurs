import random

number = random.randint(1,100)
print(number)
guess = int(input("Podaj liczbę: "))
counter = 1

while number != guess:
    if counter == 5:
        print(f"Przegrałeś, liczba to {number}.")
        break
    if guess < number:
        guess = int(input("Za mało, podaj większą liczbę: "))
    if guess > number:
        guess = int(input("Za dużo, podaj mniejszą liczbę: "))
    if guess == number:
        print("Wygrałeś")
    counter += 1

