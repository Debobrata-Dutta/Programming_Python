a=input()
l=[]
for i in a:
    if(i>='0' and i<='9'):
        l.append(int(i))
print(sum(l))
print(sum(l)/len(l))
