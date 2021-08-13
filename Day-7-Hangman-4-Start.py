#Step 4
import random
import draw
import logo
import words

print(logo.logo[0])

word_list = words.word_list

word = random.choice(word_list)
#word = word_list[0]

display = []

print()
for i in word:
    display.append('_')
    print('_', end=" ")

lives = 6


while '_' in display and lives > 0:
    print('\n')
    letter = input('Digite uma letra: ').lower()

    print('\n' * 30)

    for i in range(len(word)):
        if word[i] == letter:
            display.pop(i)
            display.insert(i, letter)

    if letter in word:
        print(draw.stages[lives])
    else:
        lives -= 1
        print(draw.stages[lives])

    for i in display:
        print(i, end=" ")

if lives != 0:
    print('\n\nParabens, você acertou!')
else:
    print('\n\nVocê perdeu')

input()