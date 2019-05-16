print("'                                                       HERE IS YOUR REPORT ANALYSIS                                                   '")
t=700
at=100
e=float(input("ENTER YOUR MARKS IN-ENGLISH"))
h=float(input("ENTER YOUR MARKS IN-HINDI"))
m=float(input("ENTER YOUR MARKS IN-MATHS"))
s=float(input("ENTER YOUR MARKS IN-SCIENCE"))
sst=float(input("ENTER YOUR MARKS IN-SOCIAL SCIENCE"))
cs=float(input("ENTER YOUR MARKS IN-COMPUTER SCIENCE"))
sy=float(input("ENTER YOUR MARKS IN-PSYCHOLOGY"))

a=((e+h+m+s+cs+sst+sy)/7)
p=((e+h+m+s+cs+sst+sy)/700)(100)
print("YOUR AVERAGE IS--", a)
print("YOUR TOTAL PERCENTAGE IS--", p)

sp= input("enter the subject whose percentage you want to know")
if sp=='ENGLISH':
    ep=((e/100)(100))
    print(ep)
elif sp=='MATHS':
    ep=((m/100)(100))
    print(ep)
elif sp=='SCIENCE':
    ep=((s/100)(100))
    print(ep)
elif sp=='SOCIAL SCIENCE':
    ep=((sst/100)(100))
    print(ep)
elif sp=='COMPUTER SCIENCE':
    ep=((cs/100)(100))
    print(ep)
elif sp=='HINDI':
    ep=((h/100)(100))
    print(ep)
elif sp=='PSYCOLOGY':
    ep=((sy/100)(100))
    print(ep)                        
