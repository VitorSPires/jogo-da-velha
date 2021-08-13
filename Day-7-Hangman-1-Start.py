#Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)

letter = input('Digite uma letra: ').lower()

for i in word:
    if letter == i:
        print('certo')
    else:
        print('errado')