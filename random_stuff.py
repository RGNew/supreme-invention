import string
import random

alphabet = string.ascii_lowercase

#print(alphabet)

rand_val = random.randint(0,25)
#print(rand_val)

# letter = alphabet[rand_val]
# print(letter)

word_length = 5

for i in range(word_length):
     rand_val = random.randint(0,25)  # select a random int from 0 to 25
     letter = alphabet[rand_val]  # use previous random int to select letter
     print(letter, end='')  # print the letter with no newline