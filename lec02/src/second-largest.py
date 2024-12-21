#!/usr/bin/env python

def find_second_largest(numbers):
    if len(numbers) < 2:
        return "non ci sono abbastanza numeri nella lista"

    largest = -1
    second_largest = -1

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest != -1:
        return second_largest
    else:
        return "non c'è un secondo numero più grande"

numbers = [30,20,30,30,30,30]
second_largest = find_second_largest(numbers)
print("Numeri: ", numbers)
print("Secondo numero più grande: ",second_largest)
