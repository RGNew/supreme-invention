import string
import random

alphabet = string.ascii_lowercase  # creates string from all lowercase letters

rand_val = random.randint(0,25)  # generates a random number from 0 to 25

def random_word_gen():
    '''
    Returns a random word of word_length composed of letters of the alphabet.
    '''

    word = ''
    word_length = random.randint(1,10)

    for _ in range(word_length):
        rand_val = random.randint(0,25)  # select a random int from 0 to 25
        letter = alphabet[rand_val]  # use previous random int to select letter
        word += letter  #  add each letter together into a string

    return word

def random_sentence_gen():
    '''
    Returns a sentence of sentence_word_count composed of randomly generated words.
    It uses the random_word_gen function to generate words.
    '''

    sentence_word_count = random.randint(1,7)  # selects a random number for word count in sentence
    sentence = random_word_gen()  # generates the first word
    sentence = sentence.capitalize()  # capitalizes the first word

    for _ in range(sentence_word_count):  # for loop to create the sentence by concatenating random words
        rand_word = random_word_gen()  # calls the random_word_gen function to generate random word
        sentence = sentence + ' ' + rand_word  # combines the randomly generated words into a sentence
    
    return sentence

def random_paragraph_gen():
    '''
    Prints out a paragraph composed of paragraph_sentence_count randomized sentences.
    '''

    paragraph_sentence_count = random.randint(1,6)
    paragraph = ''

    for _ in range(paragraph_sentence_count):  # for loop to print each sentence
        paragraph_sentence = random_sentence_gen()  # generates the current sentence
        paragraph += paragraph_sentence + '. '
    
    return paragraph

def random_document_gen():
    '''
    Prints mutiple randomized paragraphs to a document.
    '''

    paragraph_count = random.randint(5,10)
    paragraph = ''

    with open('random_document.txt','w') as f:
        for _ in range(paragraph_count):
            paragraph = random_paragraph_gen()
            f.write(paragraph + '\n\n')

#random_paragraph_gen()
random_document_gen()