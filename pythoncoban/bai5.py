# Viết chương trình tìm ước số chung lớn nhất (USCLN) và bội số chung nhỏ nhất (BSCNN) của hai số nguyên dương a và b
# nhập từ bàn phím

# Sử dụng thuật toán Euclid

"""
* Tìm ước số chung lớn nhất (USCLN)
*
* @param a: Số nguyên dương
* @param b: Số nguyên dương
* @return USCLN của a và b
"""

def uscln(a, b):
    if(b==0):
        return a;
    return uscln(b, a % b);

"""
* Tìm bội số chung nhỏ nhất (BSCNN)
*
* @param a: Số nguyên dương
* @param b: Số nguyên dương
* @return BSCNN của a và b
"""

def bscnn(a, b):
    return int((a * b) / uscln(a, b));

a = int(input("Nhập số nguyên dương a = "));
b = int(input("Nhập số nguyên dương b = "));

# tính USCLN của a và b
print("Ước số chung lớn nhất của ", a, " và ", b, " là: ", uscln(a, b));
print("Bội số chung nhỏ nhất của ", a, " và ", b, " là: ", bscnn(a, b));