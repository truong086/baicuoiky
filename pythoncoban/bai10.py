# Viết chương trình tính tổng của các chữ số của một số nguyên n trong python. Số nguyên n được nhập từ bàn phím
# Với n = 1234, tổng các chữ số:: 1 + 2 + 3 + 4 = 10

"""
* Tính tổng các chữ số của một số nguyên dương n
*
* @param n: số nguyên dương
* @return
"""

def tinhtong(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;

n = int(input("Nhập số nguyên dương n = "));
print("tổng các chữ số ", n, " là ", tinhtong(n));