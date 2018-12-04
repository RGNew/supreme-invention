import string 

bigram_probs = {letter: 1 for letter in string.ascii_lowercase}

for letter, prob in bigram_probs.items:
    print(letter, ':', prob)