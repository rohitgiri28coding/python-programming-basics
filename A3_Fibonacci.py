# 0, 1, 1, 2, 3, 5, 8
print('Fibonacci Series')
while True:
    no_of_elements = int(input('Enter number of elements: '))
    if no_of_elements >= 0:
        break
    else:
        print('Enter a valid number of elements')
if no_of_elements == 0:
    print('0')
elif no_of_elements == 1:
    print('0\n1')
else:
    print('0\n1')
    first_element = 0
    second_element = 1
    while (no_of_elements-2) >= 0:
        print(first_element+second_element)
        second_element = first_element + second_element
        first_element = second_element - first_element
        no_of_elements -= 1
# M2
no_of_terms = int(input("Enter the number of terms to print the Fibonacci sequence: "))

if no_of_terms <= 0:
    print("Enter a valid number of terms to get a valid result!")
elif no_of_terms == 1:
    print(0)
else:
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < no_of_terms:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    print("The Fibonacci sequence:")
    print(*fibonacci_sequence, sep=",")


