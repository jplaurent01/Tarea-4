"""
Created on Fri Jul  3 09:59:07 2020

@author: Jose Pablo Laurent Chaves
Carné: B63761
Grupo: 01
"""

'''
1. Crear un esquema de modulación BPSK para los bits presentados.
 Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria)
 para cada bit y luego una concatenación de todas estas formas de onda.
'''

import numpy as np
import csv
from scipy import stats
from scipy import signal
from scipy import integrate
import matplotlib.pyplot as plt

#vector de bits vacios para su posterior lectura
bit_list = []

#Lectura archivo de bits10k.csv 
with open('bits10k.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        bit_list.append(row[0])#asignar valor

# Número de bits por generar
N = len(bit_list)

# Generar bits para "transmitir"
bit = list(map(int, bit_list)) 

# Frecuencia de operación
f = 5000 # 5 kHz

# Duración del período de cada onda
T = 1/f # 5 ms

# Número de puntos de muestreo por período
p = 50 

# Puntos de muestreo para cada período
tp = np.linspace(0, T, p)

# Creación de la forma de onda
seno = np.sin(2*np.pi * f * tp)

# Visualización de la forma de onda de la portadora
plt.plot(tp, seno)
plt.xlabel('Tiempo / s')
plt.savefig('onda.png')

# Frecuencia de muestreo
fs = p/T # 50 kHz

# Creación de la línea temporal para toda la señal Tx
t = np.linspace(0, N*T, N*p)

#Vector de la señal modulada
senal = np.zeros(N*p) #se puede usar t.shape

# Creación de la señal modulada BPSK
for k, b in enumerate(bit):
    if b==1:
        senal[k*p:(k+1)*p] = b * seno  
    else:    
        senal[k*p:(k+1)*p] = -1* seno
  
# Visualización de los primeros bits modulados
pb = 5
plt.figure()
plt.plot(senal[0:pb*p])
plt.savefig('Tx.png')

'''
2. Calcular la potencia promedio de la señal modulada generada.
'''
# Potencia intantánea
Pinst = senal**2

# Potencia promedio: promedio temporal de la potencia instantánea
Ps = integrate.trapz(Pinst, t) / (T*N)
print('Potencia promedio de la señal modulada generada :', Ps)

'''
3. Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano)
 con una relación señal a ruido (SNR) desde -2 hasta 3 dB..
'''
def AWG(SNR, U):
    Pn = Ps / 10**(SNR / 10)
    sigma = np.sqrt(Pn)
    ruido = np.random.normal(0, sigma, U)
    return  senal + ruido

#SNR = -3 dB   
SNR10 = AWG(-3, senal.shape)
# Visualización de los pirmeros bits recibidos
pb = 5
plt.figure()
plt.plot(SNR10[0:pb*p])
plt.savefig('Rx10.png') 

#SNR = -4 dB   
SNR11 = AWG(-4, senal.shape)
# Visualización de los pirmeros bits recibidos
pb = 5
plt.figure()
plt.plot(SNR11[0:pb*p])
plt.savefig('Rx11.png') 

#SNR = -5 dB   
SNR12 = AWG(-5, senal.shape)
# Visualización de los pirmeros bits recibidos
pb = 5
plt.figure()
plt.plot(SNR12[0:pb*p])
plt.savefig('Rx12.png') 

#SNR = -6 dB   
SNR13 = AWG(-6, senal.shape)
# Visualización de los pirmeros bits recibidos
pb = 5
plt.figure()
plt.plot(SNR13[0:pb*p])
plt.savefig('Rx13.png') 

#SNR = -7 dB   
SNR14 = AWG(-7, senal.shape)
# Visualización de los pirmeros bits recibidos
pb = 5
plt.figure()
plt.plot(SNR14[0:pb*p])
plt.savefig('Rx14.png') 

#SNR = -2 dB   
SNR1 = AWG(-2, senal.shape)
# Visualización de los pirmeros bits recibidos
pb = 5
plt.figure()
plt.plot(SNR1[0:pb*p])
plt.savefig('Rx1.png') 

#SNR = -1 dB     
SNR2 = AWG(-1, senal.shape)
# Visualización de los pirmeros bits recibidos
pb = 5
plt.figure()
plt.plot(SNR2[0:pb*p])
plt.savefig('Rx2.png') 

#SNR = 0  dB    
SNR3 = AWG(0, senal.shape)
# Visualización de los pirmeros bits recibidos
pb = 5
plt.figure()
plt.plot(SNR3[0:pb*p])
plt.savefig('Rx3.png') 

#SNR = 1  dB    
SNR4 = AWG(1, senal.shape)
# Visualización de los pirmeros bits recibidos
pb = 5
plt.figure()
plt.plot(SNR4[0:pb*p])
plt.savefig('Rx4.png') 

#SNR = 2 dB      
SNR5 = AWG(2, senal.shape)
# Visualización de los pirmeros bits recibidos
pb = 5
plt.figure()
plt.plot(SNR5[0:pb*p])
plt.savefig('Rx5.png')

#SNR = 3 dB   
SNR6 = AWG(3, senal.shape)
# Visualización de los pirmeros bits recibidos
pb = 5
plt.figure()
plt.plot(SNR6[0:pb*p])
plt.savefig('Rx6.png')


'''
4. Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), 
antes y después del canal ruidoso.
'''
#densidad espectral de potencia de la señal antes  del canal ruidoso
fw, PSD = signal.welch(senal, fs, nperseg=1024)
plt.figure()
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/HZ')
plt.savefig('PSD0.png')

#densidad espectral de potencia de la señal después del canal ruidoso,-2 dB
fw1, PSD1 = signal.welch(SNR1, fs, nperseg=1024)
plt.figure()
plt.semilogy(fw1, PSD1)
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/HZ')
plt.savefig('PSD1.png')

#densidad espectral de potencia de la señal después del canal ruidoso,-1 dB
fw2, PSD2 = signal.welch(SNR2, fs, nperseg=1024)
plt.figure()
plt.semilogy(fw2, PSD2)
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/HZ')
plt.savefig('PSD2.png')

#densidad espectral de potencia de la señal después del canal ruidoso,0 dB
fw3, PSD3 = signal.welch(SNR3, fs, nperseg=1024)
plt.figure()
plt.semilogy(fw3, PSD3)
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/HZ')
plt.savefig('PSD3.png')

#densidad espectral de potencia de la señal después del canal ruidoso,1 dB
fw4, PSD4 = signal.welch(SNR4, fs, nperseg=1024)
plt.figure()
plt.semilogy(fw4, PSD4)
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/HZ')
plt.savefig('PSD4.png')

#densidad espectral de potencia de la señal después del canal ruidoso,2 dB
fw5, PSD5 = signal.welch(SNR5, fs, nperseg=1024)
plt.figure()
plt.semilogy(fw5, PSD5)
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/HZ')
plt.savefig('PSD5.png')

#densidad espectral de potencia de la señal después del canal ruidoso,3 dB
fw6, PSD6 = signal.welch(SNR6, fs, nperseg=1024)
plt.figure()
plt.semilogy(fw6, PSD6)
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/HZ')
plt.savefig('PSD6.png')

'''
5. Demodular y decodificar la señal.
'''
def decof (Rx ,seno, N, p):
    #pseudo energía de la onda original
    Es = np.sum(seno**2)
    # Inicialización del vector de bits recibidos, se guardan los bits recibidos
    bitsRx = np.zeros(N)
    # Decodificación de la señal por detección de energía
    for k in range(len(bitsRx)):
        E = np.sum(Rx[k*p:(k+1)*p] * seno)
        if E > 0:
            bitsRx[k] = 1
        else:
            bitsRx[k] = 0  
    # Contar errores np.sum(np.abs(bit - bitsRx))  
    # Tasa de error de bits (BER, bit error rate) err/N     
    return np.sum(np.abs(bit - bitsRx))/N  

#Demodular y decodificar la señal para -7 dB
BER14 = decof (SNR14 ,seno, N, p) 
print('tasa de error de bits para -7 dB: ', BER14)

#Demodular y decodificar la señal para -6 dB
BER13 = decof (SNR13 ,seno, N, p) 
print('tasa de error de bits para -6 dB: ', BER13)

#Demodular y decodificar la señal para -5 dB
BER12 = decof (SNR12 ,seno, N, p) 
print('tasa de error de bits para -5 dB: ', BER12)

#Demodular y decodificar la señal para -4 dB
BER11 = decof (SNR11 ,seno, N, p) 
print('tasa de error de bits para -4 dB: ', BER11)

#Demodular y decodificar la señal para -3 dB
BER10 = decof (SNR10 ,seno, N, p) 
print('tasa de error de bits para -3 dB: ', BER10)

#Demodular y decodificar la señal para -2 dB
BER1 = decof (SNR1 ,seno, N, p) 
print('tasa de error de bits para -2 dB: ', BER1)
    
#Demodular y decodificar la señal para -1 dB
BER2 = decof (SNR2 ,seno, N, p)  
print('tasa de error de bits para -1 dB: ', BER2) 
      
#Demodular y decodificar la señal para 0 dB
BER3 = decof (SNR3 ,seno, N, p)   
print('tasa de error de bits para 0 dB: ', BER3)  
  
#Demodular y decodificar la señal para 1 dB
BER4 = decof (SNR4 ,seno, N, p)    
print('tasa de error de bits para 1 dB: ', BER4)
 
#Demodular y decodificar la señal para 2 dB
BER5 = decof (SNR5 ,seno, N, p)  
print('tasa de error de bits para 2 dB: ', BER5)    

#Demodular y decodificar la señal para 3 dB
BER6 = decof (SNR6 ,seno, N, p)  
print('tasa de error de bits para 3 dB: ', BER6)      

BER = np.array([BER14, BER13, BER12, BER11, BER10, BER1, BER2, BER3, BER4, BER5, BER6])

'''
6.Graficar BER versus SNR
'''
# Puntos de muestreo para cada SNR
snrs = np.array([-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3])
plt.figure()
plt.semilogy(snrs, BER)
plt.title('BER versus SNR')
plt.xlabel('SNR')
plt.ylabel('BER')
plt.savefig('BERVSSNR.png')