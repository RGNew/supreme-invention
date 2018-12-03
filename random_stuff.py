import string
import random

alphabet = string.ascii_lowercase

#print(alphabet)

rand_val = random.randint(0,25)
#print(rand_val)

# letter = alphabet[rand_val]
# print(letter)

word_length = 5

sentence_word_count = 5

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

def random_sentence_gen(sentence_word_count=5):
    '''
    Returns a sentence of sentence_word_count composed of randomly generated words.
    It uses the random_word_gen function to generate words.
    '''

    sentence = ''

    for _ in range(sentence_word_count):  # for loop used to create the sentence by concatinating random words
        rand_word = random_word_gen()  # calls the random_word_gen function to generate random word
        sentence = sentence + ' ' + rand_word  # combines the randomly generated words into a sentence
    
    return sentence

#print(f'The word is {random_word_gen(word_length)}.')  # print out the full word
print(random_sentence_gen(sentence_word_count))  # prints the sentence to the console