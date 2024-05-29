A1=0.34
A2=0.3
A3=0.3
A=A1+A2+A3
#gọi b1 là số sinh đôi giả có cùng giới tính nam
#gọi b2 là số sinh đôi giả có cùng giới tính nữ
b1=0.5*0.5
b2=0.5*0.5
# C cặp sinh đôi thật = tổng cặp sinh đôi cùng giới - số sinh đôi giả có cùng giới
# tỉ lệ cặp sinh đôi thật
C=A1+A2-b1-b2
# tỉ lệ cặp sinh đôi thật trong số các cặp sinh đôi có cùng giới tính
D=C/(A1+A2)
print("tỉ lệ cặp sinh đôi thật =",C)
print("tỉ lệ cặp sinh đôi thật trong số các cặp sinh đôi có cùng giới tính =",D)