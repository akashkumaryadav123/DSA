# def rotatedStrings(s:str,goal:str):
#     if len(s)!=len(goal):
#         return False
#     for start in range(len(s)):
#         if goal[start]==goal[0]:
#             match=True
#             for i in range(len(s)):
#                 if s[(start+i)%len(s)]!=goal[i]:
#                     match=False
#             if match:
#                 return True
    
#     return False
# print(rotatedStrings("defdefdefabcabc","defdefabcabcdef"))

        
def rotateStrings(s:str,goal:str):
    if len(s)!=len(goal):
        return False
    return goal in (s+s)