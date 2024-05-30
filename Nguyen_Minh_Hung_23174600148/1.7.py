import random

# Hàm tính tổ hợp
def combination(n, k):
    a = 1
    b = 1
    for i in range(k):
        a *= (n - i)
        b *= (i + 1)
    return a // b

# Tính xác suất cho từng trường hợp
def probabilities():
    total_ways = combination(10, 6)
    
    # 1) Xác suất để cả 6 người là nam
    all_male_ways = combination(6, 6)
    prob_all_male = all_male_ways / total_ways

    # 2) Xác suất để có 4 nam và 2 nữ
    four_male_ways = combination(6, 4)
    two_female_ways = combination(4, 2)
    prob_four_male_two_female = (four_male_ways * two_female_ways) / total_ways

    # 3) Xác suất để có ít nhất 2 nữ
    no_female_ways = combination(6, 6)
    only_one_female_ways = combination(6, 5) * combination(4, 1)
    prob_at_least_two_female = 1 - ((no_female_ways + only_one_female_ways) / total_ways)

    return prob_all_male, prob_four_male_two_female, prob_at_least_two_female

# In kết quả
prob_all_male, prob_four_male_two_female, prob_at_least_two_female = probabilities()
print("1) Xác suất để cả 6 người là nam:", prob_all_male)
print("2) Xác suất để có 4 nam và 2 nữ:", prob_four_male_two_female)
print("3) Xác suất để có ít nhất 2 nữ:", prob_at_least_two_female)
