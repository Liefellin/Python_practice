# Zala Weyker
# 10/21/2023
# Censorship

badThing = input("what do you hate?")
stuff = ["puppies", "kittens", "slime"]
censored_list = [i if i != badThing.lower() else "REDACTED" for i in stuff]

print(censored_list)