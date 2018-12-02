import string
import random

alphabet = string.ascii_lowercase

#print(alphabet)

rand_val = random.randint(0,25)
#print(rand_val)

# letter = alphabet[rand_val]
# print(letter)

word_length = 5

def random_word_gen(word_length=5):
    '''
    Returns a random word of word_length composed of letters of the alphabet.
    '''
    
    word = ''

    for _ in range(word_length):
        rand_val = random.randint(0,25)  # select a random int from 0 to 25
        letter = alphabet[rand_val]  # use previous random int to select letter
        word += letter  #  add each letter together into a string

    return word

print(f'The word is {random_word_gen(word_length)}.')  # print out the full word