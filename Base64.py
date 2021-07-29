#Libreria 
import base64

##Encriptado base 64
#Texto para encriptar
texto = "cifrado base 64"

#Funcion que encripta
encriptar = base64.b64encode(texto.encode("utf-8"))
textoEncriptado = str(encriptar, "utf-8")

##Desencriptado base 64
#Funcion que desencripta
desencriptar = base64.b64decode(textoEncriptado)
textoDesencriptado = str(desencriptar, "utf-8")

#Texto final 
print("El texto encriptado es:", textoEncriptado)
print("El texto desencriptado es:", textoDesencriptado)

