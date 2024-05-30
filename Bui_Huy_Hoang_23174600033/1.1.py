# ý a
omega = 0
for i in range(1,7):
    for j in range(1,7):
        omega += 1
print(omega, "là không gian các biến cố sơ cấp")

# ý b 
count = 0
for i in range(1,7):
    for j in range(1,7):
        if i + j ==7:
            count += 1
seven_dots_probability = count/omega
print(seven_dots_probability, "là xác suất để tổng số chấm = 7")

