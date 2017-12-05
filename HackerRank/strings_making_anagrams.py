def number_needed(a, b):
    
    mapA = {}
    mapB = {}
    
    for i in a:
        if i not in mapA:
            mapA[i] = 1
        else:
            mapA[i] += 1
            
    for i in b:
        if i not in mapB:
            mapB[i] = 1
        else:
            mapB[i] += 1
            
    count = 0
    
    for key, value in mapA.items():
        if key not in mapB:
            count += mapA[key]
        else:
            count += max(0, value - mapB[key])
            
            
    for key, value in mapB.items():
        if key not in mapA:
            count += mapB[key]
        else:
            count += max(0, value - mapA[key])
    
    return count

a = input().strip()
b = input().strip()

print(number_needed(a, b))
