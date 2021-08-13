#Step 2 and 3
import random

word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)

display = []

print()
for i in word:
    display.append('_')
    print('_', end=" ")

while '_' in display:
    print('\n')
    letter = input('Digite uma letra: ').lower()

    print('\n' * 30)

    for i in range(len(word)):
        if word[i] == letter:
            display.pop(i)
            display.insert(i, letter)

    if letter in word:
        print('certo')
    else:
        print('errado')

    print()
    for i in display:
        print(i, end=" ")

print('Você ganhou!')