# cook your dish here
T = int(input())
for _ in range(T):
    n = int(input())
    a = []
    if n<=1:
        print("-1")
        continue
    if n%2==0:
        for i in range(n):
            if i%2==0:
                a.append(2)
            else:
                a.append(-2)
    if n%2==1:
        for i in range(n-3):
            if i%2==0:
                a.append(2)
            else:
                a.append(-2)
        a.append(1)            
        a.append(2)            
        a.append(-3)            
    print(*a)
