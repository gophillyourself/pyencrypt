def inputencrypt(text, privkey):
  enc_text = []
  text_arr = list(text)
  for i in range(0, len(text)):
    encrypted = ord(text_arr[i]) * privkey
    print(text_arr[i]," ", ord(text_arr[i]), " * ",privkey )
    enc_text.append(encrypted)
  
  print("Encrypted text = ", enc_text )
  return(enc_text)

def decrypt(enc_text, privkey):
  dec = []
  for i in range(0, len(enc_text)):
    dec.append(chr(int(enc_text[i] / privkey)))

  print(dec)
  

privkey = int(input("Enter Priv Key (int) : "))
text = input("Enter Text to be encrypted : ")

enc_text = inputencrypt(text, privkey)

decrypt(enc_text, privkey)
  