# Viết chương trình liệt kê các số Fibonacci nhỏ hơn n là số nguyên tố trong python. N là số nguyên dương được nhập từ bàn phím

import math
"""
* Tính số fibonacci thứ n
* 
* @param n: Chỉ số của số fibonacci tính từ 0
*         vd: F0 = 0, F1 = 1, F2 = 1, F3 = 1
* @return số fibonacci thứ n
"""
def fibonacci(n):
    if(n < 0):
        return - 1;
    elif(n == 0 or n == 1):
        return n;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2);

"""
* Check số nguyên tố
*
* @param n: số nguyên tố
* @return true là số nguyên tố
*         false không phải là số nguyên tố
"""

def isPrimeNumber(n):
    # Kiểm tra n < 2 không phải là số nguyên tố
    if(n < 2):
        return False;

    # Check số nguyên tố khi n >= 2
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if(n % i == 0):
            return False;
        return True;

"""
* Chương trình liệt kê các số Fibonacci nhỏ hơn n là số nguyên tố
* Với n nhập từ bàn phím 
*
* @author viettuts.vn
"""

n = int(input("Nhập số nguyên dương n = "));
print("Tất cả các số Fibonacci nhỏ hơn ", n, " và nguyên tố:");
i = 0;
fin = fibonacci(i);
while (fin < n):
    fin = fibonacci(i);
    if(isPrimeNumber(fin)):
        print(fin);
    i = i + 1;
