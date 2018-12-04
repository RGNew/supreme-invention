import string 

bigram_probs = {letter: 1 for letter in string.ascii_lowercase}

for letter, prob in bigram_probs.items():
    print(letter, ':', prob)

monogram_counts = dict({})  # empty dictionary to write to
with open('english_monograms.txt', 'r') as f:
    for line in f:
        contents = line.split(' ')  # lines are in format 'X #'
        letter = contents[0]
        count = int(contents[1])  # convert the count to an integer for summation
        monogram_counts[letter.lower()] = count

# add up the values in the dictionary
total = sum([monogram_counts[letter] for letter in monogram_counts.keys()])

monogram_prob = {letter: monogram_counts[letter] / total for letter in monogram_counts.keys()}

for letter, prob in monogram_prob.items():
    print('Letter:', letter,'has frequency', prob)