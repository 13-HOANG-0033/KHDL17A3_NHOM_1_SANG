b1 = b2 = b3 = b4 = True
# ý 1 : có đúng 1 sinh viên đạt yêu cầu
one_pass = [b1 and not b2 and not b3 and not b4] or [not b1 and b2 and not b3 and not b4] or [not b1 and not b2 and b3 and not b4] or [not b1 and not b2 and not b3 and b4]

# ý 2: có đúng 3 sinh viên đạt yêu cầu
three_pass = [b1 and b2 and b3 and not b4] or [not b1 and b2 and b3 and b4] or [b1 and not b2 and b3 and b4] or [b1 and b2 and not b3 and b4]

# ý 3: có ít nhất 1 sinh viên đạt yêu cầu
at_least_one_pass = [not b4]

# ý 4: không có sinh viên đạt yêu cầu
fail = [not b1 and not b2 and not b3 and not b4]

# chương trình chính
choice = input("Bạn muốn biểu diễn các biến cố của ý mấy?(1,2,3,4): ")
if choice.isdigit() ==1:
    print(one_pass)
elif choice.isdigit() ==2:
    print(three_pass)
elif choice.isdigit() ==3:
    print(at_least_one_pass)
elif choice.isdigit() ==4:
    print(fail)
else:
    print("Lựa chọn không hợp lệ")

