#Write a Python program to count the frequency of each character in a string (ignore the case of letters).


str = input('Enter your line: ').lower()


dct = dict()
for i in str:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1

print(dct)