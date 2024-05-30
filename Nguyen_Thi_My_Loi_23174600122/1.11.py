'''Có 3 tiêu chí chọn xe hơi
A là hộp số tự động
B là động cơ V6
C là điều hòa nhiệt độ'''

p_A = 0.7
p_B = 0.75
p_C = 0.8
p_A_or_B = 0.8
p_A_or_C = 0.85
p_B_or_C = 0.9
p_A_or_B_or_C = 0.95

# ý 1 : người mua chọn ít nhất 1 trong 3 tiêu chí
p_A_and_B = p_A + p_B - p_A_or_B
p_A_and_C = p_A + p_C - p_A_or_C
p_B_and_C = p_B + p_C - p_B_or_C
p_A_and_B_and_C = p_A_or_B_or_C - p_A - p_B - p_C + p_A_and_B + p_A_and_C + p_B_and_C
print(p_A_and_B_and_C , "là xác suất người mua chọn ít nhất 1 trong 3 tiêu chí")

# ý 2: Người mua không chọn tiêu chí nào
p_no_choices = 1 - p_A_and_B_and_C
print(p_no_choices, "là xác suất người mua không chọn tiêu chí nào trong 3 tiêu chí trên")

# ý 3: Người mua chỉ chọn tiêu chí điều hòa nhiệt độ
p_only_AC_choice = p_A_or_B_or_C -  p_A_and_B
print(p_only_AC_choice, "là xác suất người mua chỉ chọn tiêu chí điều hòa")

# ý 4: Người mua chỉ chọn duy nhất 1 tiêu chí
p_only_one_choice = (3 * p_A_or_B_or_C) - p_A_and_B - p_A_and_C - p_B_and_C
print(p_only_one_choice, "là xác suất người mua chọn duy nhất 1 trong 3 tiêu chí")