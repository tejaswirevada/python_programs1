#Compound Interest:
p=float(input("Enter Principal amount:"))
r=float(input("Enter Rate of Interest:"))
t=float(input("Enter Time (in Years):"))
amount=p*(1+r/100)**t
CI=amount-p
print("Total Amount=",amount)
print("Compound Interest=",CI)
