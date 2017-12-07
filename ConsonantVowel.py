###############################################
# ConsonantVowel.py
# Vandenburg 2015 / De Borde 2017
##############################################

# INSTRUCTIONS

##############################################################
# Improve the VowelsConsonants program to show the vowels
# consonants and other characters in a separate line instead
# of including other characters with the consonants.
##############################################################

userInput = input("Enter your sentence: ")
vowels = "AEIOUaeiou"

displayVowels = ""
displayConsonants = ""
displayOther = ""

for letter in userInput:
    if letter in vowels:
        displayVowels += letter
    elif letter.isalpha():
        displayConsonants += letter
    else:
        displayOther += letter


print("Vowels: " + displayVowels)
print("Consonants: " + displayConsonants)
print("Other: " + displayOther)
