# Problem 1
def reverse_number(num:str) -> str:
    
    # sets a starting index value at 1 and output as an empty string
    i = 1
    output = ""
    
    # loops over every digit in num using index i and concatenates the reverse index character of the string to the output 
    while i <= len(num):
        output += num[-i]
        i += 1
    
    return output

# Problem 2
def sum_of_digits(num:str) -> int:
    
    # checks if num is a number
    if not num.isdigit():
        return f'ERROR: "{num}" is a float or NaN'

    # sets starting index value and output to 0
    i, output = 0, 0

    # loops over every value in len(num) using index i
    while i < len(num):

        # adds the value of num[i] to the output and moves on to the next digit
        output += int(num[i])
        i += 1

    return output

# Problem 3
def multiples_of_three(n:int) -> None:

    # checks if n is an int
    if not isinstance(n, int):
        print(f'ERROR "{n}" is not an int')

        # previous functions had returns instead of prints so now if the check is triggered the function returns None
        return

    # sets starting index to 0
    i = 0

    # iterates once for every value <= multiples of 3 in n
    while i <= n // 3:

        # moves on to next multiple of 3
        i += 1

    # prints output of "x" multiplied by index; multiplies by i - 1 because of i starts at 0
    print("x" * (i - 1))
