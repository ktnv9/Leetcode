
def merge_strings_alternatively(word1, word2):
    
    # handle empty input cases
    if not word1 or not word2:
        return word1 + word2
    
    output = ''

    # keep merging alternatively until the end of the shorter word
    for index in range(min(len(word1), len(word2))):
        output += word1[index] + word2[index]

    # merge the rest of the word from the longer word.
    output += word1[index+1:] + word2[index+1:]
    
    return output

word1 = 'abc'
word2 = 'pqr'

merged_word = merge_strings_alternatively(word1, word2)
print(merged_word)
