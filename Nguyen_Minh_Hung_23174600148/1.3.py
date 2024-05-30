import random

# 1) Xây dựng không gian mẫu khi ta muốn quan sát các mặt xuất hiện ở mỗi lần gieo
sample_space_1 = [1, 2, 3, 4, 5, 6]
print("Không gian mẫu khi quan sát các mặt xuất hiện ở mỗi lần gieo:", sample_space_1)

# 2) Xây dựng không gian mẫu khi ta xem xét số lần tung cho tới khi dừng lại
sample_space_2 = []
while True:
    roll = random.randint(1, 6)
    sample_space_2.append(roll)
    if roll == 6:
        break
print("Không gian mẫu khi xem xét số lần tung cho tới khi dừng lại:", sample_space_2)