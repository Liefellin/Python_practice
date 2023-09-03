# Zala Weyker
# 9/1/2023
# Digit of life calculator
# A "Digit of life" is the digit you get when you
# add together all the digits in the numerical form of your birthday,
# then add THOSE digits together if there is more than one,
# and repeat this process until you are left with one digit.

def add_digits_loop(num):
    while len(str(num))>1:
        new_num = 0
        for digit in str(num):
            new_num += int(digit)
        num = new_num
    return num


print("Your digit of life is " + str(add_digits_loop(input("Find out your digit of life! Enter your birthday number in this format: MMDDYYYY\n"))) + "!")
