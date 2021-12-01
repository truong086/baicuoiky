# Viết chương trình liệt kê tất cả số nguyên tố có 5 chữ số trong pỵhon

import math
"""
* Check số nguyên tố
*
* @author viettuts.vn
* @param n: số nguyên dương
* @return true là số nguyên tố
*         false không là số nguyên tố
"""
def isPrimeNumber(n):
    #Số nguyên n < 2 không phải là số nguyên tố
    if(n < 2):
        return False;

    #Check số nguyên tố khi n >= 2
    squareRoot = int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if(n % i == 0):
            return False;
        return True;

print("Liệt kê tất cả các số nguyên tố có 5 chữ số: ");
dem = 0;
for i in range(10001, 99999):
    if(isPrimeNumber(i)):
        print(i);
        dem = dem + 1;
print("Tổng các số nguyên tố có 5 chữ số là: ", dem);