import math
# ý 1
nx = 1
px = 1/5
ny = 2
py = 1/5
P_x_equals_0 = ((math.factorial(nx)) / (math.factorial(nx-0) * math.factorial(0))) * (px **0) * (1-px)**nx
P_x_equals_1 = ((math.factorial(nx)) / (math.factorial(nx-1) * math.factorial(1))) * (px **1) * (1-px)**nx

P_y_equals_0 = ((math.factorial(ny)) / (math.factorial(ny-0) * math.factorial(0))) * (py **0) * (1-py)**ny
P_y_equals_1 = ((math.factorial(ny)) / (math.factorial(ny-1) * math.factorial(1))) * (py **1) * (1-py)**ny
P_y_equals_2 = ((math.factorial(ny)) / (math.factorial(ny-2) * math.factorial(2))) * (py **2) * (1-py)**ny

P_x_plus_y_equals_0 = P_x_equals_0 * P_y_equals_0
P_x_plus_y_equals_1 = (P_x_equals_0 * P_y_equals_1) + (P_x_equals_1 * P_y_equals_0)
P_x_plus_y_equals_2 = (P_x_equals_0 * P_y_equals_2) + (P_x_equals_1 * P_y_equals_1)
P_x_plus_y_equals_3 = P_x_equals_1 * P_y_equals_2
print("Bảng phân phối xác suất X + Y với các giá trị X = 0,1,2,3 có giá trị P là: ", P_x_plus_y_equals_0, P_x_plus_y_equals_1, P_x_plus_y_equals_2, P_x_plus_y_equals_3)

# ý 2
nx2 = 1
px2 = 1/2
ny2 = 2
py2 = 1/2
P2_x_equals_0 = ((math.factorial(nx2)) / (math.factorial(nx2-0) * math.factorial(0))) * (px2 **0) * (1-px2)**nx2
P2_x_equals_1 = ((math.factorial(nx2)) / (math.factorial(nx2-1) * math.factorial(1))) * (px2 **1) * (1-px2)**nx2

P2_y_equals_0 = ((math.factorial(ny2)) / (math.factorial(ny2-0) * math.factorial(0))) * (py2 **0) * (1-py2)**ny2
P2_y_equals_1 = ((math.factorial(ny2)) / (math.factorial(ny2-1) * math.factorial(1))) * (py2 **1) * (1-py2)**ny2
P2_y_equals_2 = ((math.factorial(ny2)) / (math.factorial(ny2-2) * math.factorial(2))) * (py2 **2) * (1-py2)**ny2

P2_x_plus_y_equals_0 = P2_x_equals_0 * P2_y_equals_0
P2_x_plus_y_equals_1 = (P2_x_equals_0 * P2_y_equals_1) + (P2_x_equals_1 * P2_y_equals_0)
P2_x_plus_y_equals_2 = (P2_x_equals_0 * P2_y_equals_2) + (P2_x_equals_1 * P2_y_equals_1)
P2_x_plus_y_equals_3 = P2_x_equals_1 * P2_y_equals_2
print("Bảng phân phối xác suất X + Y với X = 0,1,2,3 có giá trị P là: ", P2_x_plus_y_equals_0, P2_x_plus_y_equals_1, P2_x_plus_y_equals_2, P2_x_plus_y_equals_3)

if P2_x_plus_y_equals_0 > P2_x_plus_y_equals_3:
    print("Không phải phân phối nhị thức")
else:
    print("Đây là phân phối nhị thức")