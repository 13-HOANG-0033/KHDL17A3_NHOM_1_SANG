#n=3000,p=1/6
#1 
#tìm z của fz1 và z của fz2
z1=(550-3000*1/6)/((3000*(1/6)(1-(1/6)))**(1/2))
z2=(450-(3000*(1/6)))/((3000*(1/6)(1-(1/6)))**(1/2))
#z1 = 3/25,z2=-3/25
#theo bảng 2 fz1=0.5478, fz2= 0.4522
P=0.5478-0.4522
print("m xác suất tối thiểu để số lần xuất hiện mặt sáu chấm nằm trong khoảng từ 450 đến 550 :",P)

#2
X=Ex=3000*1/6
p=3.5/X
Vx=X*p*(1-p)
#P(|X-3.5|)<0.1=Vx/(0.1**2)
Px=Vx/(0.1**2)
print("xác suất của biến cố: |X-3,5|<0,1 =",Px)
