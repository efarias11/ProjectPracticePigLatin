# Translate inputted words and whole sentences into pig latin

print("Hello, I am going to translate your words into pig latin for my cajun grandpa.")
print("")

inputted_word = input("What is the first word that comes to mind?: ")

pig_latin_1 = inputted_word[1::]
pig_latin_letter = inputted_word[:1]
pig_latin_ay = "ay"

print("")
print("Grandpa, he said: "+pig_latin_1+pig_latin_letter+pig_latin_ay)
