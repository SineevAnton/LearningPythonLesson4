# The natural degree of K is set.
# Create randomly the list of coefficients (values from 0 to 100) of polynomial and write the polynomial K-degree in the file.
# Example:
# k = 2 => 2 * x2 + 4 * x + 5 = 0 or x2 + 5 = 0 or 10 * x2 = 0
from random import randint as rnd

k = int(input('Please enter a k-degree: '))
signs = ['+', '-']
coefficients = []
for _ in range(k + 1):
    coefficients.append(rnd(0,10))
result = ''
for i in range(k, 0, -1):
    if i == 1:
        result += f'{coefficients[i]}*x^{i} {signs[rnd(0,1)]} {coefficients[0]} = 0'
    else:
        if coefficients[i] != 0:
            result += f'{coefficients[i]}*x^{i} {signs[rnd(0,1)]} '
with open('polynoms.txt', 'a') as file:
    file.write(result + "\n")
print(result)