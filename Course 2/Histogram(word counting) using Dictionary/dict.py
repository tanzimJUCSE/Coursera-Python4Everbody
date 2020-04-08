#In this problem you have to count the most sending email holder which will be 
#extracted from the lines strating with "From"



fname = input("Enter file name: ")
fh = open(fname)
ls=[]
rs=[]
result=dict()
for line in fh:
    if not (line.startswith('From ')):
        continue
    ls=line.split()
    rs.append(ls[1])
for mail in rs:
    result[mail]=result.get(mail,0)+1

count=0
ww=None
for word,value in result.items():
    if count<value:
        count=value
        ww=word


print("%s %d "%(ww,count))

