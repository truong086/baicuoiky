# Giải phương trình bậc 2: ax2 + bx + c = 0

import math

# Giải phương trình abacj 2: ax2 + bx + c = 0
# @param a: hệ số bậc 2
# @param b: hệ số bậc 1
# @param c: Số hạng tự do

def giaiptbac2(a, b, c):
    #Kiểm tra các hệ số
    if (a == 0):
        if(b == 0):
            print("Phương trình vô nghiệp!")
        else:
            print("Phương trình có một nghiệm: x =", + (-c / b));
        return;

    #Tính delta
    delta = b * b - 4 * a * c;
    #Tính ngiệm
    if(delta > 0):
        x1 = (float) ((-b + math.sqrt(delta)) / (2 * a));
        x2 = (float) ((-b - math.sqrt(delta)) / (2 * a));
        print("Phương trình có 2 nghiệm là: x1 = ", x1, "và x2 = ", x2);
    elif(delta == 0):
        x1 = (-b / (2 * a));
        print("Phương trình có nghiệm kép: x1 = x2 = ", x1);
    else:
        print("Phương trình vô nghiệm!");

# Nhập các hệ số
a = float(input("Nhập hệ số bậc 2, a = "));
b = float(input("Nhập hệ số bậc 2, b = "));
c = float(input("Nhập hằng số tự do, python = "));

# Gọi hàm giải phương trình bậc 2
giaiptbac2(a, b, c)