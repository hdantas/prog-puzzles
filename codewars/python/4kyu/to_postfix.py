def to_postfix (infix):
    precedence = {'(':0,'+':1,'-':1,'*':2,'/':2,'^':3}
    postfix = ""
    stack = []

    for token in infix:
        if token == '(': stack.append(token)
        elif token == ')': # When ) is found
            while(stack[-1] != '('): postfix += stack.pop() # pop until we find the matching (
            stack.pop() # clear '(' from the stack
        elif token in str(range(0,10)): postfix += token #When an operand is read, output it
        elif token in "+-*/^": #When an operator is read
            while(stack and precedence[stack[-1]] >= precedence[token]): postfix += stack.pop() #Pop until the top of the stack has an element of lower precedence
            stack.append(token) #Then push it
    
    return postfix + ''.join(stack[::-1])

print to_postfix("2+7*5") == "275*+"
print to_postfix("(((3*3)/(7+1)))") == "33*71+/"
print to_postfix("5+(6-2)*9+3^(7-1)") == "562-9*+371-^+"
print to_postfix("(5-4-1)+9/5/2-7/1/7") == "54-1-95/2/+71/7/-"