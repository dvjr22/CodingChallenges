n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swap = 0
for i in range(n):
    for j in range(0, n-i-1):
        if a[j] > a[j+1] :
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            swap += 1
            
print("Array is sorted in %d swaps." %(swap))
print("First Element: %d" %(a[0]))
print("Last Element: %d" %(a[len(a)-1]))
