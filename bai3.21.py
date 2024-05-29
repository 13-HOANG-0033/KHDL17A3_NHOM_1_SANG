#Y = e**(-x) với lambda = 2
#Ex=tích phân từ 0 đén vô cùng của e**(-x)*2*e**(-2x)
Ex=2/3
#Ex=tích phân từ 0 đén vô cùng của e**(-2x)*2*e**(-2x) - Ex**2
Vx=1/2-(2/3)**2
dolechchuan=Vx**(1/2)
print("kì vọng của biến Y = e**(-x) =",Ex)
print("độ lệch chuẩn của biến Y = e**(-x) =",Ex)