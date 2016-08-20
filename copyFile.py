
def thuanNghich(a):
    tmp = a
    b = int(0)
    while (int(a)>0):
        b = b*10 + int(a) % 10
        a= a/10
    print("b = ", b)
    if (tmp==b) :
        return True
    else :
        return False
so = input("Nhập vào so: ")

if (thuanNghich(int(so))==True) : print("Là số thuận nghịch")
else : print("Không là số thuận nghịch")


