###############################################
# CeaserCypher.py                             #
# Your name here Alex H                       #
###############################################

# INSTRUCTIONS #

##############################################################
# This is where you assignment will be created               #
##############################################################
from pip._vendor.distlib.compat import raw_input
Decode = raw_input("Decode? ")
Encode = raw_input("Encode? ")
alphabet = "abcdefghijklmopqrstuvwxyz"
decode = raw_input("Type your sentence: ")
decodeShift = raw_input("How many shifts to the left? ")


def decoding():
    if Decode == "Y" or "Yes":
        for letter in decode:
            if letter.isalpha():
                if decodeShift.isdigit():
                    decodenum = alphabet.find(decode)
                    decodenum += decodeShift
                    decoded = alphabet.find(decodenum)
        print(decoded)
    elif Decode == "N" or "No":
        encoding()
    else:
        print("You did not say 'Yes 'or 'No'")
        decoding()


def encoding():
    if Encode == "Y" or "Yes":
        print("Unfinished")
    elif Encode == "N" or "No":
        decoding()
    else:
        print("You did not say 'Yes' or 'No'")
        encoding()

decoding()
