#Ceasar Cipher
#---------------------

#Code Setup
import os,art

#Function
def Ceasar(direction,text,shift): #Ceasar cipher function
    os.system('cls')    
    cipheredText = ""
    option = "encrypted"
    if direction == "decode":
        shift *= -1
        option = "decrypted"    
    for chars in text:
        if chars in art.alphabet:
            position = art.alphabet.index(chars)
            cipheredText += art.alphabet[position+shift]
        else:
            cipheredText += chars
    print(f"The {option} text is:\n{cipheredText}")


#Main
shouldContinue = True
while shouldContinue: #Continuation
    print(art.logo) #User inputs
    direction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))%26

    Ceasar(direction,text,shift) #Call function

    result = input("Would you like to continue? Type 'y' or 'n'. ") #Retry?
    os.system('cls')
    if result == 'n':
        shouldContinue = False
