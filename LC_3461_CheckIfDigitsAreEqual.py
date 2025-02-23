def hasSameDigits(s: str) -> bool:
    
    # handle invalid input strings.
    if len(s) < 2:
        return False
    
    # Convert the input string into a list of digits.
    # Make sure to convert each digit character to an integer. 
    digits = list(map(int, s))

    # keep performin sum module 10 until length of the new list becomes 2.
    while len(digits) > 2:
        digits = [(digits[index]+digits[index+1])%10 for index in range(len(digits)-1)]

    # check if the two digits are the same.
    return digits[0] == digits[1]

s = "3902"
b = hasSameDigits(s)
print(b)

s = "34789"
b = hasSameDigits(s)
print(b)