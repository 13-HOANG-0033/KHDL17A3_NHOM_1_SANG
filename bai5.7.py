# Số lượng sản phẩm
n = 4000
# Xác suất chi tiết đạt tiêu chuẩn
p = 0.8
# Kỳ vọng (mean)
Ex = n * p
# Phương sai (variance)
Vx = n * p * (1 - p)
# Độ lệch chuẩn (standard deviation)
dolechchuan = Vx**(1/2)

# Khoảng giá trị từ 78% đến 83%
lower_bound = 0.78 * n
upper_bound = 0.83 * n

# Tính k cho cả hai phía của kỳ vọng
k_lower = (Ex - lower_bound) / dolechchuan
k_upper = (upper_bound - Ex) / dolechchuan
k = min(k_lower, k_upper)
print(k)
# Áp dụng bất đẳng thức Chebyshev
chebyshev_bound = 1 / (k ** 2)

# Xác suất để tỷ lệ chi tiết đạt tiêu chuẩn nằm trong khoảng từ 78% đến 83%
probability_within_bounds = 1 - chebyshev_bound

print(f"Xác suất tỷ lệ chi tiết đạt tiêu chuẩn trong khoảng từ 78% đến 83% là ít nhất: ",probability_within_bounds)
