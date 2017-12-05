def is_matched(expression):
   
    stack = []
    mapBrackets = {'{' : '}', '[' : ']', '(' : ')', 
                   ')' : '(', ']' : '[', '}': '{'}
    opening = ['{', '(', '[']
    closing = [']', ')', '}']
    
    for i in expression:
        if i in opening:
            stack.append(i)
        if i in closing:
            if len(stack) == 0:
                return False
            else:
                if mapBrackets[i] in stack:
                    stack.pop()
                
    if len(stack) > 0:
        return False
    else:
        return True

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

