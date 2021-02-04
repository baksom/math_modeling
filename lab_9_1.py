
import numpy as np
	
from scipy.integrate import odeint
	
import matplotlib.pyplot as plt
	
 
	
# Пределы изменения переменной величины
	
# В данной задаче переменной величиной является время
	
t = np.arange(0, 10, 0.1)
	
 
	
# Запись диф. уравнения в виде функции
	
def radio_function(m, t):
	
    dmdt =  k * m
	
    return dmdt
	
 
	
# Определение начальных условий и параметров
	
m_0 = 2
	
k = 1.25
	


'''
k_m = 2 
k_T =10
'''

# Решение дифференциального уравнения функцией odeint
solve_Bi = odeint(radio_function, m_0, t)

# Построение решения в виде графика функции
plt.plot(t, solve_Bi[:,0], label='')
plt.xlabel('скорость размножения')
plt.ylabel('количество бактерий')
plt.title('Размножения бактерий')
plt.legend()

plt.show()