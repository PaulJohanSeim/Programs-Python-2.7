# Copyright Paul-Johan Seim

# Fixed amount payback Credit card calculation
        
balance = 5000.00
annualInterestRate = 0.2 #In %
monthlyInterestRate = annualInterestRate/12.0 #In %: 0.2/12 = 0.016666

ubs=0
y = 101 #Initial balance y
lowMonthlyPay = 10
while y>=0:
    lowMonthlyPay += 10
    print lowMonthlyPay
    ubs=0 
    y = (balance-lowMonthlyPay)+(balance-lowMonthlyPay)*(monthlyInterestRate)
    print y
    while ubs<11:
        y = (y-lowMonthlyPay)+(y-lowMonthlyPay)*(monthlyInterestRate)
        print y
        ubs+=1

print ('Lowest Payment: ' +str(lowMonthlyPay))                
