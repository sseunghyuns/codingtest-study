n, m = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
    
m, k = map(int, input().split())
B = []
for _ in range(m):
    B.append(list(map(int, input().split())))
    


for i in range(len(A)):
    arr = []
    for j in range(len(B[0])):
        val = 0
        for k in range(len(B)):
            val+=(A[i][k]*B[k][j])
        print(val, end= ' ')
    print()

# 3x2
# [1,2]
# [3,4]
# [5,6]

# 2x3
# [-1,-2,0]
# [0, 0, 3]

