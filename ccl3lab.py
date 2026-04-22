name = input ("Enter your Name: ")
hrsworkd = float(input("Enter Number of Hours Worked: "))
numbrhrsot = float(input("Enter Number of Hours Over time: "))
sss = float(input("Enter SSS Contribution: "))
phc = float(input("Enter Philhealth Contribution: "))
hlm = float(input("Enter Housing Loan Amount: ")) 
tax_rate = 0.20
tax_amount = tax_rate * (hrsworkd * 250 + numbrhrsot * 300)
gross_salary = hrsworkd * 250 + numbrhrsot * 300
total_deduction = sss + phc + hlm + tax_amount
net_salary = gross_salary - total_deduction

print("================= PAY SLIP ====================")

print("NAME:", name)
print("GROSS SALARY:", f"{gross_salary:.2f}")
print("SSS:", f"{sss:.2f}")
print("PHILHEALTH:", f"{phc:.2f}")
print("HOUSING LOAN:", f"{hlm:.2f}")
print("Tax:", f"{tax_amount:.2f}")
print("TOTAL DEDUCTION:", f"{total_deduction:.2f}")
print("NET SALARY:", f"{net_salary:.2f}")
print("===============================================")


#selection
if name == "__main__":
    print("This code is running smoothly.")
elif name != "__main__":
    print("This code is not running smoothly.")
else:
    print("This code is kinda running smoothly.")



