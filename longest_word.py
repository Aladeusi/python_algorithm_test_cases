# this code returns longest word in a phrase or sentence
def get_longest_word(sentence):
    longest_word=""
    for word in str(sentence).split(" "): longest_word=word if len(word) > len(longest_word) else longest_word
    return longest_word

print get_longest_word("This is the begenning of algorithm")
    
    
    
    