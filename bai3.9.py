#1 
#P(X<440) = P(x=440) gọi là P
z=(440-(650*0.7))/((650*0.7*(1-0.7))**(1/2))
#z=-1.28 tra bảng 1 fz = 0.1758
p=(1/(650*0.8*(1-0.8)))*0.1758
print("xác suất để học sinh ít hơn 440 =",p)
#2 
#p=0.99 tra bảng ta có z=2.33
#z=(n-Ex)/Vx
n=(2.33*(650*0.7*0.3))+(650*0.7)**(1/2)
print("với xác suất 0,99 có thể đảm bảo đủ ghế chỗ cho sinh viên đến đọc sách là :",n)


