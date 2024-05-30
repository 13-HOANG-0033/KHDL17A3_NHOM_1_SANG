# ý 1 : X có phân phối chuẩn
normal_prob = 0.9987 - 0.0013
'''Ta có P(|X - muy| < ( 3 * sigma) = P(-3 * sigma < X - muy < 3 * sigma)
------> P((-3 * sigma) + muy < X < (3 * sigma) + muy)
    <=>   fz(((3*sigma) + muy - muy) / sigma)) -  fz(((-3*sigma) + muy - muy) / sigma))
    <=>    fz(3) - fz(-3) tra bảng 2 ta có 0.9987 - 0.0013
'''
print(normal_prob , "là phân phối chuẩn")

# ý 2 : X có phân phối mũ 
import math 
muy = 1    # do đề bài không có giá trị cụ thể cho muy và sigma nên ta giả định muy và sigma = 1
sigma = 1
exp_prob  = math.erf(-muy * (-3*sigma) +muy) - math.erf(-muy * (3*sigma) +muy)
print(exp_prob, "là phân phối mũ")

# ý 3 : phân phối đều trên đoạn [-1,1]
a = -1
b = 1
fx = 1/(b-a)
sigma = 3  # đề bài không có giá trị cụ thể nên ta giả định sigma =3, muy =2
muy = 2
uniform_prob = fx * ((3*sigma) + muy) - ((-3*sigma) + muy)
print(uniform_prob, "+c", "là phân phối đều trên đoạn [-1,1]")  