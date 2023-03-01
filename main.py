# Translate inputted words and whole sentences into pig latin
import random

print("Hello, I am going to translate your words into pig latin for my cajun grandpa.")

inputted_word = input("\nWhat is the first word that comes to mind?: ")

pig_latin_1 = inputted_word[1::]
pig_latin_letter = inputted_word[:1]
pig_latin_ay = "ay"

print("Grandpa, he said: "+pig_latin_1+pig_latin_letter+pig_latin_ay)

print("\nHmmm? Interesting, that's the first thing that came to mind?")

inputted_sentence = input("\nOk, I am hesitant. But, do you wanna tell grandpa anything else?: ")

words = inputted_sentence.split()

for word in words:
    words[words.index(word)] = (word[1::]+word[:1]+"ay").title()

s = ' '.join(words)
print("Ughhh... grandpa he said: "+s)







