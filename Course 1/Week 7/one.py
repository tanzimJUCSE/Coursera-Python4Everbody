largest =-99999999 
smallest =99999999 
while True:
    num =input("Enter a number: ")
    if num == "done":break
    try:
       n=int(num)
       if n>largest:
           largest=n

       if n<smallest :
           smallest=n
    except:
        print("Invalid input")
        

print("Maximum is", largest)
print("Minimum is", smallest)