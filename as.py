""" numeros impares Calcule el SENO 
de la suma de la raiz cúbica de las areas de los cuadrados de lado 3L,
siendo L los números IMPARES """
import math as m
a = 0
for i in range(5321, 8796):
    if i % 2 != 0:
        h = (i * 3)**2
        a += (h)**(1/3)
print(round(m.sin(a),6))
