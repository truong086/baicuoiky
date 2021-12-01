# Viết chương trình liệt kê n số nguyên tố đầu tiên trong python. Số nguyên dương n dduwwocj nhập từ bàn phím

import math
"""
* Check số nguyên tố
*
* @author viettuts.vn
* @param n : số nguyên dương
* @return true là số nguyên tố
*         false không phải số nguyên tố
"""

def isPrimeNumber(n):
    # Kiểm tra n < 2 không phải số nguyên tố
    if (n < 2):
        return False;
    # Check số nguyên tố khi n >= 2
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if(n % i == 0):
            return False;
        return True;

n = int(input("Nhập vào số nguyên dương n = "));
print(n, "Số nguyên tố đầu tiên là: ");
dem = 0; # Đếm số nguyên tố
i = 2; # Tìm số nguyên tố bắt đầu từ số 2
sb = "";
while (dem < n):
    if(isPrimeNumber(i)):
        sb = sb + str(i) + " ";
        dem = dem + 1;
    i = i + 1;
print(sb);