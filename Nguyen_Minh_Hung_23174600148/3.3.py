import math

# Tính xác suất của câu 1
def prob_X_equals_k(k):
    n = 9
    p = 3 / 5
    return (math.factorial(n) / (math.factorial(k) * math.factorial(n - k))) * (p ** k) * ((1 - p) ** (n - k))

# Tính xác suất của câu 2
def prob_Y_equals_k_given_X_equals_k(k):
    prob_X_4 = prob_X_equals_k(4)
    prob_Y_4_and_X_4 = (math.factorial(4) / (math.factorial(k) * math.factorial(4 - k))) / (math.factorial(9) / (math.factorial(4) * math.factorial(9 - 4)))
    return prob_Y_4_and_X_4 / prob_X_4

# In kết quả
print("1) Xác suất để có 4 lần nhận được bi vàng:", prob_X_equals_k(4))
print("2) Xác suất để các bi vàng đó được nhận ở các lần lấy thứ chẵn:", prob_Y_equals_k_given_X_equals_k(4))
