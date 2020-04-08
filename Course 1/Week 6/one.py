def computepay(h,r):
    if h>40:
        return (40*r+(h-40)*1.5*r)
    else :
        return h*r

hrs = float(input("Enter Hours:"))
rph = float(input("Enter Rate per hour:"))
p = computepay(hrs,rph)
print("Pay",p)