def array_left_rotation(a, n, k):
    
    for i in range(0,k):
        a.append(a.pop(0))
        
    return a
    

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
