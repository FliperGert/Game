r = int(input())
di = {}
for i in range(1, r):
    for j in range(1, r):
        for k in range(1, r):
            if i ** 2 + j ** 2 == k ** 2:
                di[k] = [i, j]

print(di )
print('end')
# I don't remember