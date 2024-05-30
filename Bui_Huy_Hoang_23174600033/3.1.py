# ý 1 : Xác suất trong ngày có 2 máy hỏng
import math
x1 = 2
n = 5
p = 0.1
two_machines_broken = ((math.factorial(n)) / (math.factorial(n-x1) * math.factorial(x1))) * p**2 * (1-p)**3
print(two_machines_broken, "là xác suất trong ngày có 2 máy hỏng")

# ý 2 : Xác suất trong ngày không quá 2 máy hỏng
x2 = 1 
x3 = 0
one_machine_broken = ((math.factorial(n)) / (math.factorial(n-x2) * math.factorial(x2))) * p**1 * (1-p)**4
no_machines_broken = ((math.factorial(n)) / (math.factorial(n-x3) * math.factorial(x3))) * p**0 * (1-p)**5

no_more_than_two_machines_broken = two_machines_broken + one_machine_broken + no_machines_broken
print(no_more_than_two_machines_broken, "là xác suất trong ngày không quá 2 máy hỏng")