from random import randint


def math_training():
    wrong = 0
    for i in range(10):
        num1 = randint(1,10)
        num2 = randint(1,10)
        operations_list = ["+", "-", "*"]
        operation = operations_list[randint(0, 2)]

        if operation == "+":
            correct_answer = num1 + num2
        elif operation == "-":
            correct_answer = num1 - num2
        elif operation == "*":
            correct_answer = num1 * num2

        users_answer = int(input(f"Ile to jest: {num1} {operation} {num2} ? "))
        if users_answer != correct_answer:
            wrong += 1

        while users_answer != correct_answer:
            users_answer = int(input(f"Ile to jest: {num1} {operation} {num2} ? "))
        print("Dobra odpowiedź!")

    right = 10 - wrong
    print(f"Koniec. Dobre odpowiedzi: {right}, złe odpowiedzi: {wrong}.")


math_training()

