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


def decoding():
    if Decode == "Y" or "Yes":
        decode = raw_input("Type your sentence: ")
        decodeshift = raw_input("How many shifts to the left? ")
        for letter in decode:
            if letter.isalpha() and decodeshift.isdigit() and len(decodeshift) == 1:
                decodenum = alphabet.find(decode)
                decodenum += n
                decoded = alphabet.find("decodenum")
                print(decoded)
                if decodenum == "0":
                    decodenum += 26
                elif decodenum == "26":
                    decodenum -= 26
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
