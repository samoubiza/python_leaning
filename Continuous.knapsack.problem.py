n, w = (int(x) for x in input().split())
a1 = [[int(x) for x in input().split()] for i in range(n)]
a1.sort(key=lambda x: x[0]/x[1], reverse=True)
sum = 0

for i in range(len(a1)):
    print(i)
    if w>=a1[i][1]:
        sum+=a1[i][0]
        w-=a1[i][1]
    else:
        sum+=float(w*(a1[i][0]/a1[i][1]))
        break
print(sum)