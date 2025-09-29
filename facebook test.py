A = [[1,5],[10,14],[16,18]]
B = [[2,6],[8,10],[11,20]]


# [[1, 6], [8, 20]]


i = 0
j = 0
res = []

while i < len(A) or j < len(B):

    if i==len(A):
        curr = B[j]
        j+=1
    
    elif j==len(B):
        curr = A[i]
        i+=1

    elif A[i][0] < B[j][0]:
        curr = A[i]
        i+=1
    else:
        curr = B[j]
        j+=1

    if res and res[-1][1] >= curr[0]:
        res[-1][1] = max(res[-1][1],curr[1])
    else:
        res.append(curr)

print(res)