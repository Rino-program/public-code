x = float(input("数を入力:"))
y = 0
while x != int(x*(10**y))/(10**y):
    y+=1
numerator = int(x*(10**y))
denominator = 10**y
for i in range(numerator,1,-1):
    if numerator % i == 0 and denominator % i == 0:
        numerator = numerator // i
        denominator = denominator // i
print(f"{numerator}/{denominator}")