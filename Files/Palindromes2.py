def is_a_palindrome_1(input_string):
    input_string = input_string.replace(" ", "").lower()
    reversed_string = input_string[::-1]
    return reversed_string == input_string != ""
        

def is_a_palindrome_2(input_string):
    input_list = [i for i in input_string.lower() if i.isalpha()]
    print(input_list)
    while len(input_list) > 1:
        if input_list.pop(0) != input_list.pop(-1):
            return False
    return True


if is_a_palindrome_1(input()):
    print("It's a palindrome")
else:
    print("it's not a palindrome")
print(is_a_palindrome_2("I'm a very yreva mi"))