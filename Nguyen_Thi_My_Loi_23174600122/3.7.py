'''3.7.Xác suất sinh đc bé gái là 0.52.Tính xác suất sao cho trong 300 em bé sắp sinh có:
1.có 180 bé trai
2.số bé trai sinh ra khoảng từ 150 tới 170
3.số bé trai sinh ra dưới 170.'''
# câu a 
n = 300
p = 0.52  # vì n quá lớn , p quá nhỏ ---> phân phối chuẩn , p là xác suất sinh bé gái
muy= n * p
sigma = (n * p * (1 - p)) ** 0.5     # P sinh 180 bé trai = P sinh 120 gái ( 300 - 180 = 120)
P_180_boys = (1/sigma) * 0.0001    # tra bảng 1 thì fz((x - muy)/sigma) = fz(-4.16) ra 0.0001
print(P_180_boys , "là xác suất đẻ 180 bé trai")

# câu b 
x1 = 130
x2 = 150
P_from_150_to_170_boys = 0.2451 - 0.0013  
''' P sinh con trai trong khoảng 150-170 đứa = P sinh con gái trong khoảng 130-150 đứa
fz((x2 - muy)/sigma) - fz((x1-muy)/sigma) = fz(-0.69) - f(-3.0) = 0.2451 - 0.0013'''
print(P_from_150_to_170_boys , "là xác suất sinh ra khoảng 150-170 bé trai")

# câu c
P_less_than_170_boys = 1 - ((x1 - muy)/sigma)
'''P sinh ra ít hơn 170 con trai = P sinh ra nhiều hơn 130 con gái
vậy P sinh ra ít hơn 170 trai = 1 - fz((130-muy)/sigma) = 1 - f(-3) '''
print(P_less_than_170_boys, "là xác suất sinh ra ít hơn 170 đứa con trai")

