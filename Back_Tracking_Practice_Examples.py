
# given a string, return all possible substrings of length = 2.

def get_substrings(input_str, substring, desired_substr_length, substrings_list):

    # base case: return if desired sub str length is 0.
    if not desired_substr_length:
        substrings_list.append('')
        return

    # base case: store the substring in the list and return.
    if len(substring) == desired_substr_length:
        substrings_list.append(substring)
        return

    # base case: return if input_str is empty
    if not input_str:
        return

    # recursive call
    for index in range(len(input_str)):
        get_substrings(input_str[index+1:], substring + input_str[index], desired_substr_length, substrings_list)


def get_specified_length_substrings(input_str, desired_substr_length):

    substring = ''
    substrings_list = []

    get_substrings(input_str, substring, desired_substr_length, substrings_list)
    return substrings_list


input_str = 'abcd'
desired_substr_length = 3
L = get_specified_length_substrings(input_str, desired_substr_length)
print(L) # Output: ['abc', 'abd', 'acd', 'bcd']


input_str = 'abcd'
desired_substr_length = 2
L = get_specified_length_substrings(input_str, desired_substr_length)
print(L)  # Output: ['ab', 'ac', 'ad', 'bc', 'bd', 'cd']

input_str = 'abc'
desired_substr_length = 4
L = get_specified_length_substrings(input_str, desired_substr_length)
print(L)  # Output: []

input_str = ''
desired_substr_length = 2
L = get_specified_length_substrings(input_str, desired_substr_length)
print(L)  # Output: []


input_str = 'abcd'
desired_substr_length = 0
L = get_specified_length_substrings(input_str, desired_substr_length)
print(L) # Output: ['']