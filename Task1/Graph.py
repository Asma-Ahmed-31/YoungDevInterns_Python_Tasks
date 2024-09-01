import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(10, 6))  


plt.plot(x, y_sin, label='Sine Wave', color='green', marker='s')
plt.plot(x, y_cos, label='Cosine Wave', color='red', marker='d')

plt.title('Comparison of Sine and Cosine Functions')


plt.xlabel('Angle in Radians')
plt.ylabel('Function Values')

plt.legend(loc='upper right')


plt.grid(True)

plt.show()