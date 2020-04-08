#typical condition
#add list with another
def addition(n):
    return n+n

numbers=[1,2,3,4,5]
res=addition(numbers)
print(res)

#using map()
#add individual value
res=map(addition,numbers)
print(list(res))

#using lambda expression
res=map(lambda x:x+x,numbers)
print(list(res))

#add two list using lambda
num=[5,4,3,2,1]
res=map(lambda x,y:x+y,numbers,num)
print(list(res))

#map can listify the list of strings individually
l=['sat','sun','mon','tues']
res=map(list,l)
print(list(res))