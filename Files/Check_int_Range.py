def read_int(prompt, minimum, maximum):
    try:
        assert minimum <= int(prompt) <= maximum
        return prompt
    except AssertionError:
        print(f"Error: the value is not within permitted range ({minimum}..{maximum})")
    except ValueError:
        print("Error: wrong input")


v = False
while not v:
    v = read_int(input("Enter a number from -10 to 10: "), -10, 10)
print("The number is:", v)
