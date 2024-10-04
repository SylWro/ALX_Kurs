def calc():
    try:
        num1 = float(input("Podaj pierwszą liczbę: "))
    except ValueError:
        num1 = float(input("Podaj poprawną pierwszą liczbę: "))

    try:
        num2 = float(input("Podaj drugą liczbę: "))
    except ValueError:
        num2 = float(input("Podaj poprawną drugą liczbę: "))

    while True:
        operation = input("Podaj znak działania (+ - * /): ").strip()
        if operation == "*" or operation == "/" or operation == "+" or operation == "-":
            if operation == "+":
                correct_answer = num1 + num2
            elif operation == "-":
                correct_answer = num1 - num2
            elif operation == "*":
                correct_answer = num1 * num2
            elif operation == "/":
                correct_answer = num1 / num2
            break

    try:
        users_answer = int(input(f"Ile to jest: {num1} {operation} {num2}? "))
    except ValueError:
        users_answer = int(input(f"Podaj wynik w formie liczby! Ile to jest: {num1} {operation} {num2}?"))
    while users_answer != correct_answer:
        try:
            users_answer = int(input(f"Sprobuj ponownie. Ile to jest: {num1} {operation} {num2} ? "))
        except ValueError:
            users_answer = int(input(f"Podaj wynik w formie liczby! Ile to jest: {num1} {operation} {num2}?"))
    print("Dobra odpowiedź!")


calc()