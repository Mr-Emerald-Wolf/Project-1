#Making Compound Interest
p = int(input("Enter Principle: "))
r = int(input("Enter Rate of Interest: "))
t = int(input("Enter Time Period in Years: "))
c  = p*((1+r)/100)**t
print("The compound interest is ",c," and the total amount to be paid after",t,"years is",p+c)
