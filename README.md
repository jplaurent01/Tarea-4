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

Para la simulación del canal ruidoso del tipo AWGN, se utiliza una relación señal a ruido (SNR) desde -7 hasta 3 dB, ya que la modulación BPSK, es muy robusta y se pretende obtener a partir de dicho intervalo cierto grado de error al transmitir bits.

![Rx14](Rx14.png)
Canal ruidoso para -7 dB

![Rx13](Rx13.png)
Canal ruidoso para -6 dB

![Rx12](Rx12.png)
Canal ruidoso para -5 dB

![Rx11](Rx11.png)
Canal ruidoso para -4 dB

![Rx10](Rx10.png)
Canal ruidoso para -3 dB

![Rx1](Rx1.png)
Canal ruidoso para -2 dB

![Rx2](Rx2.png)
Canal ruidoso para -1 dB

![Rx3](Rx3.png)
Canal ruidoso para 0 dB

![Rx4](Rx4.png)
Canal ruidoso para 1 dB

![Rx5](Rx5.png)
Canal ruidoso para 2 dB

![Rx6](Rx6.png)
Canal ruidoso para 3 dB


4) Graficar la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso.


5)  Demodular y decodificar la señal y hacer un conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR.


6) Graficar BER versus SNR.
