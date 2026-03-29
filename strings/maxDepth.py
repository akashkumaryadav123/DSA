def maxDepth( s: str):
    stack=[]
    maxD=0
    depth=0
    for i in s:
        if i=="(":
            stack.append("(")
            depth+=1
        elif i==")":
            stack.pop(-1)
            depth-=1
        maxD=max(maxD,depth)
    return maxD
print(maxDepth(s =  "()(())((()()))"))