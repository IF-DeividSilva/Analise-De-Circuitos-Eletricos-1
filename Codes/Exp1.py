import numpy as np
import matplotlib.pyplot as plt

# Dados da Tabela 2
V = np.array([0, 2, 4, 6, 8, 10, 12]) # Tensão em volts
I = np.array([0.04, 2.49, 5.03, 7.5, 10.01, 12.44, 14.91]) / 1000 # Corrente em mA convertida para A (820)
#I = np.array([0.01, 0.93, 1.85, 2.77, 3.69, 4.6, 5.51]) / 1000 # Corrente em mA convertida para A (2200)
Rx = 820 # Resistência em ohms

# Realizando a regressão linear
coefs = np.polyfit(V, I, 1)

# Coeficientes da regressão linear
m, b = coefs

# Verificando se a inclinação é igual a Rx
print(f"Inclinação da reta: {m} Ω")
print(f"Resistência do bipolo: {Rx} Ω")

# Plotando os dados e a reta de regressão
plt.scatter(V, I, label='Dados')
plt.plot(V, m*V + b, color='red', label='Reta de regressão')
plt.xlabel('Tensão (V)')
plt.ylabel('Corrente (A)')
plt.title('Gráfico de V x I Resistor 820 Ω')
plt.legend()
plt.grid(True)
plt.show()
