class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        depth=0
        for c in s:
            if c=='(':
                depth+=1
                if depth>1:
                    stack.append(c)
            else:
                depth-=1
                if depth>0:
                    stack.append(c)
        return "".join(stack)
        