
def gcd_of_strings(str1, str2):

    max_len = -1
    gcd_str = ""
    l1, l2 = len(str1), len(str2)
    for index in range(min(len(str1), len(str2))):

        substr = str1[:index+1]
        l3 = len(substr)

        if l1 % l3 == 0 and l2 % l3 == 0:
            
            mstr1 = substr * int(l1/l3)
            mstr2 = substr * int(l2/l3)

            if mstr1 == str1 and mstr2 == str2:

                if l3 > max_len:
                    max_len = l3
                    gcd_str = substr
                
    return gcd_str

str1 = "ABCABC"
str2 = "ABC"
str1 = "ABABAB"
str2 = "ABAB"
str1 = "LEET"
str2 = "CODE"
gcd_str = gcd_of_strings(str1, str2)

print(gcd_str)