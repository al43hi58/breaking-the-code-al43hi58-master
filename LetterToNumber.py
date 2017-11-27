###############################################
# LetterToNumber.py
# Vandenburg 2015 / De Borde 2017
##############################################

# INSTRUCTIONS

##############################################################
# Your task is to write a program in Python that:
# 1) Asks the user to type in a letter
# 2) Finds the position of that letter in the alphabet
# 3) Display that letter back to the user
##############################################################


# Create a variable with all the letters in the alphabet
alphabetbig="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabetsmall="abcdefghijklmnopqrstuvwxyz"
# Ask the user to type in a letter
letter=input("Please type a letter: ")

# Find the position of the letter in the alphabet
posbig=alphabetbig.find(letter)
possmall=alphabetsmall.find(letter)
# As the first position is 0, we need to add 1
posbig += 1
possmall += 1
#display the number back to the user
print(posbig + possmall)


