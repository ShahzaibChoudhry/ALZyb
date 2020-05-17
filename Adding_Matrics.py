
a = [[9,8,3],
     [5,8,2],
     [5,4,1]]
b = [[5,6,2],
     [7,7,2],
     [3,8,9]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(a)):
    for c in range(len(a[0])):
        result[i][c] = a[i][c] + b[i][c]
for d in result:
    print(d)