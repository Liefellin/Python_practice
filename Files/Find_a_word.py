# Zala Weyker
# 9/10/2023
# Find a word
# This program accepts two strings. one is a word, the second a meaningless jumble of characters. This program will determine whether or not the second string contains a jumbled version of the first string hidden among it's characters.
def compile_text(text):
    letters = {}
    for character in text.lower():
        if character.isalpha():
            if character in letters:
                letters[character] += 1
            else:
                letters[character] = 1
    return letters


def contains_scrambled_word(word, scramble):
    word = compile_text(word)
    scramble = compile_text(scramble)
    for character in word:
        if character in scramble:
            if scramble[character] >= word[character]:
                pass
            else:
                return False
        else:
            return False
    return True


print(contains_scrambled_word("dog", "ifnunq ubuybubyubbubuinij"))
print(contains_scrambled_word("dog", "nbuyudnunuiauhduaindoubuggh"))
