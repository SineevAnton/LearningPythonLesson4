# Create a number sequence.
# Write a program which will output a list of non-repeating elements of the original sequence.

from random import randint as rnd

originalList = [rnd(0, 10) for _ in range(10)]
print(f'Original sequence is: {originalList}')
nonRepeatingElements = []
for el in originalList:
    if originalList.count(el) == 1:
        nonRepeatingElements.append(el)
print(f'Non-repeating elements: {nonRepeatingElements}')