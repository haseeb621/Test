# 1. ⁠Write a program that takes a string as input and prints the reversed string.

def reverse_string(input_string):
    reversed_str = ''
    for x in range(len(input_string)-1,-1,-1):
     reversed_str += input_string[x]
    return reversed_str

input_string = '543shahzaib21'
print("Reversed string:", reverse_string(input_string))