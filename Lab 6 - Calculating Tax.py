#Lab 6 - Calculating Tax

personalAllowance = 11850

salary = int(input("Enter your salary: "))

def tax20():
   return (salary - (salary * 0.2))

def tax40():
   return (salary - (salary * 0.4))

def tax45():
   return (salary - (salary * 0.45))
   

def getIncomeTax():

    print("Calculating income tax...")

    if salary < 11850:
       print ("Salary within range of personal allowance. Income tax is 0%.")
    
    elif 11851 <= salary <= 34500:
       print (f"Tax is set at 20%. Your salary after tax is: £",tax20())
    
    elif 34501 <= salary <= 150000:
        print (f"Tax is set at 40%. Your salary after tax is: £",tax40())

    elif 150001 <= salary:
       print (f"Tax is set at 45%. Your salary after tax is: £",tax45())
    
getIncomeTax()




    

    



