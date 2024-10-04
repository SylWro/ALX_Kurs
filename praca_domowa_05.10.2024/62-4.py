def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


def sort_given_numbers():
    list_of_numbers = []
    answer = int(input("Podaj dowolną liczbę całkowitą: "))
    while answer != 0:
        list_of_numbers.append(answer)
        answer = int(input("Podaj dowolną liczbę całkowitą: "))
    sorted_list = bubble_sort(list_of_numbers)
    print(f"Posortowane liczby: {sorted_list}")


sort_given_numbers()
