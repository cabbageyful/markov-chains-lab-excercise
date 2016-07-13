from random import choice

import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_path = open(sys.argv[1])

    contents = file_path.read()

    file_path.close()

    return contents


def make_chains(text_string, n):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

# add new argument for n of n-gram
# while len(words) > n
# "bigram" now equals n-gram
#     ngram = use range to create tuple up to index n-1
# if ngram exists in list of keys
#     append.words[n]
# else
#     add new key and value of words[n]
# return list slice of words[n-1:]    

    chains = {}

#     # your code goes here
    words = text_string.split()

    # Stopped here, close but need to figure out else
    ngram = tuple(words[i] if i < n + 1 else "" for i in range(len(words)))


    while len(words) > n:

        if bigram in chains.keys():
            chains[bigram].append(words[2])
                        
        else:
            chains[bigram] = [ words[2] ]
        
        words = words[1:]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

# initiliaze empty string
# pick random tuple key
# if key exists then...
# string = join tuple key and value
# return the next tuple key which would be second and third words of the new string

    text = []
    
    random_phrase = choice(chains.keys())
        
    while random_phrase in chains.keys():
        next_two = [random_phrase[0], random_phrase[1]] 
        if text == []:    
            # .extend and .append are on two separate lines because each
            # method changes the list in place and doesn't return an object
            text.extend(next_two)
            
        text.append(choice(chains[random_phrase]))

        random_phrase = (text[-2], text[-1])

    text = ' '.join(text)

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 4)

# Produce random text
#random_text = make_text(chains)

print random_text


