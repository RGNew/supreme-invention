import string
import random
from markov_bigrams import monogram_prob

alphabet = string.ascii_lowercase  # creates string from all lowercase letters

rand_val = random.randint(0,25)  # generates a random number from 0 to 25

def random_letter_gen(num_letters=1):
    '''
    Create list random letters using the standard English frequency.
    '''
    letters = list(monogram_prob.keys())
    probs = list(monogram_prob.values())
    generated_letters = random.choices(letters, probs, k=num_letters)
    return generated_letters


def random_word_gen():
    '''
    Returns a random word of word_length composed of letters of the alphabet.
    '''

    word = ''
    word_length = random.randint(1,10)

    letters = random_letter_gen(word_length)
    word = ''.join(letters)

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

    paragraph_sentence_count = random.randint(1,6)  # sets the amount of sentences in the paragraph
    paragraph = ''  # intializes the paragraph to be empty

    for _ in range(paragraph_sentence_count):  # for loop to print each sentence
        paragraph_sentence = random_sentence_gen()  # generates the current sentence
        paragraph += paragraph_sentence + '. '  # appends the next sentence to the paragraph
    
    return paragraph  # returns the paragraph from the function

def random_document_gen():
    '''
    Prints mutiple randomized paragraphs to a document.
    '''

    paragraph_count = random.randint(5,10)  # picks a random integer for the amount of paragraphs
    paragraph = ''  # initializes the paragraph to an empty string

    with open('random_document.html','w') as f:  # opens the HTML document that will be written to
        for _ in range(paragraph_count):  #  for loop for writing paragraphs to document
            paragraph = random_paragraph_gen()  # generates the current random paragraph
            f.write('<p>' + paragraph + '</p>')  # writes the current paragraph to the document with p tags

#random_paragraph_gen()
random_document_gen()  # runs the fucntion to generate the randomized HTML doc