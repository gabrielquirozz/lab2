import nltk
import re
import numpy as np
import pandas
from collections import Counter
import matplotlib.pyplot as plt
import string
import random

#-----------------------1---------------------------------
x = "10110111000110"
y = "10100100110010"


def operacionXOR (cadena1, cadena2):
    y = int(cadena1, 2)^int(cadena2,2)
    y = bin(y)[2:].zfill(len(cadena1))

    return y

print(operacionXOR (x, y))

#--------------------------2-------------------------------
#“Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a
#lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short
#vehemence of any carnal pleasure
Z = "11100010100000001001110001001101011000010110111000100000011010010111001100100000011001000110100101110011011101000110100101101110011001110111010101101001011100110110100001100101011001000010110000100000011011100110111101110100001000000110111101101110011011000111100100100000011000100111100100100000011010000110100101110011001000000111001001100101011000010111001101101111011011100010110000100000011000100111010101110100001000000110001001111001001000000111010001101000011010010111001100100000011100110110100101101110011001110111010101101100011000010111001000100000011100000110000101110011011100110110100101101111011011100010000001100110011100100110111101101101001000000110111101110100011010000110010101110010001000000110000101101110011010010110110101100001011011000111001100101100001000000111011101101000011010010110001101101000001000000110100101110011001000000110000100001010011011000111010101110011011101000010000001101111011001100010000001110100011010000110010100100000011011010110100101101110011001000010110000100000011101000110100001100001011101000010000001100010011110010010000001100001001000000111000001100101011100100111001101100101011101100110010101110010011000010110111001100011011001010010000001101111011001100010000001100100011001010110110001101001011001110110100001110100001000000110100101101110001000000111010001101000011001010010000001100011011011110110111001110100011010010110111001110101011001010110010000100000011000010110111001100100001000000110100101101110011001000110010101100110011000010111010001101001011001110110000101100010011011000110010100100000011001110110010101101110011001010111001001100001011101000110100101101111011011100010000001101111011001100010000001101011011011100110111101110111011011000110010101100100011001110110010100101100001000000110010101111000011000110110010101100101011001000111001100100000011101000110100001100101001000000111001101101000011011110111001001110100000010100111011001100101011010000110010101101101011001010110111001100011011001010010000001101111011001100010000001100001011011100111100100100000011000110110000101110010011011100110000101101100001000000111000001101100011001010110000101110011011101010111001001100101"

#se hallan monogramas (simbolos)
tokens = re.findall('.', Z)
#se genera un objeto de tipo FreqDist (contiene un diccionario adentro)
freq = nltk.FreqDist(tokens)
top = freq.most_common(50)
array = [a[1] for a in top]
f = np.array(array)

#se generan las probabilidades
p = f/f.sum()
pfreq= {top[i][0]: p[i] for i in range(0, len(top))}

#histograma
df = pandas.DataFrame.from_dict(pfreq, orient='index')
df.plot(kind='bar')
plt.show()


#----------------------3------------------------------

#se hallan bigramas (simbolos)
tokens = re.findall('..', Z)
#se genera un objeto de tipo FreqDist (contiene un diccionario adentro)
freq = nltk.FreqDist(tokens)
top = freq.most_common(50)
array = [a[1] for a in top]
f = np.array(array)

#se generan las probabilidades
p = f/f.sum()
pfreq= {top[i][0]: p[i] for i in range(0, len(top))}

#histograma
df = pandas.DataFrame.from_dict(pfreq, orient='index')
df.plot(kind='bar')
plt.show()

#se hallan trigramas (simbolos)
tokens = re.findall('...', Z)
#se genera un objeto de tipo FreqDist (contiene un diccionario adentro)
freq = nltk.FreqDist(tokens)
top = freq.most_common(50)
array = [a[1] for a in top]
f = np.array(array)

#se generan las probabilidades
p = f/f.sum()
pfreq= {top[i][0]: p[i] for i in range(0, len(top))}

#histograma
df = pandas.DataFrame.from_dict(pfreq, orient='index')
df.plot(kind='bar')
plt.show()

