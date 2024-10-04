def provide_non_repeating():
    answer = input("Podaj 10 liczb z zakresu 1-10: ")
    answer_strip = answer.strip("[, ]")
    answer_final = answer_strip.replace(",", "")
    answer_list = []
    first = set()
    repeated = set()
    for number in answer_final:
        answer_list.append(number)

    for num in answer_list:
        if num in first:
            repeated.add(num)
        else:
            first.add(num)
    result = first - repeated
    print(answer_list)
    print(result)

provide_non_repeating()