hrs=float(input("Enter hrs:"))
rph=float(input("Enter rph:"))
if hrs>40 :
	p=40*rph+(h-40)*1.5*rph
else :
	p=hrs*rph
print(p)	