# Viết chương trình phân tích số nguyên tố n thành các thừa số nguyên tố trong python. Ví dụ 100 = 2x2x5x5

"""
* Phân tích số nguyên thành tích
*
* @param positiveInt
* @return
"""

def PhanTichSoNguyen(n):
    i = 2;
    listnumber = [];
    #Phân tích
    while(n > 2):
        if(n % i == 0):
            n = int(n / i);
            listnumber.append(i);
        else:
            i = i + 1;
    # Nếu listnumber mà trống thì add n vào listnumber
    if(len(listnumber) == 0):
        listnumber.append(n);
    return listnumber;

n = int(input("Nhập số nguyên dương n = "));
# Phân tích số nguyên dương n
listnumber = PhanTichSoNguyen(n);
size = len(listnumber);
sb = "";
for i in range(0, size - 1):
    sb = sb + str(listnumber[i]) + " x ";
sb = sb + str(listnumber[size - 1]);

# In kết quả ra màn hinhg
print("Kết quả ", n, " = ", sb);