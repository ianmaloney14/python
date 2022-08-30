for i in range(0, 151, 1):
    print(i)

for i in range(5, 1001, 5):
    print(i)

for i in range(1, 101):
    if i%10 == 0:
        print("Coding")
    elif i%5 == 0:
        print("Coding Dojo")
    else:
        print(i)

oddsum = 0
for i in range(1, 500001, 2):
    oddsum += i
print(oddsum)

for i in range(2018, 1, -4):
    print(i)

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum, 3):
    print(i+1)
