def ransom_note(magazine, ransom):
    
    mapMag = {}
    
    for i in magazine:
        if i not in mapMag:
            mapMag[i] = 1
        else:
            mapMag[i] +=1
         
    for i in ransom:
        mapMag[i] -= 1
        
    for key, value in mapMag.items():
        if value < 0:
            return False
    
    return True
    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
