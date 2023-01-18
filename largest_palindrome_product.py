'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_number_palindrome(num):
    num_string = str(num)
    num_string_reverse = num_string[::-1]
    return num_string == num_string_reverse 


max_found = 0
max_i = 0
max_j = 0

for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        multiple = i * j
        if is_number_palindrome(multiple) and multiple > max_found:
            max_found = multiple
            max_i = i
            max_j = j

print(f"{max_i} x {max_j} = {max_found}")