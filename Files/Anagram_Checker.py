# Zala Weyker
# 9/1/2023
# Anagram Checker

def compile_text(text):
    letters = {}
    for character in text:
        character = character.lower()
        if character.isalpha():
            if character in letters:
                letters[character] += 1
            else:
                letters[character] = 1
    return letters
    # creates, fills up, and returns the letters dictionary with a counter of how many of each letter are in text. Ignores non-letters


def is_anagram(text1, text2):
    return compile_text(text1) == compile_text(text2)
    # checks if texts compile into the same letter counting dictionary as per compile_text(). if so, we've got an anagram!


print(is_anagram(input(), input()))

