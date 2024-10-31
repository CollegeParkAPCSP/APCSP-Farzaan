def reverse_number(num:str) -> str:
    i = 1
    output = ""
    while i <= len(num):
        output += num[-i]
        i += 1
    
    return output
 
def sum_of_digits(num:str) -> int:
    if not num.isdigit():
        return f'ERROR: "{num}" is a float or NaN'

    i, output = 0, 0
    while i < len(num):
        output += int(num[i])
        i += 1

    return output

def multiples_of_three(n:int) -> None:
    if not isinstance(n, int):
        print(f'ERROR "{n}" is not an int')
        return
    
    i = 0
    while i <= n // 3:
        i += 1

    print("x" * (i - 1))
