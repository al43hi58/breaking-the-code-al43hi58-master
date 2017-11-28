###############################################
# CeaserCypher.py
# Your name here
##############################################

# INSTRUCTIONS

##############################################################
# This is where you assignment will be created
##############################################################
from pip._vendor.distlib.compat import raw_input
Decode = raw_input("Decode? ")
Encode = raw_input("Encode? ")
alphabet="abcdefghijklmopqrstuvwxyz"
decode = raw_input("Type your sentence: ")

def decoding():
    if Decode == "Y" or "Yes":

        print("Unfinished")
    if Decode == "N" or "No":
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
