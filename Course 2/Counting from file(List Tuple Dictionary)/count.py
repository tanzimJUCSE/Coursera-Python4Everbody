fname = input("Enter file name: ")
fh = open(fname)
ls=[]
rs=[]
result=[]
ans=[]
d=dict()
for line in fh:
    if not (line.startswith('From ')):
        continue
    ls=line.split()
    rs.append(ls[5])
print(rs)
for i in range(len(rs)):
    result=rs[i].split(':')
    del result[1:3]
    ans=ans+result

ans.sort()
for name in ans:
    d[name]=d.get(name,0)+1
for key,value in d.items():
    print("%s %d" %(key,value))
