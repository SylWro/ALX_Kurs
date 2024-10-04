def provide_odd():
    answer = int(input("Podaj dodatnią liczbę całkowitą"))
    odd_numbers = []
    if answer <= 0:
        print("Nieprawidłowa liczba.")
    elif answer == 1:
        print(answer)
    else:
        for n in range(1, answer + 1):
            if n % 2 != 0:
                odd_numbers.append(n)

        print(odd_numbers)

provide_odd()