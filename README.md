# Tarea-4
Solución Tarea 4 B63761

1) Crear un esquema de modulación BPSK para los bits presentados. Esto implica asignar una forma de onda sinusoidal normalizada (amplitud unitaria) para cada bit y luego una concatenación de todas estas formas de onda.

En la siguiente imagen se observa la forma de onda de la portadora de 5000 Hz.
![onda](onda.png)
Con base en la onda sinusoidal vista anteriormente, se procede a realizar el esquema de modulación BPSK para los bit del archivo bits10k.csv, con los cuales se obtiene la siguiente señal modulada  para BPSK.
![Tx](Tx.png)

2) Calcular la potencia promedio de la señal modulada generada.
Se obtiene como potencia promedia 0.4900009800019598 W de la señal modulada generada por BPSK. 

3) Simular un canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB.



4) Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso.


5)  Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR.


6) Graficar BER versus SNR.
