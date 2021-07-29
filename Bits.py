#Texto 
texto = "bits"

#Se convierte el string a bits
stb = ''.join(format(ord(i), '08b') for i in texto)

#Se convierte de bits a string
bts = ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(stb)]*8))

#Texto Final   
print("El texto en bits es: ", stb)
print("El texto es: ",bts)
