sigma = 2  # Với N(muy, sigma**2) theo đề bài = N(175,4) ----> sigma = 2
muy = 175
# ý 1 : Tỉ lệ người trưởng thành có tầm vóc >180cm
fz1 = (180 - muy) / sigma
fz1_new_value = 0
if fz1 == 2.5:
    fz1_new_value += 0.9938 # tra bảng 2 ta có fz(2.5) = 0.9938
P_X_greater_than_180 = 1 - fz1_new_value
print(P_X_greater_than_180, "là xác suất người trưởng thành có vóc dáng >180cm")

# ý 2: Tỉ lệ người trưởng thành có tầm vóc từ 166cm đến 177cm
fz2a = (177 -  muy) / sigma
fz2b = (166 - muy) / sigma
fz2a_new_value = 0
fz2b_new_value = 0
if fz2a == 1:
    fz2a_new_value += 0.8463 # tra bảng 2
if fz2b == -4.5:
    fz2b_new_value += 0  # tra bảng 2
P_X_between_166_and_177 = fz2a_new_value - fz2b_new_value
print(P_X_between_166_and_177, "là xác suất người trưởng thành có tầm vóc từ 166cm tới 177cm")

# ý 3: tìm h0 , nếu biết rằng 33% người trưởng thành có tầm vóc dưới mức h0
new_muy = 1.75
fz_of_h0 = 0.33 * sigma + muy 
h0 = 0
if fz_of_h0 == 2.41:
    h0 = 2.41 * 2 + 175
print(h0, "là giá trị cần tìm")