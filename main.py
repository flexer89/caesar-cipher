import functions
  
functions.alphabet.reverse()
decision = "yes"

while decision=="yes":
  #Menu display and data input
  functions.clear()
  functions.logo_print()
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  
  #Function calling
  if direction =="encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    functions.encrypt(text,shift)
  elif direction =="decode":
    #reverse an alphabet to avoid out of index error
    functions.alphabet.reverse()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    functions.decrypt(text,shift)
    functions.alphabet.reverse()
  else:
    print("You picked a wrong option.")
    
  decision=input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
  