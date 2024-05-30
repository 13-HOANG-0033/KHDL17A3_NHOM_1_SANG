import math

# Hàm tính giai thừa
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Hàm tính xác suất theo phân phối Poisson
def poisson_probability(k, lamb):
    return (math.exp(-lamb) * (lamb ** k)) / factorial(k)

# 1) Tính xác suất tất cả 4 chiếc ôtô đều được thuê
prob_all_rented = poisson_probability(4, 2)

# 2) Tính xác suất không phải tất cả 4 chiếc ôtô đều được thuê
prob_not_all_rented = 1 - poisson_probability(0, 2)

# 3) Tính xác suất cửa hàng không đáp ứng được yêu cầu
prob_no_car_rented = poisson_probability(0, 2)

# 4) Trung bình có bao nhiêu ôtô được thuê
average_rented = 2

# 5) Tìm số ôtô cần có để xác suất không đáp ứng được nhu cầu cần thuê bé hơn 2%
required_cars = 0
while poisson_probability(0, required_cars) >= 0.02:
    required_cars += 1

# In kết quả
print("1) Xác suất tất cả 4 chiếc ôtô đều được thuê:", prob_all_rented)
print("2) Xác suất không phải tất cả 4 chiếc ôtô đều được thuê:", prob_not_all_rented)
print("3) Xác suất cửa hàng không đáp ứng được yêu cầu:", prob_no_car_rented)
print("4) Trung bình có bao nhiêu ôtô được thuê:", average_rented)
print("5) Cửa hàng cần có ít nhất", required_cars, "ô tô để xác suất không đáp ứng được nhu cầu cần thuê bé hơn 2%")