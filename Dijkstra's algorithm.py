#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sam_PC
#
# Created:     22.01.2016
# Copyright:   (c) sam_PC 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

v =6
V = [i for i in range(1,v+1)]
start = 1
w = [[0, 6, 2, 0,0,0], [0, 0, 0, 4,1,2], [0, 0, 0, 0,0,0], [0, 0, 0, 0,0,0], [0, 0, 0, 0,0,0], [0, 0, 0, 0,0,0]]
d = {}
for i in range(1,v+1):
    d[i]=float("Inf")
d[start]=0
Q=V[:]
while Q!=[]:
    u = min(Q, key= lambda k: d[k])
    for i in range(6):
        if w[u-1][i]!=0:
            if d[i+1]>d[u]+w[u-1][i]:
                d[i+1] = d[u]+w[u-1][i]

    Q.remove(u)
print(d)

