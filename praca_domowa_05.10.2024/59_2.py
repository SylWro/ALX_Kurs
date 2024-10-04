from random import randint


def multiplication_training():
    for i in range(5):
        num1 = randint(1,10)
        num2 = randint(1,10)
        correct_answer = num1 * num2
        users_answer = int(input(f"Ile to jest: {num1} * {num2} ? "))
        while users_answer != correct_answer:
            users_answer = int(input(f"Ile to jest: {num1} * {num2} ? "))
        print("Dobra odpowiedź!")
    print("Koniec")


multiplication_training()

