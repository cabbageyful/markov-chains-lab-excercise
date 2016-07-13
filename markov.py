from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    f = open(file_path)

    contents = f.read()

    f.close()

    # contents = contents.replace('\n', ' ')
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
# # while loop - if indices 0 and 1 of contents exist in dictionary key tuple list, add index 2 to value list
# #     if indices 0 and 1 do not exist in dictionary key tuple list, add both the key tuple and value
# #       remove first element of string
# # return dictionary

    chains = {}

#     # your code goes here
    words = text_string.split()

    while len(words) > 2:
        bigram = (words[0], words[1])
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
    
    # your code goes here
    random_phrase = choice(chains.keys())
        
    while random_phrase in chains.keys():
        next_two = [random_phrase[0], random_phrase[1]] 
        if text == []:    
            # .extend and .append are on two separate lines because each
            # method changes the list in place and doesn't return an object
            text.extend(next_two)
            text.append(choice(chains[random_phrase]))
            
        else:
            text.append(choice(chains[random_phrase]))

        random_phrase = (text[-2], text[-1])

    text = ' '.join(text)

    return text
    # return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
