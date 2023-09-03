def is_a_palindrome_1(input_string):
    input_string = input_string.replace(" ","").lower()
    reversed_string = []
    for character in input_string:
        reversed_string.insert(0, character)
    print(reversed_string)
    if "".join(reversed_string)==input_string!="":
        return True
    else:
        return False

def is_a_palindrome_2(input_string):
    pairs=[]
    input_list = [i for i in input_string.replace(" ","").lower()]
    print(input_list)
    while len(input_list)>1:
        pairs.append([input_list.pop(0),input_list.pop(-1)])
    print(pairs)
    for item in pairs:
        if item[0]!=item[1]:
            return False
    return True

if is_a_palindrome_2(input()):
    print("It's a palindrome")
else:
    print("it's not a palindrome")