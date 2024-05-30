################## BÀI 1.9 ######################

P1 = 0.5                  # Xsuat trúng thầu dự án thứ nhất
P2 = 0.4                  # Xsuat trúng thầu dự án thứ hai
P1_P2 = 0.1               # Xsuat trúng cả hai dự án

# 1) Xsuất trúng ít nhất 1 dự án
Xac_suat_1 = P1 + P2 - P1_P2
print("1) Xác suất trúng ít nhất 1 dự án:", Xac_suat_1)
# 2) Xsuất trúng đúng 1 dự án
Xac_suat_2= (P1 - P1_P2) + (P2 - P1_P2)
print("2) Xác suất trúng đúng 1 dự án:", Xac_suat_2)
# 3) Xsuất trúng thầu dự án thứ 2 biết đã trúng dự án thứ 1
Xac_suat_3= P1_P2 / P1
print("3) Xác suất trúng thầu dự án thứ 2 biết đã trúng dự án thứ 1:", Xac_suat_3)
# 4) Xsuất trúng thầu dự án thứ 2 biết rằng không trúng dự án thứ 1
Xac_suat_4 = (P2 - P1_P2) / (1 - P1)
print("4) Xác suất trúng thầu dự án thứ 2 biết rằng không trúng dự án thứ 1:",Xac_suat_4)

