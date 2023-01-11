import random

s1="acgtacgtacgtacgt"
s2="cagtcagtcagtcagt"

match_score=5
mismatch_score=-4

one=[]
two=[]

model=[[0 for i in range(17)] for j in range(17)]

i=16
j=16

def dp(s1,s2,match_score,mismatch_score,model,i,j):
    if s1[i-1]==s2[j-1]:
        model[i][j]=dp(s1,s2,match_score,mismatch_score,model,i-1,j-1)+match_score
        return model
        one.append(s1[i-1])
        two.append(s2[j-1])
    elif s1[i-1]!=s2[j-1]:
        value=max(dp(s1,s2,match_score,mismatch_score,model,i-1,j-1),dp(s1,s2,match_score,mismatch_score,model,i,j-1),dp(s1,s2,match_score,mismatch_score,model,i-1,j))
        model[i][j]=value+mismatch_score
        one.append(s1[i-1])
        one.append("-")
        two.append(s2[j-1])
        return model
    elif i==0 or j==0:
        return 0
    else:
        break

print(one)
print(two)
dp(s1,s2,match_score,mismatch_score,model,i,j)
