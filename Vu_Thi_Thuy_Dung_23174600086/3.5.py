###################### BÀI 3.5 ###########################

P = 0.1              # Xsuất trúng dự án
M = 0                # Tổng xsuất

# Duyệt qua tất cả các giá trị có thể của X
for X in range(15):
    Xac_Suat = ((1 - P) ** (14 - X)) * (P ** X)                 # Tính xsuất X = x
    for Y in range(10):                                         # Duyệt qua tcả các gtrị có thể của Y
        for Z in range(8):                                       # Duyệt qua tcả các gtrị có thể của Z
            if X + Y + Z == 4:
               M += Xac_Suat * ((1 - P)**(9 - Y))*(P**Y)*((1-P)**(7-Z))*(P**Z)  # Tích của xsuất X,xsuất Y và Z
print("P(X + Y + Z = 4):", M)

