# Set the natural number N. Write a program, which will create a list, filled with prime factors of the number N.
# !!! It's comfortable to check the solution with 32, 9282 or/and 102102 input numbers !!!

n = int(input('Please input a natural number: '))

result = []
for i in range(1, 1 + n // 2):
    counter = 0
    if n % i == 0:
        for j in range(1, i+1):
            if i % j == 0:
                counter += 1
    if counter == 2:
        result.append(i)
print(f'List of prime factors of {n} is: {result}')