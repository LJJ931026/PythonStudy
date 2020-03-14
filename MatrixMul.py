n = int(input("Enter the number of matrix: "))
print("Enter values for matrix A")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
print("Enter values for matrix B")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append(a[i][j] * b[i][j] for j in range(n))
print("After matrix values")
print("-" * 7 * n)
for x in c:
    for y in x:
        print(str(y).rjust(5), end=' ')
    print()
print("-" * 7 * n)


