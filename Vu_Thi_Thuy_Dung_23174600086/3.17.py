# ý 1 : Tỉ lệ chỗ đậu xe có thể sử dụng
'''Chiều dài trung bình của bãi đỗ xe là kì vọng E(X) = muy
----> Chiều dài xe của người đàn ông là (0.15*muy)
mà sigma = (0.01 ** 1/2) * muy nên ta có:   
'''
fz = (0.15-1) / (0.01**(1/2))
fz_new_value = 0
if fz == -8.5:
    fz_new_value += 0    # tra bảng 2
P_parking = 1 - fz_new_value
print(P_parking, "là xác suất chỗ đỗ xe có thể sử dụng")

# ý 2 : Chiều dài của xe = bao nhiêu nếu muốn chủ của nó có thể sử dụng 90% chỗ đậu xe?
muy = 4
square_sigma = 0.01 * (muy**2)
P_car_length = 0.9
fz2 = 1-0.9
fz2_new_value = 0
if fz2 == 0.1:
    fz2_new_value += 2.8     # tra bảng
car_length = (fz2_new_value * square_sigma) +4
print(car_length, "là chiều dài thỏa mãn yêu cầu đề bài")