import random

s="aaaaccccggggtttt"
random.shuffle(list(s))
s1=s
random.shuffle(list(s))           
s2=s

string1=string2=[]
i=j=16

model=[[0 for i in range(17)] for j in range(17)]

#Note: match score=5 and mismatch score=-4

def dp(s1,s2,model,i,j):
    if i==0 or j==0:
        return 0
    
    elif s1[i-1]==s2[j-1]:
        if model[i][j]==0:
            model[i][j]=dp(s1,s2,model,i-1,j-1)+5
            return model[i][j]
        else:
            return model[i][j]
    
    elif s1[i-1]!=s2[j-1]:
        if model[i][j]==0:
            value=max(dp(s1,s2,model,i-1,j-1),dp(s1,s2,model,i,j-1),dp(s1,s2,model,i-1,j))
            model[i][j]=value+(-4)
            return model[i][j]
        else:
            return model[i][j]
    
    else:
        pass
dp(s1,s2,model,i,j)
