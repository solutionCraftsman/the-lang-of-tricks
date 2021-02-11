
import string

phrase = "Madam I'm Adam"
print(phrase)
for character_to_remove in string.punctuation + string.whitespace:
    phrase = phrase.replace(character_to_remove, "")


print("after")
print(phrase)

alphabets = []
for i in range(65, 91):
    alphabets.append(chr(i).lower())


print(alphabets)
