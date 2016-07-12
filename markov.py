from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()
    contents = contents.replace('\n', ' ')
    return contents


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

# initialize empty dictionary
# call open_and_read
# # for loop - if indices 0 and 1 of contents exist in dictionary key tuple list, add index 2 to value list
# #     if indices 0 and 1 do not exist in dictionary key tuple list, add both the key tuple and value
# #       remove first element of string
# # return dictionary

    chains = {('word', 'stuff'): [1, 2], ('omg', 'wow'): [3, 4], ('Would', 'you'): [5, 6]}

#     # your code goes here
    words = text_string.split()
    
    for word in words: 
        bigram = (words[0], words[1])
        if bigram in chains.keys():
            next_words = chains[bigram]             
            next_words.append(words[2])
            chains[bigram] = next_words
            words = words[1:]
        
        else:
            chains[bigram] = []
            next_words.append(words[2])
            chains[bigram] = next_words
            words = words[1:]
        
    print words
    


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