def stringabits(texto):
    stb = ''.join(format(ord(i), '08b') for i in texto)
    return stb

texto = input("Ingrese una cadena de texto:\n")
print(texto, ',',stringabits(texto))

number_of_strings = 1
length_of_string = len(texto)
for x in range(number_of_strings):
  textoy = ''.join(random.choice(string.ascii_letters) for _ in range(length_of_string))

print('Cadena aleatoria:', stringabits(textoy))
Z2 = operacionXOR(str(stringabits(texto)), str(stringabits(textoy)))
print('Operacion XOR:', Z2)

#se hallan monogramas (simbolos)
tokens = re.findall('.', stringabits(Z2))
#se genera un objeto de tipo FreqDist (contiene un diccionario adentro)
freq = nltk.FreqDist(tokens)
top = freq.most_common(50)
array = [a[1] for a in top]
f = np.array(array)

#se generan las probabilidades
p = f/f.sum()
pfreq= {top[i][0]: p[i] for i in range(0, len(top))}

#histograma
df = pandas.DataFrame.from_dict(pfreq, orient='index')
df.plot(kind='bar')
plt.show()


#----------------------3------------------------------

#se hallan bigramas (simbolos)
tokens = re.findall('..', stringabits(Z2))
#se genera un objeto de tipo FreqDist (contiene un diccionario adentro)
freq = nltk.FreqDist(tokens)
top = freq.most_common(50)
array = [a[1] for a in top]
f = np.array(array)

#se generan las probabilidades
p = f/f.sum()
pfreq= {top[i][0]: p[i] for i in range(0, len(top))}

#histograma
df = pandas.DataFrame.from_dict(pfreq, orient='index')
df.plot(kind='bar')
plt.show()

#se hallan trigramas (simbolos)
tokens = re.findall('...', stringabits(Z2))
#se genera un objeto de tipo FreqDist (contiene un diccionario adentro)
freq = nltk.FreqDist(tokens)
top = freq.most_common(50)
array = [a[1] for a in top]
f = np.array(array)

#se generan las probabilidades
p = f/f.sum()
pfreq= {top[i][0]: p[i] for i in range(0, len(top))}

#histograma
df = pandas.DataFrame.from_dict(pfreq, orient='index')
df.plot(kind='bar')
plt.show()


#se hallan monogramas (simbolos)
tokens = re.findall('.', stringabits(textoy))
#se genera un objeto de tipo FreqDist (contiene un diccionario adentro)
freq = nltk.FreqDist(tokens)
top = freq.most_common(50)
array = [a[1] for a in top]
f = np.array(array)

#se generan las probabilidades
p = f/f.sum()
pfreq= {top[i][0]: p[i] for i in range(0, len(top))}

#histograma
df = pandas.DataFrame.from_dict(pfreq, orient='index')
df.plot(kind='bar')
plt.show()


#----------------------3------------------------------

#se hallan bigramas (simbolos)
tokens = re.findall('..', stringabits(textoy))
#se genera un objeto de tipo FreqDist (contiene un diccionario adentro)
freq = nltk.FreqDist(tokens)
top = freq.most_common(50)
array = [a[1] for a in top]
f = np.array(array)

#se generan las probabilidades
p = f/f.sum()
pfreq= {top[i][0]: p[i] for i in range(0, len(top))}

#histograma
df = pandas.DataFrame.from_dict(pfreq, orient='index')
df.plot(kind='bar')
plt.show()

#se hallan trigramas (simbolos)
tokens = re.findall('...', stringabits(textoy))
#se genera un objeto de tipo FreqDist (contiene un diccionario adentro)
freq = nltk.FreqDist(tokens)
top = freq.most_common(50)
array = [a[1] for a in top]
f = np.array(array)

#se generan las probabilidades
p = f/f.sum()
pfreq= {top[i][0]: p[i] for i in range(0, len(top))}

#histograma
df = pandas.DataFrame.from_dict(pfreq, orient='index')
df.plot(kind='bar')
plt.show()
