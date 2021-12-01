# Viết danh sách liệt kê các số nhỏ hơn n. Số nguyên dương n được nhập từ bàn phím
import math

"""
* Kiểm tra số nguyên tố
*
* @author viettuts.vn
* @param n: số nguyên dương
* @return true là số nguyên dương
*         false không là số nguyên tố
"""

def isPrimeNumber(n):
    # Số nguyên n < 2 không phải là số nguyên tố
    if (n < 2):
        return False;
    # Check số nguyên tố khi n >= 2
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False;
        return True;

n = int(input("Nhập vào số nguyên dương "));
print(" Tất cả các số nguyên tố nhỏ hơn  ", n , " là: ");
sb = "";
if(n >= 2):
    sb = sb + "2" + " ";
for i in range(3, n+1):
    if(isPrimeNumber(i)):
        sb = sb + str(i) + " ";
    i = i + 2;

print(sb);